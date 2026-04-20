from pydantic import BaseModel


class Book(BaseModel):
    id : str | None
    title :  str | None
    author : str | None
    number : int | None
