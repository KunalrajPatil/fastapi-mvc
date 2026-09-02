from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel
from typing import Optional
from models.productModel import Product

app = FastAPI()


# -----------------------------
# In-memory database
# -----------------------------
products = []
product_id = 0


# -----------------------------
# Root API
# -----------------------------
@app.get("/")
def read_root():
    return {
        "message": "backend to bhag rha hai"
    }


# -----------------------------
# Create Product
# POST /products
# -----------------------------
@app.post("/products", status_code=201)
def create_product(product: Product):
    global product_id

    product_id += 1
    product.id = product_id

    products.append(product)

    return {
        "isSuccess": True,
        "message": "Product created successfully",
        "product": product
    }


# -----------------------------
# Get All Products
# GET /products
# -----------------------------
@app.get("/products")
def get_products():
    return {
        "isSuccess": True,
        "products": products
    }


# -----------------------------
# Get Particular Product
# GET /products/{product_id}
# -----------------------------
@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:
        if product.id == product_id:
            return {
                "isSuccess": True,
                "product": product
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):

    for index, product in enumerate(products):

        if product.id == product_id:

            # Keep the existing ID
            updated_product.id = product_id

            products[index] = updated_product

            return {
                "isSuccess": True,
                "message": "Product updated successfully",
                "product": updated_product
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    for index, product in enumerate(products):

        if product.id == product_id:

            deleted_product = products.pop(index)

            return {
                "isSuccess": True,
                "message": "Product deleted successfully",
                "product": deleted_product
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )