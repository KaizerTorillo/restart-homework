from fastapi import FastAPI
from typing import Union    #You can import List, Dict, Set, Final. 
                            #need to use Union for things like having a specific type for dictionary key:value pairs. eg. Dict[str; Union[None, str, int]]
from pydantic import BaseModel


app = FastAPI()

# The @ is a decorator.
# uvicorn main:app --reload

@app.get("/")
async def root():
    return {"message": "Hello World"}


class Item(BaseModel):
    name: str
    price: float

@app.get("/items/{item_id}")
def read_item(item_id: int, item: Item, item2: Item, q: Union[str, None] = None):    #This is saying that by default, the value of q is None but th etype for q can either be None or string. 
    return {"item_id": item_id, "q": q, "item": item, "item2": item2}


    

#Uograding this API

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}