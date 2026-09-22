# Library Management System using OOP

# Class to represent a Book
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author 
        self.is_borrowed = False

    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, "
              f"Author: {self.author}, Status: {status}")


# Class to represent a Patron (Library User)
class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron ID: {self.patron_id}, Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:", ", ".join(self.borrowed_books))
        else:
            print("No books borrowed.")


# Class to represent the Library
class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add a new book
    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    # Register a new patron
    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    # Borrow a book
    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print(f"Book '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book.title)
            print(f"{patron.name} borrowed '{book.title}'.")

    # Return a book
    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.title in patron.borrowed_books:
            patron.borrowed_books.remove(book.title)
            book.is_borrowed = False
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print(f"{patron.name} has not borrowed '{book.title}'.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            book.display()

    # Display all patrons
    def display_patrons(self):
        print("\nRegistered Patrons:")
        for patron in self.patrons.values():
            patron.display()
            print("-" * 30)
