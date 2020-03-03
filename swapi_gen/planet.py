from collections import UserDict
from collections import UserList

class Planet(UserDict):
    """This represents a JSON object.
    """
    class DiameterProperty(object):
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

    class RotationPeriodProperty(object):
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

    class OrbitalPeriodProperty(object):
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

    class TerrainProperty(object):
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

    class GravityProperty(object):
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

    class SurfaceWaterProperty(object):
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

    class ResidentsProperty (UserList):
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

    class ClimateProperty(object):
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

    class PopulationProperty(object):
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
        """Initialization for the Planet object.
        It can be initialized with an object, or by passing each
        object property as a keyword argument.
        """
        new_data = {}
        try:
            prop = data["diameter"] if ("diameter" in data) else kwargs["diameter"]
            if not isinstance(prop, self.DiameterProperty):
                new_data["diameter"] = self.DiameterProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'diameter'")
        try:
            prop = data["rotation_period"] if ("rotation_period" in data) else kwargs["rotation_period"]
            if not isinstance(prop, self.RotationPeriodProperty):
                new_data["rotation_period"] = self.RotationPeriodProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'rotation_period'")
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
            prop = data["orbital_period"] if ("orbital_period" in data) else kwargs["orbital_period"]
            if not isinstance(prop, self.OrbitalPeriodProperty):
                new_data["orbital_period"] = self.OrbitalPeriodProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'orbital_period'")
        try:
            prop = data["terrain"] if ("terrain" in data) else kwargs["terrain"]
            if not isinstance(prop, self.TerrainProperty):
                new_data["terrain"] = self.TerrainProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'terrain'")
        try:
            prop = data["gravity"] if ("gravity" in data) else kwargs["gravity"]
            if not isinstance(prop, self.GravityProperty):
                new_data["gravity"] = self.GravityProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'gravity'")
        try:
            prop = data["surface_water"] if ("surface_water" in data) else kwargs["surface_water"]
            if not isinstance(prop, self.SurfaceWaterProperty):
                new_data["surface_water"] = self.SurfaceWaterProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'surface_water'")
        try:
            prop = data["name"] if ("name" in data) else kwargs["name"]
            if not isinstance(prop, self.NameProperty):
                new_data["name"] = self.NameProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'name'")
        try:
            prop = data["residents"] if ("residents" in data) else kwargs["residents"]
            if not isinstance(prop, self.ResidentsProperty):
                new_data["residents"] = self.ResidentsProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'residents'")
        try:
            prop = data["climate"] if ("climate" in data) else kwargs["climate"]
            if not isinstance(prop, self.ClimateProperty):
                new_data["climate"] = self.ClimateProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'climate'")
        try:
            prop = data["url"] if ("url" in data) else kwargs["url"]
            if not isinstance(prop, self.UrlProperty):
                new_data["url"] = self.UrlProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'url'")
        try:
            prop = data["population"] if ("population" in data) else kwargs["population"]
            if not isinstance(prop, self.PopulationProperty):
                new_data["population"] = self.PopulationProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'population'")
        try:
            prop = data["films"] if ("films" in data) else kwargs["films"]
            if not isinstance(prop, self.FilmsProperty):
                new_data["films"] = self.FilmsProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'films'")
        super().__init__(new_data)

    def GetDiameter(self):
        return self.data["diameter"]
    
    def SetDiameter(self, new_value):
        if not isinstance(new_value, self.DiameterProperty):
            self.data["diameter"] = self.DiameterProperty(new_value)
        else:
            self.data["diameter"] = new_value
        return self

    def GetRotationPeriod(self):
        return self.data["rotation_period"]
    
    def SetRotationPeriod(self, new_value):
        if not isinstance(new_value, self.RotationPeriodProperty):
            self.data["rotation_period"] = self.RotationPeriodProperty(new_value)
        else:
            self.data["rotation_period"] = new_value
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

    def GetOrbitalPeriod(self):
        return self.data["orbital_period"]
    
    def SetOrbitalPeriod(self, new_value):
        if not isinstance(new_value, self.OrbitalPeriodProperty):
            self.data["orbital_period"] = self.OrbitalPeriodProperty(new_value)
        else:
            self.data["orbital_period"] = new_value
        return self

    def GetTerrain(self):
        return self.data["terrain"]
    
    def SetTerrain(self, new_value):
        if not isinstance(new_value, self.TerrainProperty):
            self.data["terrain"] = self.TerrainProperty(new_value)
        else:
            self.data["terrain"] = new_value
        return self

    def GetGravity(self):
        return self.data["gravity"]
    
    def SetGravity(self, new_value):
        if not isinstance(new_value, self.GravityProperty):
            self.data["gravity"] = self.GravityProperty(new_value)
        else:
            self.data["gravity"] = new_value
        return self

    def GetSurfaceWater(self):
        return self.data["surface_water"]
    
    def SetSurfaceWater(self, new_value):
        if not isinstance(new_value, self.SurfaceWaterProperty):
            self.data["surface_water"] = self.SurfaceWaterProperty(new_value)
        else:
            self.data["surface_water"] = new_value
        return self

    def GetName(self):
        return self.data["name"]
    
    def SetName(self, new_value):
        if not isinstance(new_value, self.NameProperty):
            self.data["name"] = self.NameProperty(new_value)
        else:
            self.data["name"] = new_value
        return self

    def GetResidents(self):
        return self.data["residents"]
    
    def SetResidents(self, new_value):
        if not isinstance(new_value, self.ResidentsProperty):
            self.data["residents"] = self.ResidentsProperty(new_value)
        else:
            self.data["residents"] = new_value
        return self

    def GetClimate(self):
        return self.data["climate"]
    
    def SetClimate(self, new_value):
        if not isinstance(new_value, self.ClimateProperty):
            self.data["climate"] = self.ClimateProperty(new_value)
        else:
            self.data["climate"] = new_value
        return self

    def GetUrl(self):
        return self.data["url"]
    
    def SetUrl(self, new_value):
        if not isinstance(new_value, self.UrlProperty):
            self.data["url"] = self.UrlProperty(new_value)
        else:
            self.data["url"] = new_value
        return self

    def GetPopulation(self):
        return self.data["population"]
    
    def SetPopulation(self, new_value):
        if not isinstance(new_value, self.PopulationProperty):
            self.data["population"] = self.PopulationProperty(new_value)
        else:
            self.data["population"] = new_value
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