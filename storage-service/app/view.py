from app import app
from flask import request
from service import database, utils
import json


@app.route("/test", methods=["GET"])
def test():
    return "OK"


@app.route("/client", methods=["GET"])
def get_client():
    list_of_clients = []
    if request.args.get('name') is not None:
        list_of_clients = database.get_clients_by_name(request.args.get('name'))
    elif request.args.get('id') is not None:
        list_of_clients = database.get_clients_by_id(request.args.get('id'))
    elif request.args.get('product_id') is not None:
        list_of_clients = database.get_client_by_product_id(request.args.get('product_id'))
    return json.dumps(list_of_clients)


@app.route("/product", methods=["GET"])
def get_product():
    list_of_products = []
    if request.args.get('client_id') is not None:
        list_of_products = database.get_products_by_client_id(request.args.get('client_id'))
    elif request.args.get('space_id') is not None:
        list_of_products = database.get_products_by_space_id(request.args.get('space_id'))
    elif request.args.get('id') is not None:
        list_of_products = database.get_products_by_id(request.args.get('id'))
    return json.dumps(list_of_products, default=utils.json_converter)
