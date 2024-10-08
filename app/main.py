from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Всем привет"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": f'{q}'}


@app.get("/hello/{name}")
def hello_name(name: str):
    return {"hello": f'Привет {name}'}