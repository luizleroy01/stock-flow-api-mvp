from flask import jsonify, request
from services import product_service

def get_products():
    products = product_service.get_all_products()
    return jsonify(products),200