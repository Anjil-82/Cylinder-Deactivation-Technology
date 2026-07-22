class fuelData :
    data={
        "Gasoline": {

            "LHV": 43e6,
            "AFR": 14.7,
            "Density": 740,
            "Cp": 2200,
            "Cv": 1710,
            "Octane": 95

           },

         "Diesel": {

            "LHV": 42.5e6,
            "AFR": 14.5,
            "Density": 832,
            "Cp": 2100,
            "Cv": 1650,
            "Cetane": 50

               },
            }
    @classmethod
    def fuels(cls):
        return list(cls.data.keys())
    
    @classmethod
    def get_fuel_data(cls,fuel_name:str):
        if(fuel_name not in cls.data):
            raise ValueError (f"{fuel_name} not present in the database")

        return cls.data[fuel_name]

    