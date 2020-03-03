import toolz

from interfaces import AbstractModel
from swapi.models import QueryResultBuilder, QueryResult
from swapi.stores import AbstractStore
from swapi_gen.specie import Specie


class SpecieModel(AbstractModel):
    def __init__(self, store: AbstractStore):
        self.store = store

    def get(self, id):
        raise NotImplemented

    def list(self) -> QueryResult[Specie]:
        responses = self.store.get("planets")
        response, responses = toolz.peek(responses)
        return QueryResultBuilder() \
            .count(response.count) \
            .iterator(toolz.mapcat(lambda r: (Specie(p) for p in r.results), responses)) \
            .build()
