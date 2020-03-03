from collections import UserDict
from collections import UserList

class Film(UserDict):
    """This represents a JSON object.
    """
    class StarshipsProperty (UserList):
        """ This represents a JSON array.
        """
        
        def __init__(self, the_list=None):
            """Initializer for array.
            """
            self.the_list = the_list

            if isinstance(the_list, type(self)):
                super().__init__(the_list.data)
            else:
                super().__init__([(x) for x in the_list])

        def Append(self, new_value):
            self.data.append((new_value))
            return self

        def Serializable(self):
            return self.data

    class SpeciesProperty (UserList):
        """ This represents a JSON array.
        """
        
        def __init__(self, the_list=None):
            """Initializer for array.
            """
            self.the_list = the_list

            if isinstance(the_list, type(self)):
                super().__init__(the_list.data)
            else:
                super().__init__([(x) for x in the_list])

        def Append(self, new_value):
            self.data.append((new_value))
            return self

        def Serializable(self):
            return self.data

    class EpisodeIdProperty(object):
        """ This class is a schema-validating wrapper around a integer.
        """

        def __init__(self, value):
            self.Set(value)

        @staticmethod
        def _Validate(value):
            if not isinstance(value, int):
                raise ValueError("Passed value was not a integer")        

        def Set(self, new_value):
            if isinstance(new_value, type(self)):
                self._value = new_value._value
            else:
                self._Validate(new_value)
                self._value = new_value
            return self

        def Get(self) -> int:
            return self._value

        def Serializable(self):
            return self.Get()

    class ProducerProperty(object):
        """ This class is a schema-validating wrapper around a string.
        """

        def __init__(self, value):
            self.Set(value)

        @staticmethod
        def _Validate(value):
            if not isinstance(value, str):
                raise ValueError("Passed value was not a string")        

        def Set(self, new_value):
            if isinstance(new_value, type(self)):
                self._value = new_value._value
            else:
                self._Validate(new_value)
                self._value = new_value
            return self

        def Get(self) -> str:
            return self._value

        def Serializable(self):
            return self.Get()

    class EditedProperty(object):
        """ This class is a schema-validating wrapper around a string.
        """

        def __init__(self, value):
            self.Set(value)

        @staticmethod
        def _Validate(value):
            if not isinstance(value, str):
                raise ValueError("Passed value was not a string")        

        def Set(self, new_value):
            if isinstance(new_value, type(self)):
                self._value = new_value._value
            else:
                self._Validate(new_value)
                self._value = new_value
            return self

        def Get(self) -> str:
            return self._value

        def Serializable(self):
            return self.Get()

    class CreatedProperty(object):
        """ This class is a schema-validating wrapper around a string.
        """

        def __init__(self, value):
            self.Set(value)

        @staticmethod
        def _Validate(value):
            if not isinstance(value, str):
                raise ValueError("Passed value was not a string")        

        def Set(self, new_value):
            if isinstance(new_value, type(self)):
                self._value = new_value._value
            else:
                self._Validate(new_value)
                self._value = new_value
            return self

        def Get(self) -> str:
            return self._value

        def Serializable(self):
            return self.Get()

    class OpeningCrawlProperty(object):
        """ This class is a schema-validating wrapper around a string.
        """

        def __init__(self, value):
            self.Set(value)

        @staticmethod
        def _Validate(value):
            if not isinstance(value, str):
                raise ValueError("Passed value was not a string")        

        def Set(self, new_value):
            if isinstance(new_value, type(self)):
                self._value = new_value._value
            else:
                self._Validate(new_value)
                self._value = new_value
            return self

        def Get(self) -> str:
            return self._value

        def Serializable(self):
            return self.Get()

    class DirectorProperty(object):
        """ This class is a schema-validating wrapper around a string.
        """

        def __init__(self, value):
            self.Set(value)

        @staticmethod
        def _Validate(value):
            if not isinstance(value, str):
                raise ValueError("Passed value was not a string")        

        def Set(self, new_value):
            if isinstance(new_value, type(self)):
                self._value = new_value._value
            else:
                self._Validate(new_value)
                self._value = new_value
            return self

        def Get(self) -> str:
            return self._value

        def Serializable(self):
            return self.Get()

    class ReleaseDateProperty(object):
        """ This class is a schema-validating wrapper around a string.
        """

        def __init__(self, value):
            self.Set(value)

        @staticmethod
        def _Validate(value):
            if not isinstance(value, str):
                raise ValueError("Passed value was not a string")        

        def Set(self, new_value):
            if isinstance(new_value, type(self)):
                self._value = new_value._value
            else:
                self._Validate(new_value)
                self._value = new_value
            return self

        def Get(self) -> str:
            return self._value

        def Serializable(self):
            return self.Get()

    class TitleProperty(object):
        """ This class is a schema-validating wrapper around a string.
        """

        def __init__(self, value):
            self.Set(value)

        @staticmethod
        def _Validate(value):
            if not isinstance(value, str):
                raise ValueError("Passed value was not a string")        

        def Set(self, new_value):
            if isinstance(new_value, type(self)):
                self._value = new_value._value
            else:
                self._Validate(new_value)
                self._value = new_value
            return self

        def Get(self) -> str:
            return self._value

        def Serializable(self):
            return self.Get()

    class PlanetsProperty (UserList):
        """ This represents a JSON array.
        """
        
        def __init__(self, the_list=None):
            """Initializer for array.
            """
            self.the_list = the_list

            if isinstance(the_list, type(self)):
                super().__init__(the_list.data)
            else:
                super().__init__([(x) for x in the_list])

        def Append(self, new_value):
            self.data.append((new_value))
            return self

        def Serializable(self):
            return self.data

    class VehiclesProperty (UserList):
        """ This represents a JSON array.
        """
        
        def __init__(self, the_list=None):
            """Initializer for array.
            """
            self.the_list = the_list

            if isinstance(the_list, type(self)):
                super().__init__(the_list.data)
            else:
                super().__init__([(x) for x in the_list])

        def Append(self, new_value):
            self.data.append((new_value))
            return self

        def Serializable(self):
            return self.data

    class UrlProperty(object):
        """ This class is a schema-validating wrapper around a string.
        """

        def __init__(self, value):
            self.Set(value)

        @staticmethod
        def _Validate(value):
            if not isinstance(value, str):
                raise ValueError("Passed value was not a string")        

        def Set(self, new_value):
            if isinstance(new_value, type(self)):
                self._value = new_value._value
            else:
                self._Validate(new_value)
                self._value = new_value
            return self

        def Get(self) -> str:
            return self._value

        def Serializable(self):
            return self.Get()

    class CharactersProperty (UserList):
        """ This represents a JSON array.
        """
        
        def __init__(self, the_list=None):
            """Initializer for array.
            """
            self.the_list = the_list

            if isinstance(the_list, type(self)):
                super().__init__(the_list.data)
            else:
                super().__init__([(x) for x in the_list])

        def Append(self, new_value):
            self.data.append((new_value))
            return self

        def Serializable(self):
            return self.data


    def __init__(self, data=None, **kwargs):
        """Initialization for the Film object.
        It can be initialized with an object, or by passing each
        object property as a keyword argument.
        """
        new_data = {}
        try:
            prop = data["starships"] if ("starships" in data) else kwargs["starships"]
            if not isinstance(prop, self.StarshipsProperty):
                new_data["starships"] = self.StarshipsProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'starships'")
        try:
            prop = data["species"] if ("species" in data) else kwargs["species"]
            if not isinstance(prop, self.SpeciesProperty):
                new_data["species"] = self.SpeciesProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'species'")
        try:
            prop = data["episode_id"] if ("episode_id" in data) else kwargs["episode_id"]
            if not isinstance(prop, self.EpisodeIdProperty):
                new_data["episode_id"] = self.EpisodeIdProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'episode_id'")
        try:
            prop = data["producer"] if ("producer" in data) else kwargs["producer"]
            if not isinstance(prop, self.ProducerProperty):
                new_data["producer"] = self.ProducerProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'producer'")
        try:
            prop = data["edited"] if ("edited" in data) else kwargs["edited"]
            if not isinstance(prop, self.EditedProperty):
                new_data["edited"] = self.EditedProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'edited'")
        try:
            prop = data["created"] if ("created" in data) else kwargs["created"]
            if not isinstance(prop, self.CreatedProperty):
                new_data["created"] = self.CreatedProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'created'")
        try:
            prop = data["opening_crawl"] if ("opening_crawl" in data) else kwargs["opening_crawl"]
            if not isinstance(prop, self.OpeningCrawlProperty):
                new_data["opening_crawl"] = self.OpeningCrawlProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'opening_crawl'")
        try:
            prop = data["director"] if ("director" in data) else kwargs["director"]
            if not isinstance(prop, self.DirectorProperty):
                new_data["director"] = self.DirectorProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'director'")
        try:
            prop = data["release_date"] if ("release_date" in data) else kwargs["release_date"]
            if not isinstance(prop, self.ReleaseDateProperty):
                new_data["release_date"] = self.ReleaseDateProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'release_date'")
        try:
            prop = data["title"] if ("title" in data) else kwargs["title"]
            if not isinstance(prop, self.TitleProperty):
                new_data["title"] = self.TitleProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'title'")
        try:
            prop = data["planets"] if ("planets" in data) else kwargs["planets"]
            if not isinstance(prop, self.PlanetsProperty):
                new_data["planets"] = self.PlanetsProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'planets'")
        try:
            prop = data["vehicles"] if ("vehicles" in data) else kwargs["vehicles"]
            if not isinstance(prop, self.VehiclesProperty):
                new_data["vehicles"] = self.VehiclesProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'vehicles'")
        try:
            prop = data["url"] if ("url" in data) else kwargs["url"]
            if not isinstance(prop, self.UrlProperty):
                new_data["url"] = self.UrlProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'url'")
        try:
            prop = data["characters"] if ("characters" in data) else kwargs["characters"]
            if not isinstance(prop, self.CharactersProperty):
                new_data["characters"] = self.CharactersProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'characters'")
        super().__init__(new_data)

    def GetStarships(self):
        return self.data["starships"]
    
    def SetStarships(self, new_value):
        if not isinstance(new_value, self.StarshipsProperty):
            self.data["starships"] = self.StarshipsProperty(new_value)
        else:
            self.data["starships"] = new_value
        return self

    def GetSpecies(self):
        return self.data["species"]
    
    def SetSpecies(self, new_value):
        if not isinstance(new_value, self.SpeciesProperty):
            self.data["species"] = self.SpeciesProperty(new_value)
        else:
            self.data["species"] = new_value
        return self

    def GetEpisodeId(self):
        return self.data["episode_id"]
    
    def SetEpisodeId(self, new_value):
        if not isinstance(new_value, self.EpisodeIdProperty):
            self.data["episode_id"] = self.EpisodeIdProperty(new_value)
        else:
            self.data["episode_id"] = new_value
        return self

    def GetProducer(self):
        return self.data["producer"]
    
    def SetProducer(self, new_value):
        if not isinstance(new_value, self.ProducerProperty):
            self.data["producer"] = self.ProducerProperty(new_value)
        else:
            self.data["producer"] = new_value
        return self

    def GetEdited(self):
        return self.data["edited"]
    
    def SetEdited(self, new_value):
        if not isinstance(new_value, self.EditedProperty):
            self.data["edited"] = self.EditedProperty(new_value)
        else:
            self.data["edited"] = new_value
        return self

    def GetCreated(self):
        return self.data["created"]
    
    def SetCreated(self, new_value):
        if not isinstance(new_value, self.CreatedProperty):
            self.data["created"] = self.CreatedProperty(new_value)
        else:
            self.data["created"] = new_value
        return self

    def GetOpeningCrawl(self):
        return self.data["opening_crawl"]
    
    def SetOpeningCrawl(self, new_value):
        if not isinstance(new_value, self.OpeningCrawlProperty):
            self.data["opening_crawl"] = self.OpeningCrawlProperty(new_value)
        else:
            self.data["opening_crawl"] = new_value
        return self

    def GetDirector(self):
        return self.data["director"]
    
    def SetDirector(self, new_value):
        if not isinstance(new_value, self.DirectorProperty):
            self.data["director"] = self.DirectorProperty(new_value)
        else:
            self.data["director"] = new_value
        return self

    def GetReleaseDate(self):
        return self.data["release_date"]
    
    def SetReleaseDate(self, new_value):
        if not isinstance(new_value, self.ReleaseDateProperty):
            self.data["release_date"] = self.ReleaseDateProperty(new_value)
        else:
            self.data["release_date"] = new_value
        return self

    def GetTitle(self):
        return self.data["title"]
    
    def SetTitle(self, new_value):
        if not isinstance(new_value, self.TitleProperty):
            self.data["title"] = self.TitleProperty(new_value)
        else:
            self.data["title"] = new_value
        return self

    def GetPlanets(self):
        return self.data["planets"]
    
    def SetPlanets(self, new_value):
        if not isinstance(new_value, self.PlanetsProperty):
            self.data["planets"] = self.PlanetsProperty(new_value)
        else:
            self.data["planets"] = new_value
        return self

    def GetVehicles(self):
        return self.data["vehicles"]
    
    def SetVehicles(self, new_value):
        if not isinstance(new_value, self.VehiclesProperty):
            self.data["vehicles"] = self.VehiclesProperty(new_value)
        else:
            self.data["vehicles"] = new_value
        return self

    def GetUrl(self):
        return self.data["url"]
    
    def SetUrl(self, new_value):
        if not isinstance(new_value, self.UrlProperty):
            self.data["url"] = self.UrlProperty(new_value)
        else:
            self.data["url"] = new_value
        return self

    def GetCharacters(self):
        return self.data["characters"]
    
    def SetCharacters(self, new_value):
        if not isinstance(new_value, self.CharactersProperty):
            self.data["characters"] = self.CharactersProperty(new_value)
        else:
            self.data["characters"] = new_value
        return self

    def Serializable(self):
        return self.data