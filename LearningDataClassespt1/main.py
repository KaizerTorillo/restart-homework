from dataclasses import dataclass

@dataclass
class ItemOrigin:
    country: str
    production_date: str
    

@dataclass
class InventoryItem:  #When defining data classes, also need to define type of data property in each data class. 
    name: str
    quantity: int
    serial_num: str
    origin: ItemOrigin

def main():
    item_origin = ItemOrigin(country = "Ethiopian", production_date = "02/12/2023")
    my_item1 = InventoryItem(name = "printer", 
                             quantity = 2, 
                             serial_num = "KJAHSD",
                            origin = item_origin)
    my_serialized_object1 = my_item1.__dict__
    print(my_serialized_object1)
    my_item2 = InventoryItem(**my_serialized_object1)
    print(my_item2.__dict__)
    
if __name__ == "__main__":
    main()
    
