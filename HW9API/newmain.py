from dto import InventoryItem, ItemOrigin
from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI()

my_inventory_item_dict: Dict[str, InventoryItem] = {}


@app.put("/items/{serial_num}")
def create_item(
    item: InventoryItem, serial_num: str
) -> None:  # This is for the output, so that it will say None instaed of just "string"
    my_inventory_item_dict[serial_num] = item
    print(my_inventory_item_dict)


@app.get("/items/{serial_num}")  # Getting one item.
def get_item(serial_num: str) -> InventoryItem:
    if serial_num in my_inventory_item_dict.keys():
        return my_inventory_item_dict
    else:
        raise HTTPException(status_code=404, detail="Item not found : " + serial_num)


@app.delete("/items/{serial_num}")
def delete_item(serial_num: str) -> Dict:
    if serial_num in my_inventory_item_dict.keys():
        my_delted_item = my_inventory_item_dict.pop(serial_num)
        print(my_inventory_item_dict)
        return {"msg": "Successfylly deleted"}
    else:
        raise HTTPException(status_code=404, detail="Item not found : " + serial_num)


@app.get("/items/")  # What if we want multiple items? Use this
def get_items() -> List[InventoryItem]:
    return (
        my_inventory_item_dict.values()
    )  # We are only wanting a list of the values, not the whole dictionary.
