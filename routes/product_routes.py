from flask import Blueprint
from controllers import product_controller

product_bp = Blueprint("product_bp",__name__)

product_bp.route("/",methods=["GET"])(product_controller.get_products)
product_bp.route("/filter",methods=["POST"])(product_controller.get_product_by_filter)