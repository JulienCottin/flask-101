# wsgi.py
# pylint: disable=missing-docstring

from flask import jsonify
from flask import Flask
app = Flask(__name__)

from flask import request
import itertools

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'test' },
}

START_INDEX = len(PRODUCTS) + 1
IDENTIFIER_GENERATOR = itertools.count(START_INDEX)

BASE_URL = '/api/v1'

@app.route('/')
def hello():
    return "Hello World!"

@app.route(f'{BASE_URL}/products', methods=['GET'])
def read_many_products():
    return jsonify(PRODUCTS)

@app.route(f'{BASE_URL}/products/<int:product_id>', methods=['GET'])
def read_single_product(product_id):
    if PRODUCTS.get(product_id) is None:
        return '', 404
    return jsonify(PRODUCTS[product_id]), 200

@app.route(f'{BASE_URL}/products/<int:product_id>', methods=['DELETE'])
def delete_single_product(product_id):
    deleted_product=PRODUCTS.pop(product_id, None)
    if deleted_product is None :
        return '', 404
    return '', 204

@app.route(f'{BASE_URL}/products', methods=['POST'])
def create_single_product():
    product_id=(next(IDENTIFIER_GENERATOR))
    product_name=request.get_json()
    new_product={ 'id': product_id, 'name': product_name['name'] }
    PRODUCTS[product_id]=new_product
    return jsonify(PRODUCTS[product_id]), 201
