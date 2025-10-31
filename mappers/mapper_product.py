from models import Product
from datetime import datetime
def map_product(product, data):
    if "name" in data: product.name = data["name"]
    if "description" in data: product.description = data["description"]
    if "price" in data: product.price = data["price"]
    if "stock" in data: product.stock = data["stock"]
    if "category_id" in data: product.category_id = data["category_id"]
    if "supplier_id" in data: product.supplier_id = data["supplier_id"]
    if "manufacture_date" in data:
        product.manufacture_date = datetime.strptime(data["manufacture_date"], "%Y-%m-%d").date()
    if "expiration_date" in data:
        product.expiration_date = datetime.strptime(data["expiration_date"], "%Y-%m-%d").date()
    
    return product
