from dto import InventoryItem, ItemOrigin
from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel, field_validator


app = FastAPI()

my_inventory_items_dict: Dict[str, InventoryItem] = {InventoryItem{serial_num}, InventoryItem}


@app.put("/items/{serial_num}")
def update_item(serial_num: str):
    if serial_num in my_inventory_items_dict:
        return my_inventory_items_dict
    return "Not an item"

@app.get("items/{item}")
def read_item(serial_num: str):
    return my_inventory_items_dict
        
    

