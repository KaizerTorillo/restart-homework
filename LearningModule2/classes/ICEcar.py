from .Cars import Cars

class ICEcar(Cars):
    def __init__(self, brand, mileage_km, fuel_consumption, fuel_level):
        Cars.__init__(self, brand, mileage_km)
        self.fuel_consumption = fuel_consumption
        self.fuel_level = fuel_level