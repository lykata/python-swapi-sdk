from collections import UserDict
from collections import UserList

class Vehicle(UserDict):
    """This represents a JSON object.
    """
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

    class MaxAtmospheringSpeedProperty(object):
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

    class CostInCreditsProperty(object):
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

    class VehicleClassProperty(object):
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

    class CargoCapacityProperty(object):
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

    class ModelProperty(object):
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

    class CrewProperty(object):
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

    class ConsumablesProperty(object):
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

    class LengthProperty(object):
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

    class PilotsProperty (UserList):
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

    class PassengersProperty(object):
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

    class ManufacturerProperty(object):
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
        """Initialization for the Vehicle object.
        It can be initialized with an object, or by passing each
        object property as a keyword argument.
        """
        new_data = {}
        try:
            prop = data["edited"] if ("edited" in data) else kwargs["edited"]
            if not isinstance(prop, self.EditedProperty):
                new_data["edited"] = self.EditedProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'edited'")
        try:
            prop = data["max_atmosphering_speed"] if ("max_atmosphering_speed" in data) else kwargs["max_atmosphering_speed"]
            if not isinstance(prop, self.MaxAtmospheringSpeedProperty):
                new_data["max_atmosphering_speed"] = self.MaxAtmospheringSpeedProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'max_atmosphering_speed'")
        try:
            prop = data["cost_in_credits"] if ("cost_in_credits" in data) else kwargs["cost_in_credits"]
            if not isinstance(prop, self.CostInCreditsProperty):
                new_data["cost_in_credits"] = self.CostInCreditsProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'cost_in_credits'")
        try:
            prop = data["vehicle_class"] if ("vehicle_class" in data) else kwargs["vehicle_class"]
            if not isinstance(prop, self.VehicleClassProperty):
                new_data["vehicle_class"] = self.VehicleClassProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'vehicle_class'")
        try:
            prop = data["cargo_capacity"] if ("cargo_capacity" in data) else kwargs["cargo_capacity"]
            if not isinstance(prop, self.CargoCapacityProperty):
                new_data["cargo_capacity"] = self.CargoCapacityProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'cargo_capacity'")
        try:
            prop = data["model"] if ("model" in data) else kwargs["model"]
            if not isinstance(prop, self.ModelProperty):
                new_data["model"] = self.ModelProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'model'")
        try:
            prop = data["created"] if ("created" in data) else kwargs["created"]
            if not isinstance(prop, self.CreatedProperty):
                new_data["created"] = self.CreatedProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'created'")
        try:
            prop = data["crew"] if ("crew" in data) else kwargs["crew"]
            if not isinstance(prop, self.CrewProperty):
                new_data["crew"] = self.CrewProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'crew'")
        try:
            prop = data["consumables"] if ("consumables" in data) else kwargs["consumables"]
            if not isinstance(prop, self.ConsumablesProperty):
                new_data["consumables"] = self.ConsumablesProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'consumables'")
        try:
            prop = data["length"] if ("length" in data) else kwargs["length"]
            if not isinstance(prop, self.LengthProperty):
                new_data["length"] = self.LengthProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'length'")
        try:
            prop = data["name"] if ("name" in data) else kwargs["name"]
            if not isinstance(prop, self.NameProperty):
                new_data["name"] = self.NameProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'name'")
        try:
            prop = data["pilots"] if ("pilots" in data) else kwargs["pilots"]
            if not isinstance(prop, self.PilotsProperty):
                new_data["pilots"] = self.PilotsProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'pilots'")
        try:
            prop = data["passengers"] if ("passengers" in data) else kwargs["passengers"]
            if not isinstance(prop, self.PassengersProperty):
                new_data["passengers"] = self.PassengersProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'passengers'")
        try:
            prop = data["url"] if ("url" in data) else kwargs["url"]
            if not isinstance(prop, self.UrlProperty):
                new_data["url"] = self.UrlProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'url'")
        try:
            prop = data["manufacturer"] if ("manufacturer" in data) else kwargs["manufacturer"]
            if not isinstance(prop, self.ManufacturerProperty):
                new_data["manufacturer"] = self.ManufacturerProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'manufacturer'")
        try:
            prop = data["films"] if ("films" in data) else kwargs["films"]
            if not isinstance(prop, self.FilmsProperty):
                new_data["films"] = self.FilmsProperty(prop)
        except KeyError:
            raise ValueError("Missing property 'films'")
        super().__init__(new_data)

    def GetEdited(self):
        return self.data["edited"]
    
    def SetEdited(self, new_value):
        if not isinstance(new_value, self.EditedProperty):
            self.data["edited"] = self.EditedProperty(new_value)
        else:
            self.data["edited"] = new_value
        return self

    def GetMaxAtmospheringSpeed(self):
        return self.data["max_atmosphering_speed"]
    
    def SetMaxAtmospheringSpeed(self, new_value):
        if not isinstance(new_value, self.MaxAtmospheringSpeedProperty):
            self.data["max_atmosphering_speed"] = self.MaxAtmospheringSpeedProperty(new_value)
        else:
            self.data["max_atmosphering_speed"] = new_value
        return self

    def GetCostInCredits(self):
        return self.data["cost_in_credits"]
    
    def SetCostInCredits(self, new_value):
        if not isinstance(new_value, self.CostInCreditsProperty):
            self.data["cost_in_credits"] = self.CostInCreditsProperty(new_value)
        else:
            self.data["cost_in_credits"] = new_value
        return self

    def GetVehicleClass(self):
        return self.data["vehicle_class"]
    
    def SetVehicleClass(self, new_value):
        if not isinstance(new_value, self.VehicleClassProperty):
            self.data["vehicle_class"] = self.VehicleClassProperty(new_value)
        else:
            self.data["vehicle_class"] = new_value
        return self

    def GetCargoCapacity(self):
        return self.data["cargo_capacity"]
    
    def SetCargoCapacity(self, new_value):
        if not isinstance(new_value, self.CargoCapacityProperty):
            self.data["cargo_capacity"] = self.CargoCapacityProperty(new_value)
        else:
            self.data["cargo_capacity"] = new_value
        return self

    def GetModel(self):
        return self.data["model"]
    
    def SetModel(self, new_value):
        if not isinstance(new_value, self.ModelProperty):
            self.data["model"] = self.ModelProperty(new_value)
        else:
            self.data["model"] = new_value
        return self

    def GetCreated(self):
        return self.data["created"]
    
    def SetCreated(self, new_value):
        if not isinstance(new_value, self.CreatedProperty):
            self.data["created"] = self.CreatedProperty(new_value)
        else:
            self.data["created"] = new_value
        return self

    def GetCrew(self):
        return self.data["crew"]
    
    def SetCrew(self, new_value):
        if not isinstance(new_value, self.CrewProperty):
            self.data["crew"] = self.CrewProperty(new_value)
        else:
            self.data["crew"] = new_value
        return self

    def GetConsumables(self):
        return self.data["consumables"]
    
    def SetConsumables(self, new_value):
        if not isinstance(new_value, self.ConsumablesProperty):
            self.data["consumables"] = self.ConsumablesProperty(new_value)
        else:
            self.data["consumables"] = new_value
        return self

    def GetLength(self):
        return self.data["length"]
    
    def SetLength(self, new_value):
        if not isinstance(new_value, self.LengthProperty):
            self.data["length"] = self.LengthProperty(new_value)
        else:
            self.data["length"] = new_value
        return self

    def GetName(self):
        return self.data["name"]
    
    def SetName(self, new_value):
        if not isinstance(new_value, self.NameProperty):
            self.data["name"] = self.NameProperty(new_value)
        else:
            self.data["name"] = new_value
        return self

    def GetPilots(self):
        return self.data["pilots"]
    
    def SetPilots(self, new_value):
        if not isinstance(new_value, self.PilotsProperty):
            self.data["pilots"] = self.PilotsProperty(new_value)
        else:
            self.data["pilots"] = new_value
        return self

    def GetPassengers(self):
        return self.data["passengers"]
    
    def SetPassengers(self, new_value):
        if not isinstance(new_value, self.PassengersProperty):
            self.data["passengers"] = self.PassengersProperty(new_value)
        else:
            self.data["passengers"] = new_value
        return self

    def GetUrl(self):
        return self.data["url"]
    
    def SetUrl(self, new_value):
        if not isinstance(new_value, self.UrlProperty):
            self.data["url"] = self.UrlProperty(new_value)
        else:
            self.data["url"] = new_value
        return self

    def GetManufacturer(self):
        return self.data["manufacturer"]
    
    def SetManufacturer(self, new_value):
        if not isinstance(new_value, self.ManufacturerProperty):
            self.data["manufacturer"] = self.ManufacturerProperty(new_value)
        else:
            self.data["manufacturer"] = new_value
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