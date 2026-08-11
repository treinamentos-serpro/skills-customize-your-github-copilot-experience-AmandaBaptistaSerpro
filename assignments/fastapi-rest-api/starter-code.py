from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")

books = [
    {"id": 1, "title": "Python Basics", "author": "Ada"},
    {"id": 2, "title": "Clean Code", "author": "Robert"},
]


class BookCreate(BaseModel):
    title: str
    author: str


class BookUpdate(BaseModel):
    title: str
    author: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


# TODO: Implement GET /books


# TODO: Implement GET /books/{book_id}


# TODO: Implement POST /books


# TODO: Implement PUT /books/{book_id}


# TODO: Implement DELETE /books/{book_id}
