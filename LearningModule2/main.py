from classes import ICEcar, ElectricCar, Cars

def main():
    
    my_car = Cars(brand = "Toyota", mileage_km = 40000)

    my_car.driving(distance = 1000) 

    print(my_car.__dict__)
    print(my_car)
    
    my_ev = ElectricCar("BMW", 2500, 500)
    my_ev.driving(distance = 300)

    #my_ice = ICEcar(brand = "Honda", mileage_km=5000)
    my_ice = ICEcar("Honda", 1300, 7, 50)
    my_ice.driving(distance = 600)

    print(my_ev.__dict__)
    print(my_ev)

    print(my_ice.__dict__)
    print(my_ice)
    
if __name__ == "__main__":
    main()
    
#Errors in this code, when calling main, gives line 5 error module obkect is not callable