from models.product_model import Product
from app import db

def get_all_products():
    return [p.to_dict() for p in Product.query.all()]