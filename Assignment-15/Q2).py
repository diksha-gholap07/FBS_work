#Create a class Product with members as pid,pname,price and quantity .Add following methods:
#d. Constructor (Support both parameterized and parameterless)
#e. Destructor
#f. ShowBook
class Product:

    def __init__(self, pid=None, pname=None, price=None, quantity=None):
        self.product_id = pid
        self.product_name = pname
        self.product_price = price
        self.product_quantity = quantity
        print("Product object created.")
    
    def __del__(self):
        print("Destructor is called")

    def showProduct(self):
        print("PRODUCT INFO:")
        print("PRODUCT ID:", {self.product_id})
        print("PRODUCT NAME:", {self.product_name})
        print("PRODUCT price:", {self.product_price})
        print("PRODUCT QUANTITY:", {self.product_quantity})
        print("PRODUCT DETAILS:")

product1 = Product()
product1.product_id = 111
product1.product_name = "shoes"
product1.product_price = 600
product1.product_quantity = 100
print("###############################")

product2 = Product(222, "uniforms", 800, 100)
product2.showProduct()
