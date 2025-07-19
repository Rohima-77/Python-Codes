class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def update_price(self, new_price):
        self.price = new_price
        print(f"Price updated for {self.name}")
    
    def update_quantity(self, change):
        self.quantity += change
        print(f"Quantity updated for {self.name}. New quantity: {self.quantity}")
    
    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")

class Inventory:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        self.products[product.product_id] = product
        print(f"Added {product.name} to inventory")
    
    def remove_product(self, product_id):
        if product_id in self.products:
            product = self.products.pop(product_id)
            print(f"Removed {product.name} from inventory")
        else:
            print("Product not found")
    
    def display_inventory(self):
        print("Current Inventory:")
        for product in self.products.values():
            product.display_info()
            print("---")


inventory = Inventory()
product1 = Product("P001", "Laptop", 999.99, 10)
product2 = Product("P002", "Mouse", 19.99, 50)

inventory.add_product(product1)
inventory.add_product(product2)
product1.update_quantity(-2)  # Selling 2 laptops
inventory.display_inventory()
