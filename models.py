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

class SupplierClient:
    def __init__(self, name, email, shipping_address, phone, type):
        self.name = name
        self.email = email
        self.shipping_address = shipping_address
        self.phone = phone
        self.type = type

    def to_json(self):
        return {
            "SupplierClientName": self.name,
            "SupplierClientEmail": self.email,
            "SupplierClientShippingAddress1": self.shipping_address,
            "SupplierClientPhone1": self.phone,
            "SupplierClientType": self.type
        }

class InventoryLocation:
    def __init__(self, abbreviation, name, address):
        self.abbreviation = abbreviation
        self.name = name
        self.address = address

    def to_json(self):
        return {
            "InventoryLocationAbbreviation": self.abbreviation,
            "InventoryLocationName": self.name,
            "InventoryLocationAddress": self.address
        }
