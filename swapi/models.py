from dataclasses import dataclass
from typing import Iterator, Generic, TypeVar


@dataclass
class APIResponse:
    next: str
    count: str
    results: list
    previous: str


Model = TypeVar('Model')


class QueryResult(Generic[Model]):
    def __init__(self, count: int, iterator: Iterator[Model]):
        self._count = count
        self._iterator = iterator

    def iter(self) -> Iterator[Model]:
        return self._iterator

    def count(self):
        return self._count


class QueryResultBuilder:
    def __init__(self):
        self._count = None
        self._iterator = None

    def count(self, count):
        self._count = count
        return self

    def iterator(self, iterator):
        self._iterator = iterator
        return self

    def build(self) -> QueryResult:
        return QueryResult(
            count=self._count,
            iterator=self._iterator
        )
