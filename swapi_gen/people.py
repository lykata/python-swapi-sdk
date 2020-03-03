from collections import UserDict
from collections import UserList

class People(UserDict):
    """This represents a JSON object.
    """
    class EyeColorProperty(object):
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

    class HeightProperty(object):
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

    class GenderProperty(object):
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

    class MassProperty(object):
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

    class HairColorProperty(object):
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

    class SkinColorProperty(object):
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

    class NameProperty(object):
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

    class BirthYearProperty(object):
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

    class HomeworldProperty(object):
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

    class FilmsProperty (UserList):
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
        """Initialization for the People object.
        It can be initialized with an object, or by passing each
        object property as a keyword argument.
        """
        new_data = {}
        try:
            prop = data["eye_color"] if ("eye_color" in data) else kwargs["eye_color"]
            if not isinstance(prop, self.EyeColorProperty):
                new_data["eye_color"] = self.EyeColorProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'eye_color'")
        try:
            prop = data["height"] if ("height" in data) else kwargs["height"]
            if not isinstance(prop, self.HeightProperty):
                new_data["height"] = self.HeightProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'height'")
        try:
            prop = data["starships"] if ("starships" in data) else kwargs["starships"]
            if not isinstance(prop, self.StarshipsProperty):
                new_data["starships"] = self.StarshipsProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'starships'")
        try:
            prop = data["gender"] if ("gender" in data) else kwargs["gender"]
            if not isinstance(prop, self.GenderProperty):
                new_data["gender"] = self.GenderProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'gender'")
        try:
            prop = data["vehicles"] if ("vehicles" in data) else kwargs["vehicles"]
            if not isinstance(prop, self.VehiclesProperty):
                new_data["vehicles"] = self.VehiclesProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'vehicles'")
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
            prop = data["mass"] if ("mass" in data) else kwargs["mass"]
            if not isinstance(prop, self.MassProperty):
                new_data["mass"] = self.MassProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'mass'")
        try:
            prop = data["hair_color"] if ("hair_color" in data) else kwargs["hair_color"]
            if not isinstance(prop, self.HairColorProperty):
                new_data["hair_color"] = self.HairColorProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'hair_color'")
        try:
            prop = data["skin_color"] if ("skin_color" in data) else kwargs["skin_color"]
            if not isinstance(prop, self.SkinColorProperty):
                new_data["skin_color"] = self.SkinColorProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'skin_color'")
        try:
            prop = data["name"] if ("name" in data) else kwargs["name"]
            if not isinstance(prop, self.NameProperty):
                new_data["name"] = self.NameProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'name'")
        try:
            prop = data["species"] if ("species" in data) else kwargs["species"]
            if not isinstance(prop, self.SpeciesProperty):
                new_data["species"] = self.SpeciesProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'species'")
        try:
            prop = data["birth_year"] if ("birth_year" in data) else kwargs["birth_year"]
            if not isinstance(prop, self.BirthYearProperty):
                new_data["birth_year"] = self.BirthYearProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'birth_year'")
        try:
            prop = data["url"] if ("url" in data) else kwargs["url"]
            if not isinstance(prop, self.UrlProperty):
                new_data["url"] = self.UrlProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'url'")
        try:
            prop = data["homeworld"] if ("homeworld" in data) else kwargs["homeworld"]
            if not isinstance(prop, self.HomeworldProperty):
                new_data["homeworld"] = self.HomeworldProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'homeworld'")
        try:
            prop = data["films"] if ("films" in data) else kwargs["films"]
            if not isinstance(prop, self.FilmsProperty):
                new_data["films"] = self.FilmsProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'films'")
        super().__init__(new_data)

    def GetEyeColor(self):
        return self.data["eye_color"]
    
    def SetEyeColor(self, new_value):
        if not isinstance(new_value, self.EyeColorProperty):
            self.data["eye_color"] = self.EyeColorProperty(new_value)
        else:
            self.data["eye_color"] = new_value
        return self

    def GetHeight(self):
        return self.data["height"]
    
    def SetHeight(self, new_value):
        if not isinstance(new_value, self.HeightProperty):
            self.data["height"] = self.HeightProperty(new_value)
        else:
            self.data["height"] = new_value
        return self

    def GetStarships(self):
        return self.data["starships"]
    
    def SetStarships(self, new_value):
        if not isinstance(new_value, self.StarshipsProperty):
            self.data["starships"] = self.StarshipsProperty(new_value)
        else:
            self.data["starships"] = new_value
        return self

    def GetGender(self):
        return self.data["gender"]
    
    def SetGender(self, new_value):
        if not isinstance(new_value, self.GenderProperty):
            self.data["gender"] = self.GenderProperty(new_value)
        else:
            self.data["gender"] = new_value
        return self

    def GetVehicles(self):
        return self.data["vehicles"]
    
    def SetVehicles(self, new_value):
        if not isinstance(new_value, self.VehiclesProperty):
            self.data["vehicles"] = self.VehiclesProperty(new_value)
        else:
            self.data["vehicles"] = new_value
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

    def GetMass(self):
        return self.data["mass"]
    
    def SetMass(self, new_value):
        if not isinstance(new_value, self.MassProperty):
            self.data["mass"] = self.MassProperty(new_value)
        else:
            self.data["mass"] = new_value
        return self

    def GetHairColor(self):
        return self.data["hair_color"]
    
    def SetHairColor(self, new_value):
        if not isinstance(new_value, self.HairColorProperty):
            self.data["hair_color"] = self.HairColorProperty(new_value)
        else:
            self.data["hair_color"] = new_value
        return self

    def GetSkinColor(self):
        return self.data["skin_color"]
    
    def SetSkinColor(self, new_value):
        if not isinstance(new_value, self.SkinColorProperty):
            self.data["skin_color"] = self.SkinColorProperty(new_value)
        else:
            self.data["skin_color"] = new_value
        return self

    def GetName(self):
        return self.data["name"]
    
    def SetName(self, new_value):
        if not isinstance(new_value, self.NameProperty):
            self.data["name"] = self.NameProperty(new_value)
        else:
            self.data["name"] = new_value
        return self

    def GetSpecies(self):
        return self.data["species"]
    
    def SetSpecies(self, new_value):
        if not isinstance(new_value, self.SpeciesProperty):
            self.data["species"] = self.SpeciesProperty(new_value)
        else:
            self.data["species"] = new_value
        return self

    def GetBirthYear(self):
        return self.data["birth_year"]
    
    def SetBirthYear(self, new_value):
        if not isinstance(new_value, self.BirthYearProperty):
            self.data["birth_year"] = self.BirthYearProperty(new_value)
        else:
            self.data["birth_year"] = new_value
        return self

    def GetUrl(self):
        return self.data["url"]
    
    def SetUrl(self, new_value):
        if not isinstance(new_value, self.UrlProperty):
            self.data["url"] = self.UrlProperty(new_value)
        else:
            self.data["url"] = new_value
        return self

    def GetHomeworld(self):
        return self.data["homeworld"]
    
    def SetHomeworld(self, new_value):
        if not isinstance(new_value, self.HomeworldProperty):
            self.data["homeworld"] = self.HomeworldProperty(new_value)
        else:
            self.data["homeworld"] = new_value
        return self

    def GetFilms(self):
        return self.data["films"]
    
    def SetFilms(self, new_value):
        if not isinstance(new_value, self.FilmsProperty):
            self.data["films"] = self.FilmsProperty(new_value)
        else:
            self.data["films"] = new_value
        return self

    def Serializable(self):
        return self.data