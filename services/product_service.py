from models.product_model import Product
from repositories import product_repository
from datetime import datetime
from app import db

def get_all_products():
    return [p.to_dict() for p in Product.query.all()]

def get_product_by_id(id_product):
    product = Product.query.get(id_product)
    return product.to_dict() if product else None

def create_product(data):
    manufacture_date = None
    expiration_date = None

    if data.get("manufacture_date"):
        manufacture_date = datetime.strptime(data["manufacture_date"], "%Y-%m-%d").date()
    if data.get("expiration_date"):
        expiration_date = datetime.strptime(data["expiration_date"], "%Y-%m-%d").date()

    new_product = Product(
        name=data["name"],
        description=data.get("description"),
        price=data["price"],
        stock=data.get("stock", 0),
        category_id=data["category_id"],
        supplier_id=data.get("supplier_id"),
        manufacture_date=manufacture_date,
        expiration_date=expiration_date
    )

    db.session.add(new_product)
    db.session.commit()
    return new_product.to_dict()

def update_product(id_product, data):
    product = Product.query.get(id_product)
    if not product:
        return None

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

    db.session.commit()
    return product.to_dict()



def get_products_by_filter(data):
    filter= data if data else {"name":'Smartwatch'}
    result = product_repository.get_products_by_filter(filter)
    return result