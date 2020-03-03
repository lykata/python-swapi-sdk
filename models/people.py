import toolz

from interfaces import AbstractModel
from swapi.models import QueryResultBuilder, QueryResult
from interfaces import AbstractReader
from swapi_gen.people import People


class PeopleModel(AbstractModel):
    def __init__(self, store: AbstractReader):
        self.store = store

    def list(self) -> QueryResult[People]:
        responses = self.store.get("people")
        response, responses = toolz.peek(responses)
        return QueryResultBuilder() \
            .count(response.count) \
            .iterator(toolz.mapcat(lambda r: (People(p) for p in r.results), responses)) \
            .build()

    def get(self, id):
        raise NotImplemented
