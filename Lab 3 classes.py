class Book:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = 0000

    def add_book(self):
        self.book_id = input("Enter the Book ID: ")
        self.book_title = input("Enter the Book Title: ")
        self.author = input("Enter the Author: ")

    def display_book(self):
        print("\nBook Information:")
        print("Book ID: ", self.book_id)
        print("Book Title: ", self.book_title)
        print("Author: ", self.author)


class User:
    def __init__(self):
        self.userID = ""
        self.userName = ""
        self.password = ""
        self.address= ""
        self.phone = ""
        self.email = ""
        self.books_borrowed = []

    def add_user(self):
        self.userID = input("Enter the User ID: ")
        self.userName = input("Enter the User Name: ")
        self.address = input("Enter the User Address: ")
        self.phone = input("Enter the User Phone: ")
        self.email = input("Enter the User Email: ")

    def borrow_book(self, book):
        self.books_borrowed.append(book)
        print(f"{self.userName} borrowed '{book.book_title}'.")

    def display_user(self):
        print("\nUser Information:")
        print("User ID: ", self.userID)
        print("User Name: ", self.userName)
        print("User Password: ", self.password)
        print("User Address: ", self.address)
        print("User Phone: ", self.phone)
        print("User Email: ", self.email)
        if not self.books_borrowed:
            print("No books borrowed.")
        else:
            print("Books borrowed:")
            for b in self.books_borrowed:
                print(f" - {b.book_title} by {b.author}")

class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email_id = ""

    def add_author(self):
        self.author_id = input("Enter the Author ID: ")
        self.author_name = input("Enter the Author Name: ")
        self.affiliation = input("Enter the Affiliation: ")
        self.country = input("Enter the Country: ")
        self.phone = input("Enter the Phone: ")
        self.email_id = input("Enter the Email: ")

    def display_author(self):
        print("\nAuthor Information:")
        print("Author ID: ", self.author_id)
        print("Author Name: ", self.author_name)
        print("Affiliation: ", self.affiliation)
        print("Country: ", self.country)
        print("Phone: ", self.phone)
        print("Email: ", self.email_id)


# Main Code

# Create users and books
b1 = Book()
b2 = Book()
b3 = Book()

u1 = User()
u2 = User()
u3 = User()

# Add user info
u1.add_user()
u2.add_user()

# Add book info
b1.add_book()
b2.add_book()
b3.add_book()


# Borrow some books
u1.borrow_book(b1)
u1.borrow_book(b3)
u2.borrow_book(b2)


# Display info
print("\n--- User Details ---")
u1.display_user()
u2.display_user()