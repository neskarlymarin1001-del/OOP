import pickle

class Product:

    def __int__(self):
        self.pid = ""
        self.pname = ""
        self.price = 0.0
        self.description = ""

    def get_product_details(self):
        self.pid = input("Enter the PID: ")
        self.pname = input("Enter the product name: ")
        self.price = float(input("Enter the price: "))
        self.description = input("Enter the product description: ")

    def display_product_info(self):
        print("Product ID: ", self.pid)
        print("Product Name: ", self.pname)
        print("Product Price: ", self.price)
        print("Product Description: ", self.description)

# Main Code

while 1:

    print("Please choose one of the following: ")
    print("1. Create a product object")
    print("2. Get info for the product")
    print("3. Display the product")
    print("4. Write the product into a file")
    print("5. Read from the file and display the product info")
    print("6. Exit")

    option = input("Please enter your choice here: ")

    if option == "1":
        product_obj = Product ()

    elif option == "2":
        product_obj.get_product_details()

    elif option == "3":
        product_obj.display_product_info()

    elif option == "4":
        f1 = open("product_inventory.dat", "ab")
        pickle.dump(product_obj, f1)
        f1.close()

    elif option == "5":
        f2 = open("product_inventory.dat", "rb")
        while 1:
            try:
                received_product = pickle.load(f2)
                received_product.display_product_info()
                print(received_product.pname)
            except EOFError:
                break
        f2.close()




