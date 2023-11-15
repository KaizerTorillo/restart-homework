from .Cars import Cars

class ElectricCar(Cars): #subclass
    def __init__(self, brand, mileage_km, range):      #putting pass here wills allow non-defined function/class
        super().__init__(brand, mileage_km)             #no need to put self as attribute in (brand, mileage_km) as super() is already doing that.
        self.range = range                             #Ideally, you would use super() to show that you are calling the same class. Using the name of a clas usually means that it is another class.

