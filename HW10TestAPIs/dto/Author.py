from pydantic import BaseModel, validator


class Author(BaseModel):
    name: str

    @validator("name")
    @classmethod
    def check_valid_author(cls, name: str):
        if name.istitle():
            return name
        else:
            print("Not a valid name format")
            return False

    author_id: str
