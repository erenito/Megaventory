from flask import Flask, request, jsonify
from models import Product, SupplierClient, InventoryLocation
import requests

API_URL = "https://api.megaventory.com/v2017a/"
API_KEY = "YOUR_API_KEY"

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
        return jsonify({"message": "Failed to insert the product!", "data": response_json}), 400

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
        return jsonify({"message": f'Failed to insert the {json_body["SupplierClientType"]}!', "data": response_json}), 400

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
        return jsonify({"message": "Failed to insert the Inventory Location!", "data": response_json}), 400
    

@app.route('/get_product', methods=['GET'])
def get_product():
    
    json_body = request.get_json()
    
    json_to_send = {
        "APIKEY": API_KEY,
        "Filters": [
            {
            "FieldName": "ProductSKU",
            "SearchOperator": "Equals",
            "SearchValue": json_body["ProductSKU"]
            }
        ],
        "ReturnTopNRecords": 1
    }
    
    response = requests.post(API_URL + "Product/ProductGet", json=json_to_send)
    
    response_json = response.json()
    
    return response_json["mvProducts"][0]


@app.route('/get_client_supplier', methods=['GET'])
def get_client_supplier():
        
    json_body = request.get_json()
    
    json_to_send = {
        "APIKEY": API_KEY,
        "Filters": [
            {
            "FieldName": "SupplierClientName",
            "SearchOperator": "Equals",
            "SearchValue": json_body["SupplierClientName"]
            }
        ]
    }
    
    response = requests.post(API_URL + "SupplierClient/SupplierClientGet", json=json_to_send)
    
    response_json = response.json()
    
    return response_json["mvSupplierClients"][0]

@app.route('/get_inventory_location', methods=['GET'])
def get_inventory_location():
        
    json_body = request.get_json()
        
    json_to_send = {
        "APIKEY": API_KEY,
        "Filters": [
            {
            "FieldName": "InventoryLocationAbbreviation",
            "SearchOperator": "Equals",
            "SearchValue": json_body["InventoryLocationAbbreviation"]
            }
        ],
        "ReturnTopNRecords": 1
    }
    
    response = requests.post(API_URL + "InventoryLocation/InventoryLocationGet", json=json_to_send)
    
    response_json = response.json()
    
    return response_json["mvInventoryLocations"][0]

@app.route('/product_client_relation', methods=['POST'])
def product_client_relation():
    
    json_body = request.get_json()
    
    product_id = requests.get('http://127.0.0.1:5000/get_product', json={"ProductSKU": json_body["ProductSKU"]}).json()["ProductID"]
    
    sup_client_id = requests.get('http://127.0.0.1:5000/get_client_supplier', json={"SupplierClientName": json_body["SupplierClientName"]}).json()["SupplierClientID"]
    
    print(product_id, sup_client_id)
    
    json_to_send = {
        "APIKEY": API_KEY,
        "mvProductClientUpdate": {
            "ProductID": product_id,
            "ProductClientID": sup_client_id,
            },
        "mvRecordAction": "Insert"
    }
    
    response = requests.post(API_URL + "ProductClient/ProductClientUpdate", json=json_to_send)
    
    response_json = response.json()
    
    if 'ResponseStatus' in response_json and response_json['ResponseStatus']['ErrorCode'] == '0':
        return jsonify({"message": "Product-Client relation inserted successfully!", "data": response_json}), 200
    else:
        return jsonify({"message": "Failed to insert the Product-Client relation!", "data": response_json}), 400

@app.route('/product_supplier_relation', methods=['POST'])
def product_supplier_relation():
    
    json_body = request.get_json()
    
    product_id = requests.get('http://127.0.0.1:5000/get_product', json={"ProductSKU": json_body["ProductSKU"]}).json()["ProductID"]
    
    sup_client_id = requests.get('http://127.0.0.1:5000/get_client_supplier', json={"SupplierClientName": json_body["SupplierClientName"]}).json()["SupplierClientID"]
    
    json_to_send = {
        "APIKEY": API_KEY,
        "mvProductSupplierUpdate": {
            "ProductID": product_id,
            "ProductSupplierID": sup_client_id,
            },
        "mvRecordAction": "Insert"
    }
    
    response = requests.post(API_URL + "ProductSupplier/ProductSupplierUpdate", json=json_to_send)
    
    response_json = response.json()
    
    if 'ResponseStatus' in response_json and response_json['ResponseStatus']['ErrorCode'] == '0':
        return jsonify({"message": "Product-Supplier relation inserted successfully!", "data": response_json}), 200
    else:
        return jsonify({"message": "Failed to insert the Product-Supplier relation!", "data": response_json}), 400


@app.route('/product_inventory_location_relation', methods=['POST'])
def product_inventory_location_relation():
    
    json_body = request.get_json()

    inventory_location_id = requests.get('http://127.0.0.1:5000/get_inventory_location', json={"InventoryLocationAbbreviation": json_body["InventoryLocationAbbreviation"]}).json()["InventoryLocationID"]

    json_to_send = {
        "APIKEY": API_KEY,
        "mvProductStockUpdateList": [
            {
            "ProductSKU": product_sku["ProductSKU"],
            "ProductQuantity": json_body["ProductQuantity"],
            "InventoryLocationID": inventory_location_id
            } for product_sku in json_body["ProductSKUs"]
        ] 
    }
    
    response = requests.post(API_URL + "InventoryLocationStock/ProductStockUpdate", json=json_to_send)
    
    response_json = response.json()
    
    if 'ResponseStatus' in response_json and response_json['ResponseStatus']['ErrorCode'] == '0':
        return jsonify({"message": "Product-Inventory Location relation inserted successfully!", "data": response_json}), 200
    else:
        return jsonify({"message": "Failed to insert the Product-Inventory Location relation!", "data": response_json}), 400
    
if __name__ == '__main__':
    app.run(debug=True)