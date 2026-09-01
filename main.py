from fastapi import FastAPI
from pydantic import BaseModel
from routers.productRouter import router as product_router

app = FastAPI()
app.include_router(product_router)


class PostHello(BaseModel):
    name: str
    age: int


@app.post("/hello")
def create_hello(post_hello: PostHello):
    print(post_hello)
    return {
        "message": f"Hello {post_hello.name}, you are {post_hello.age} years old"
    }


@app.get("/")
def read_root(name: str, age: int):
    return {
        "message": f"Hello {name}, you are {age} years old"
    }


@app.get("/items/{name}")
def read_item(name: str):
    return {
        "item_name": name
    }
