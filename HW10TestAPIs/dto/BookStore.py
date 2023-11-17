#importing the BookItem class from the book_item module
from pydantic import BaseModel
from .BookItem import BookItem

class BookStore(BaseModel):
    name_bookstore: str
    book_shelve: BookItem
    