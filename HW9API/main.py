from dto import InventoryItem, ItemOrigin
from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel, field_validator




class ItemOrigin(BaseModel):
    country: str
    production_date: str
@field_validator("country")
@classmethod
def check_valid_country(cls, country: str): #cls is referring to the classmethod itself, similar to how self. refers to class.
    assert country == "Ethiopia", "Country name must be Ethiopia"


class InventoryItem(BaseModel):  #When defining data classes, also need to define type of data property in each data class. 
    name: str
    quantity: int
    serial_num: str
    origin: ItemOrigin  # A nested Dataclass.


def main():
    item_origin = ItemOrigin(country = "Ethiopia", production_date = "02/12/2023")
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