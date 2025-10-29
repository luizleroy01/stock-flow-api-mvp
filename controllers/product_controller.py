from flask import jsonify, request
from services import product_service

def get_products():
    products = product_service.get_all_products()
    return jsonify(products),200

def get_product_by_filter():
    data = request.get_json()
    product = product_service.get_products_by_filter(data)
    return jsonify(product)

def create_product():
    data = request.get_json()
    new_product = product_service(data)
    return jsonify(new_product)

def update_product():
    data = request.get_json()
    update_product = product_service.update_product(data)
    return jsonify(update_product)

def delete_product():
    id_product = request.args.get('idProduct')
    response = product_service.delete_product(id_product)
    response_message = 'Excluido com sucesso' if response == 1 else None
    return jsonify({'message': response_message})

def get_products_from_file():
    file = request.files['file']
    products = product_service.get_products_from_file(file)
    return jsonify({'products':products}),200