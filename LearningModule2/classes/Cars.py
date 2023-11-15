class Cars:
    def __init__(self, brand, mileage_km):
        self.brand = brand
        self.mileage_km = mileage_km
        
    def driving(self, distance):
        self.mileage_km = self.mileage_km + distance    #Please note that self-mileage_km was used here as mileage_km is undefined under this funciton. 
