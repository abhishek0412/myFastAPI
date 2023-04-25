# main.py

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

import getpass


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

# all the get call
@app.get("/")
async def root():
    return {"message": "Hello World! This is my first fatAPI"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": getpass.getuser()}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}



# all the post calls
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# all the put calls
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}