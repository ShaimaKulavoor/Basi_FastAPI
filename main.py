from fastapi import FastAPI, Request
from mockData import products
from dtos import ProductDTO
app = FastAPI()

@app.get("/")
def home():
    return "Welcome to byshaims!"

@app.get("/contact")
def contact():
    return "you can connect us on instagram too"

@app.get("/products")
def get_products():
    return products

## Path Parameters..
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
## if product available with the id, return product, else return error message. 
    product = None
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
           return oneProduct
    
    return {
        "error": "product not found"
    }

## query params
@app.get("/greet")
def greet_user(request:Request):
    query_params=dict(request.query_params)
    print(query_params)
    return {
        "greet" : f"Hello {query_params.get('name')}, your age is {query_params.get('age')}"

    }

## body, headers - request headers, querybparams 

## http methods
@app.post("/create_product") 
def create_product(product_data:ProductDTO):
    product_data=product_data.model_dump()
    print(product_data)
    products.append(product_data)

    return {"status": "product created successfully", "data": products} 

@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO, product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump() 
            return {"status": "product updated successfully" , "product": product_data}

        
    return {
            "error": "product not found"
        }

@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product =products.pop(index)
            return {"status": "product deleted successfully" , "product":deleted_product}
    return {
            "error": "product not found"
        }
## pydentic






##postman     
    