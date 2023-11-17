from pydantic import BaseModel, field_validator
from .Author import Author

class BookItem(BaseModel):
    name: str
    author: Author
    year_published: int 
    @field_validator("year_published")
    @classmethod
    def check_valid_year(cls, year_published: int):
        assert year_published in range (-3000, 2024), "year of publication not in range."
        return year_published