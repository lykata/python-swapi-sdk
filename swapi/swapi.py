from logging import getLogger

from models.planet import PlanetsModel
from models.specie import SpecieModel
from models.starship import StarshipModel
from models.vechicle import VehicleModel
from swapi.external import DataFetcher
from models.people import PeopleModel
from interfaces import AbstractReader
from swapi.stores import FileStore, CacheStore

logger = getLogger(__name__)


class Client:
    def __init__(self, reader: AbstractReader):
        self.planet = PlanetsModel(reader)
        self.people = PeopleModel(reader)
        self.vehicle = VehicleModel(reader)
        self.specie = SpecieModel(reader)
        self.starship = StarshipModel(reader)


class ClientBuilder:
    def __init__(self):
        self.store = None

    def with_store(self, store):
        self.store = store
        return self

    def build(self):
        client = Client(self.store)
        return client

    @staticmethod
    def default():
        client = Client(CacheStore(FileStore("cache"), DataFetcher()))
        return client


