from pydantic import BaseModel
from dto import Author, BookItem, BookStore
from fastapi import FastAPI, HTTPException

app = FastAPI()

def main():
    is_author = Author(name = "John Grisham", author_id = "HYGS-1999")
    book_item = BookItem(name = "The Broker", author = is_author, year_published = 1999)
    bookstore = BookStore(name_bookstore = "Hard2Find Books", book_shelve = book_item)
    
    my_serialised_object1 = bookstore.__dict__
    print(my_serialised_object1)
    
if __name__ == "__main__":
    main()