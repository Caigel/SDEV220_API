from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Book(BaseModel): 
    id: int
    book_name: str
    author: str
    publisher: str

class UpdateBook(BaseModel):   
    id: Optional[int] = None
    book_name: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None

inventory = {}

@app.get("/get-book/{book_id}")
def get_book(book_id: int):
    return inventory[book_id]

@app.post("/create-book/{book_id}")
def make_book(book_id: int, book: Book):
    if book_id in inventory:
        raise HTTPException(status_code=400, detail="book already exists")
        
    inventory[book_id] = book
    return inventory[book_id]


@app.put("/update-book/{book_id}")
def update_book(book_id: int, item: UpdateBook):
    if book_id not in inventory:
        raise HTTPException(status_code=404, detail="Item does not exist")
    
    if item != None:
        inventory[book_id].id = item.id

    if item != None:
        inventory[book_id].book_name = item.book_name

    if item != None:
        inventory[book_id].author = item.author

    if item != None: 
        inventory[book_id].publisher = item.publisher

    return inventory[book_id]

@app.delete("/delete-book")
def delete_book(book_id: int):
    if book_id not in inventory:
        raise HTTPException(status_code=404, detail="Item does not exist")
    del inventory[book_id]
    return {"Success": "Item deleted!"}
    











