import dataclasses
import json
import os
from abc import ABCMeta
from typing import Optional, Iterator

import toolz

from swapi.filesystem import mkdirs_from_path
from swapi.models import APIResponse
from interfaces import AbstractReader, AbstractWriter


class AbstractStore(AbstractReader, AbstractWriter, metaclass=ABCMeta):
    pass


class FileStore(AbstractStore):
    def __init__(self, path: str):
        self.path = path

    def get(self, resource_name: str) -> Optional[Iterator[APIResponse]]:
        resource_path = os.path.join(self.path, resource_name)
        try:
            for part in os.listdir(resource_path):
                joined = os.path.join(resource_path, part)
                with open(joined) as f:
                    yield APIResponse(**json.load(f))
        except FileNotFoundError:
            return None

    def save(self, folder: str, file: str, data: dict):
        resource_path = os.path.join(self.path, folder, file)
        mkdirs_from_path(resource_path)
        with open(resource_path, 'w') as f:
            f.write(json.dumps(data))


class CacheStore(AbstractReader):
    def __init__(self, store: AbstractStore, client):
        self.client = client
        self.store = store

    def _fetch_from_swapi(self, resource) -> Iterator[APIResponse]:
        responses = self.client.get(f"{resource}")
        for page in responses:
            if page.next:
                page_number = page.next.split("?")[1].split("=")[1]
                self._save(resource, f"{page_number}.json", page)
                yield page

    def get(self, resource) -> Iterator[APIResponse]:
        responses = self.store.get(resource)
        try:
            # We need to peek in order to know if we got something or not.
            # An Iterator will be returned or an StopIteration will be raised.
            _, responses = toolz.peek(responses)
        except StopIteration:
            responses = None
        if responses:
            for r in responses:
                yield r
        else:
            for r in self._fetch_from_swapi(resource):
                yield r

    def _save(self, resource, filename: str, data: APIResponse):
        self.store.save(resource, filename, dataclasses.asdict(data))
