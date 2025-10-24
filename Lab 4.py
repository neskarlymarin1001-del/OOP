class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.phone = ""
        self.emailID = ""
        self.balance = 0.0
        self.credit_card = []
        self.debit_card = ""

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
        print("Debit Card: ")
        self.debit_card.display_Card_info()
        if not self.credit_card:
            print("No Credit Cards")
        else:
            print("Credit Cards:")
            for card in self.credit_card:
                card.display_Card_info()

    def assign_card(self, card_object):
        if card_object.type == "debit":
            self.debit_card = card_object
        elif card_object.type == "credit":
            self.credit_card.append(card_object)


class Card:
    def __init__(self):
        self.type = ""
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.card_balance = 0.0

    def add_values_to_Card(self):
        self.type = input("Enter the Card Type (credit or debit): ")
        self.card_no = input("Enter Card Number: ")
        self.cvv = input("Enter Card CVV: ")
        self.expiry_date= input("Enter Card Expiry Date: ")

    def display_Card_info(self):
        print("Type: ", self.type)
        print("Card No: ", self.card_no)
        print("CVV: ", self.cvv)
        print("Expiry Date: ", self.expiry_date)
        print("Card Balance: ", self.card_balance)



# Main Code

c1 = Customer ()
c2 = Customer ()

card1 = Card()
card2 = Card()

c1.add_values_to_Customer()
#c2.add_values_to_Customer()

card1.add_values_to_Card()
#card2.add_values_to_Card()

c1.assign_card(card1)
#c2.assign_card(card2)

c1.display_Cust_info()
#c2.display_Cust_info()

