from dto import InventoryItem, ItemOrigin
from fastapi import FastAPI,HTTPException
from typing import Dict

app = FastAPI()

my_inventory_item_dict: Dict[str, InventoryItem] = {}

@app.put("/items/{serial_num}")
def create_item(item: InventoryItem, serial_num: str):
    my_inventory_item_dict[serial_num] = item
    print(my_inventory_item_dict)
    
@app.get("/items/{serial_num}")
def get_item(serial_num:str):
    if serial_num in my_inventory_item_dict.keys():
        return my_inventory_item_dict
    else: 
        raise HTTPException(status_code=404, detail = "Item not found : " + serial_num)
    
@app.delete("/items/{serial_num}")
def delete_item(serial_num: str):
    if serial_num in my_inventory_item_dict.keys():
        my_delted_item = my_inventory_item_dict.pop(serial_num)
        print(my_inventory_item_dict)
        return {"msg": "Successfylly deleted"}
    else:
        raise HTTPException(status_code = 404, detail="Item not found : " + serial_num)