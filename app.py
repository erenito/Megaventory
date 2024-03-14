from flask import Flask, request, jsonify
from models import Product, Client, Supplier, InventoryLocation
import requests

API_URL = "https://api.megaventory.com/v2017a/"
API_KEY = "cf2ed6cf718d3664@m146528"

app = Flask(__name__)

@app.route('/insert_product', methods=['POST'])
def insert_product():
    
    json_body = request.get_json()
    
    product = Product(json_body["ProductSKU"], json_body["ProductDescription"], json_body["ProductSellingPrice"], json_body["ProductPurchasePrice"])
    
    json_to_send = {
        "APIKEY": API_KEY,
        "mvProduct": product.to_json(),
        "mvRecordAction": "Insert",
        "mvInsertUpdateDeleteSourceApplication": "WooCommerce"
    }
    
    response = requests.post(API_URL + "Product/ProductUpdate", json=json_to_send)
    
    response_json = response.json()
    
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    
    if 'ResponseStatus' in response_json and response_json['ResponseStatus']['ErrorCode'] == '0':
        return jsonify({"message": "Product inserted successfully!", "data": response_json}), 200
    else:
        return jsonify({"message": "Failed to insert the product.", "error": response_json}), 400
    

if __name__ == '__main__':
    app.run(debug=True)