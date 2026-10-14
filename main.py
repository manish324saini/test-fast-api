from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/products")
def getProducts():
    return {"message": "Phone Store API", "products": ["iPhone 13", "Samsung Galaxy S21", "Google Pixel 6"], "status": "success", "code": 200}

@app.get("/productsdetails}")
def getProductsDetails():
    return {"message": "Phone Store API", "products": [{"name": "iPhone 13", "price": 799, "stock": 50}, {"name": "Samsung Galaxy S21", "price": 699, "stock": 30}, {"name": "Google Pixel 6", "price": 599, "stock": 20}], "status": "success", "code": 200}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
