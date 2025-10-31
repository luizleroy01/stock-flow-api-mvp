from models.product_model import Product
from repositories import product_repository
from mappers import mapper_product
from app import db
from utils import file_context

def get_all_products():
    return [p.to_dict() for p in Product.query.all()]

def get_product_by_id(id_product):
    product = Product.query.get(id_product)
    return product.to_dict() if product else None

def create_product(data):

    new_product = mapper_product.map_product(Product(),data)

    db.session.add(new_product)
    db.session.commit()
    return new_product.to_dict()

def update_product(id_product, data):
    product = Product.query.get(id_product)
    if not product:
        return None

    product = mapper_product(product,data)

    db.session.commit()
    return product.to_dict()

def delete_product(id_product):
    prod = Product.query.delete(id_product)
    return prod

def get_products_from_file(file):
    print(file)
    data = file_context.get_data_from_file(file)
    
    return data
