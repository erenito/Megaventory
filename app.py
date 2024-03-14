from flask import Flask, request, jsonify
from models import Product, SupplierClient, InventoryLocation
import requests

API_URL = "https://api.megaventory.com/v2017a/"
API_KEY = "fd0b3d806ef57f63@m146528"

app = Flask(__name__)

@app.route('/insert_product', methods=['POST'])
def insert_product():
    
    json_body = request.get_json()
    
    product = Product(json_body["ProductSKU"], json_body["ProductDescription"], json_body["ProductSellingPrice"], json_body["ProductPurchasePrice"])
    
    json_to_send = {
        "APIKEY": API_KEY,
        "mvProduct": product.to_json(),
        "mvRecordAction": "Insert"
    }
    
    response = requests.post(API_URL + "Product/ProductUpdate", json=json_to_send)
    
    response_json = response.json()
    
    if 'ResponseStatus' in response_json and response_json['ResponseStatus']['ErrorCode'] == '0':
        return jsonify({"message": "Product inserted successfully!", "data": response_json}), 200
    else:
        return jsonify({"message": "Failed to insert the product!"}), 400

@app.route('/insert_client_supplier', methods=['POST'])
def insert_client_supplier():
    
    json_body = request.get_json()
    
    supplier_client = SupplierClient(json_body["SupplierClientName"], json_body["SupplierClientEmail"], json_body["SupplierClientShippingAddress1"], json_body["SupplierClientPhone1"], json_body["SupplierClientType"])
    
    json_to_send = {
        "APIKEY": API_KEY,
        "mvSupplierClient": supplier_client.to_json(),
        "mvRecordAction": "Insert"
    }
    
    response = requests.post(API_URL + "SupplierClient/SupplierClientUpdate", json=json_to_send)
    
    response_json = response.json()
    
    if 'ResponseStatus' in response_json and response_json['ResponseStatus']['ErrorCode'] == '0':
        return jsonify({"message": f'{json_body["SupplierClientType"]} inserted successfully!', "data": response_json}), 200
    else:
        return jsonify({"message": f'Failed to insert the {json_body["SupplierClientType"]}!'}), 400

@app.route('/insert_inventory_location', methods=['POST'])
def insert_inventory_location():
    
    json_body = request.get_json()
    
    inventory_location = InventoryLocation(json_body["InventoryLocationAbbreviation"], json_body["InventoryLocationName"], json_body["InventoryLocationAddress"])
    
    json_to_send = {
        "APIKEY": API_KEY,
        "mvInventoryLocation": inventory_location.to_json(),
        "mvRecordAction": "Insert"
    }
    
    response = requests.post(API_URL + "InventoryLocation/InventoryLocationUpdate", json=json_to_send)
    
    response_json = response.json()
    
    if 'ResponseStatus' in response_json and response_json['ResponseStatus']['ErrorCode'] == '0':
        return jsonify({"message": "Inventory Location inserted successfully!", "data": response_json}), 200
    else:
        return jsonify({"message": "Failed to insert the Inventory Location!"}), 400

@app.route('/product_client_relation', methods=['POST'])
def product_client_relation():
    
    json_body = request.get_json()
    
    json_to_send = {
        "APIKEY": API_KEY,
        "mvProductClientUpdate": {
            "ProductID": json_body["ProductID"],
            "ProductClient": json_body["ProductClient"],
            },
        "mvRecordAction": "Insert"
    }
    
    response = requests.post(API_URL + "ProductClient/ProductClientUpdate", json=json_to_send)
    
    response_json = response.json()
    
    if 'ResponseStatus' in response_json and response_json['ResponseStatus']['ErrorCode'] == '0':
        return jsonify({"message": "Product-Client relation inserted successfully!", "data": response_json}), 200
    else:
        return jsonify({"message": "Failed to insert the Product-Client relation!"}), 400

if __name__ == '__main__':
    app.run(debug=True)