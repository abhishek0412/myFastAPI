# main.py

from fastapi import FastAPI

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
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}