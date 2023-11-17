from pydantic import BaseModel
from dto import Author, BookItem, BookStore
from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI()

my_book_items_dict: Dict[str, BookItem] = {}

@app.put("/books/{name}")
def create_item(name : str, item : BookItem) -> None:
    my_book_items_dict[name] = item
    print(my_book_items_dict)
    
@app.get("/books/{name}")
def get_item(name:str) -> BookItem:
    if name in my_book_items_dict.keys():
        return my_book_items_dict
    else:
        raise HTTPException(status_code = 404, detail = "Book not found : " + name)
    
@app.delete("/books/{name}")
def delete_item(name:str) -> Dict:
    if name in my_book_items_dict.keys():
        my_deleted_book = my_book_items_dict.pop(name)
        print(my_book_items_dict)
        return {"msg" : "Successfully deleted book from register"}
    else:
        raise HTTPException(status_code=404, detail = "Error: Book not found : " + name)