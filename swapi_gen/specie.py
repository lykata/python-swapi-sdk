from collections import UserDict
from collections import UserList

class Specie(UserDict):
    """This represents a JSON object.
    """
    class EyeColorsProperty(object):
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

    class ClassificationProperty(object):
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

    class AverageLifespanProperty(object):
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

    class PeopleProperty (UserList):
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

    class HairColorsProperty(object):
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

    class SkinColorsProperty(object):
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

    class LanguageProperty(object):
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

    class DesignationProperty(object):
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

    class AverageHeightProperty(object):
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
        """Initialization for the Specie object.
        It can be initialized with an object, or by passing each
        object property as a keyword argument.
        """
        new_data = {}
        try:
            prop = data["eye_colors"] if ("eye_colors" in data) else kwargs["eye_colors"]
            if not isinstance(prop, self.EyeColorsProperty):
                new_data["eye_colors"] = self.EyeColorsProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'eye_colors'")
        try:
            prop = data["classification"] if ("classification" in data) else kwargs["classification"]
            if not isinstance(prop, self.ClassificationProperty):
                new_data["classification"] = self.ClassificationProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'classification'")
        try:
            prop = data["edited"] if ("edited" in data) else kwargs["edited"]
            if not isinstance(prop, self.EditedProperty):
                new_data["edited"] = self.EditedProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'edited'")
        try:
            prop = data["average_lifespan"] if ("average_lifespan" in data) else kwargs["average_lifespan"]
            if not isinstance(prop, self.AverageLifespanProperty):
                new_data["average_lifespan"] = self.AverageLifespanProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'average_lifespan'")
        try:
            prop = data["created"] if ("created" in data) else kwargs["created"]
            if not isinstance(prop, self.CreatedProperty):
                new_data["created"] = self.CreatedProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'created'")
        try:
            prop = data["people"] if ("people" in data) else kwargs["people"]
            if not isinstance(prop, self.PeopleProperty):
                new_data["people"] = self.PeopleProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'people'")
        try:
            prop = data["hair_colors"] if ("hair_colors" in data) else kwargs["hair_colors"]
            if not isinstance(prop, self.HairColorsProperty):
                new_data["hair_colors"] = self.HairColorsProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'hair_colors'")
        try:
            prop = data["skin_colors"] if ("skin_colors" in data) else kwargs["skin_colors"]
            if not isinstance(prop, self.SkinColorsProperty):
                new_data["skin_colors"] = self.SkinColorsProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'skin_colors'")
        try:
            prop = data["language"] if ("language" in data) else kwargs["language"]
            if not isinstance(prop, self.LanguageProperty):
                new_data["language"] = self.LanguageProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'language'")
        try:
            prop = data["name"] if ("name" in data) else kwargs["name"]
            if not isinstance(prop, self.NameProperty):
                new_data["name"] = self.NameProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'name'")
        try:
            prop = data["designation"] if ("designation" in data) else kwargs["designation"]
            if not isinstance(prop, self.DesignationProperty):
                new_data["designation"] = self.DesignationProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'designation'")
        try:
            prop = data["average_height"] if ("average_height" in data) else kwargs["average_height"]
            if not isinstance(prop, self.AverageHeightProperty):
                new_data["average_height"] = self.AverageHeightProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'average_height'")
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

    def GetEyeColors(self):
        return self.data["eye_colors"]
    
    def SetEyeColors(self, new_value):
        if not isinstance(new_value, self.EyeColorsProperty):
            self.data["eye_colors"] = self.EyeColorsProperty(new_value)
        else:
            self.data["eye_colors"] = new_value
        return self

    def GetClassification(self):
        return self.data["classification"]
    
    def SetClassification(self, new_value):
        if not isinstance(new_value, self.ClassificationProperty):
            self.data["classification"] = self.ClassificationProperty(new_value)
        else:
            self.data["classification"] = new_value
        return self

    def GetEdited(self):
        return self.data["edited"]
    
    def SetEdited(self, new_value):
        if not isinstance(new_value, self.EditedProperty):
            self.data["edited"] = self.EditedProperty(new_value)
        else:
            self.data["edited"] = new_value
        return self

    def GetAverageLifespan(self):
        return self.data["average_lifespan"]
    
    def SetAverageLifespan(self, new_value):
        if not isinstance(new_value, self.AverageLifespanProperty):
            self.data["average_lifespan"] = self.AverageLifespanProperty(new_value)
        else:
            self.data["average_lifespan"] = new_value
        return self

    def GetCreated(self):
        return self.data["created"]
    
    def SetCreated(self, new_value):
        if not isinstance(new_value, self.CreatedProperty):
            self.data["created"] = self.CreatedProperty(new_value)
        else:
            self.data["created"] = new_value
        return self

    def GetPeople(self):
        return self.data["people"]
    
    def SetPeople(self, new_value):
        if not isinstance(new_value, self.PeopleProperty):
            self.data["people"] = self.PeopleProperty(new_value)
        else:
            self.data["people"] = new_value
        return self

    def GetHairColors(self):
        return self.data["hair_colors"]
    
    def SetHairColors(self, new_value):
        if not isinstance(new_value, self.HairColorsProperty):
            self.data["hair_colors"] = self.HairColorsProperty(new_value)
        else:
            self.data["hair_colors"] = new_value
        return self

    def GetSkinColors(self):
        return self.data["skin_colors"]
    
    def SetSkinColors(self, new_value):
        if not isinstance(new_value, self.SkinColorsProperty):
            self.data["skin_colors"] = self.SkinColorsProperty(new_value)
        else:
            self.data["skin_colors"] = new_value
        return self

    def GetLanguage(self):
        return self.data["language"]
    
    def SetLanguage(self, new_value):
        if not isinstance(new_value, self.LanguageProperty):
            self.data["language"] = self.LanguageProperty(new_value)
        else:
            self.data["language"] = new_value
        return self

    def GetName(self):
        return self.data["name"]
    
    def SetName(self, new_value):
        if not isinstance(new_value, self.NameProperty):
            self.data["name"] = self.NameProperty(new_value)
        else:
            self.data["name"] = new_value
        return self

    def GetDesignation(self):
        return self.data["designation"]
    
    def SetDesignation(self, new_value):
        if not isinstance(new_value, self.DesignationProperty):
            self.data["designation"] = self.DesignationProperty(new_value)
        else:
            self.data["designation"] = new_value
        return self

    def GetAverageHeight(self):
        return self.data["average_height"]
    
    def SetAverageHeight(self, new_value):
        if not isinstance(new_value, self.AverageHeightProperty):
            self.data["average_height"] = self.AverageHeightProperty(new_value)
        else:
            self.data["average_height"] = new_value
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