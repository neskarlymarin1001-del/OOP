class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.phone = ""
        self.emailID = ""
        self.balance = 0.0

    def add_values_to_Customer(self):
        self.cid = input("Enter Customer ID: ")
        self.cname = input("Enter Customer Name: ")
        self.acc_no = input("Enter Account Number: ")
        self.phone = input("Enter Customer Phone Number: ")
        self.emailID = input("Enter Customer Email ID: ")
        self.balance= float(input("Enter Customer Balance: "))

    def debit_from(self, amount):
        self.balance = self.balance - amount


    def credit_to(self, amount):
        self.balance = self.balance + amount

    def display_Cust_info(self):
        print("CID: ", self.cid)
        print("Name: ", self.cname)
        print("Account Number: ", self.acc_no)
        print("Phone Number: ", self.phone)
        print("Email: ", self.emailID)
        print("Balance: ", self.balance)


# Main Code

c1 = Customer ()
c2 = Customer ()

c1.add_values_to_Customer()
c2.add_values_to_Customer()

amount = float(input("Please enter amount to be credited and debited: "))
c1.debit_from(amount)
c2.credit_to(amount)

c1.display_Cust_info()
c2.display_Cust_info()