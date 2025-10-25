import pickle

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
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("Insufficient balance")

    def credit_to(self, amount):
        self.balance = self.balance + amount

    def display_Cust_info(self):
        print("\n Customer Info: ")
        print("CID: ", self.cid)
        print("Name: ", self.cname)
        print("Account Number: ", self.acc_no)
        print("Phone Number: ", self.phone)
        print("Email: ", self.emailID)
        print("Balance: ", self.balance)
        print("Debit Card: ")
        if self.debit_card:
            self.debit_card.display_Card_info()
        else:
            print("No Debit Card")
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
        print(f"  Type: {self.type}")
        print(f"  Card No: {self.card_no}")
        print(f"  CVV: {self.cvv}")
        print(f"  Expiry Date: {self.expiry_date}")
        print(f"  Card Balance: {self.card_balance}")



# Main Code

customers = []
cards = []


while True:
    print("Welcome!")
    print("1. Create customer objects")
    print("2. Create card objects")
    print("3. Transfer funds between customer objects")
    print("4. Assign card objects to customer objects")
    print("5. Display customer info")
    print("6. Display card info")
    print("7. Commit (Save Data)")
    print("8. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        c1 = Customer ()
        c1.add_values_to_Customer()
        customers.append(c1)

    elif option == "2":
        card1 = Card()
        card1.add_values_to_Card()
        cards.append(card1)

    elif option == "3":
        if len(customers) < 2:
            print("Need at least two customers to transfer funds.")
        else:
            c_debitID = input("Enter the ID of the customer you want to debit from: ")
            c_creditID = input("Enter the ID of the customer you want to credit to: ")
            amount = float(input("Please enter amount to be credited and debited: "))

            sender = None
            receiver = None

            for customer in customers:
                if customer.cid == c_debitID:
                    sender = customer
                    break

            for c in customers:
                if c.cid == c_creditID:
                    receiver = c
                    break

            if sender is not None and receiver is not None:
                sender.debit_from(amount)
                receiver.credit_to(amount)
                print("Transfer completed")
            else:
                print("Invalid customer ID")

    elif option == "4":
        if not customers or not cards:
            print("No customers or cards available.")
        else:
            cid = input("Enter the ID of the customer: ")
            card_no = input("Enter the Card Number to assign: ")

            customer = None
            card = None

            for c in customers:
                if c.cid == cid:
                    customer = c
                    break

            for crd in cards:
                if crd.card_no == card_no:
                    card = crd
                    break

            if customer is not None and card is not None:
                customer.assign_card(card)
        
    elif option == "5":
        if not customers:
            print("No customers available")
        else:
            for c in customers:
                c.display_Cust_info()

    elif option == "6":
        if not cards:
            print("No cards available")
        else:
            for card in cards:
                card.display_Card_info()
                
    elif option == "7":
        with open("bank.dat", "wb") as file:
            pickle.dump([customers, cards], file)
        print("Data saved to bank.dat")

    elif option == "8":
        print("Exiting program...")
        break

    else:
        print("Invalid option")

        
