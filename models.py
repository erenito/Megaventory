class Product:
    def __init__(self, sku, description, sales_price, purchase_price):
        self.sku = sku
        self.id = None
        self.description = description
        self.sales_price = sales_price
        self.purchase_price = purchase_price

    def to_json(self):
        return {
            "ProductSKU": self.sku,
            "ProductDescription": self.description,
            "ProductSellingPrice": self.sales_price,
            "ProductPurchasePrice": self.purchase_price
        }

class Client:
    def __init__(self, name, email, shipping_address, phone):
        self.name = name
        self.email = email
        self.shipping_address = shipping_address
        self.phone = phone

    def to_json(self):
        return {
            'Name': self.name,
            'Email': self.email,
            'Address': self.shipping_address,
            'Phone': self.phone
        }

class Supplier:
    def __init__(self, name, email, shipping_address, phone):
        self.name = name
        self.email = email
        self.shipping_address = shipping_address
        self.phone = phone

    def to_json(self):
        return {
            'Name': self.name,
            'Email': self.email,
            'Address': self.shipping_address,
            'Phone': self.phone
        }

class InventoryLocation:
    def __init__(self, abbreviation, name, address):
        self.abbreviation = abbreviation
        self.name = name
        self.address = address

    def to_json(self):
        return {
            'Abbreviation': self.abbreviation,
            'Name': self.name,
            'Address': self.address
        }
