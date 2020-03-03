from abc import ABC, abstractmethod
from typing import Optional, Iterator

from swapi.models import APIResponse


class AbstractReader(ABC):
    @abstractmethod
    def get(self, resource) -> Optional[Iterator[APIResponse]]:
        pass


class AbstractWriter(ABC):
    @abstractmethod
    def save(self, folder, file, data):
        pass


class AbstractModel(ABC):
    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def list(self):
        pass
