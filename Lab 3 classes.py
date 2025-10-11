class Book:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = 0

    def add_book(self):
        self.book_id = input("Enter the Book ID: ")
        self.book_title = input("Enter the Book Title: ")
        self.publisher = input("Enter the Publisher: ")
        self.year_of_publication = int(input("Enter the Year of Publication: "))
        self.year_of_publication = 0

    def display_book(self):
        print("\nBook Information:")
        print("Book ID: ", self.book_id)
        print("Book Title: ", self.book_title)
        print("Author: ", self.author)
        print("Publisher: ", self.publisher)
        print("Year of Publication: ", self.year_of_publication)

class User:
    def __init__(self):
        self.userID = ""
        self.userName = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.email = ""
        self.books_borrowed = []

    def add_user(self):
        self.userID = input("Enter the User ID: ")
        self.userName = input("Enter the User Name: ")
        self.password = input("Enter Password: ")
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
                print(f"{b.book_title} by {b.author}")


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

books = {}    
authors = {}  
users = {}    

while True:
    print("===== Welcome to the Library Management System =====")
    print("1. Add Author")
    print("2. Add Book")
    print("3. Add User")
    print("4. Borrow Book")
    print("5. Display Authors")
    print("6. Display Books")
    print("7. Display Users")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        author = Author()
        author.add_author()
        authors[author.author_id] = author
        print(f"Author '{author.author_name}' added successfully.")

    elif choice == "2":
        book = Book()
        book.add_book()
        author_id = input("Enter the Author ID for this book: ")
        if author_id in authors:
            book.author = authors[author_id].author_name
            book.author_id = author_id
            books[book.book_id] = book
            print(f"Book '{book.book_title}' added successfully.")
        else:
            print("Author not found. Add the author first.")

    elif choice == "3":
        user = User()
        user.add_user()
        users[user.userID] = user
        print(f"User '{user.userName}' added successfully.")

    elif choice == "4":
        user_id = input("Enter User ID: ")
        book_id = input("Enter Book ID: ")
        if user_id in users and book_id in books:
            users[user_id].borrow_book(books[book_id])
        else:
            print("User or Book not found.")

    elif choice == "5":
        if authors:
            for a in authors.values():
                a.display_author()
        else:
            print("No authors available.")

    elif choice == "6":
        if books:
            for b in books.values():
                b.display_book()
        else:
            print("No books available.")

    elif choice == "7":
        if users:
            for u in users.values():
                u.display_user()
        else:
            print("No users available.")

    elif choice == "8":
        print("Exiting Library System.")
        break

    else:
        print("Invalid choice. Try again.")
