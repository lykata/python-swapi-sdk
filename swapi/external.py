import logging
from typing import Iterator

import requests

from swapi.models import APIResponse

logger = logging.getLogger(__name__)


class DataFetcher(object):
    def __init__(self):
        self.base_url = "https://swapi.co/api"
        self.response = None

    def _get(self, url: str) -> APIResponse:
        return APIResponse(**requests.get(url).json())

    def _fetch_more(self) -> Iterator[APIResponse]:
        while self.response.next:
            self.response = self._get(self.response.next)
            logger.info("fetching more from SWAPI")
            yield self.response

    def get(self, resource) -> Iterator[APIResponse]:
        logger.info("fetching from SWAPI")
        self.response = self._get(f"{self.base_url}/{resource}/")
        return self._fetch_more()



