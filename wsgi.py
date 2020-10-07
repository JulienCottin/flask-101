# wsgi.py
# pylint: disable=missing-docstring

from flask import jsonify
from flask import Flask
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'test' },
}

BASE_URL = '/api/v1'

@app.route('/')
def hello():
    return "Hello World!"

@app.route(f'{BASE_URL}/products', methods=['GET'])
def read_many_products():
    return jsonify(PRODUCTS)
