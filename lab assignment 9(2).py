class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)
        if self.available:
            print("Status  : Available")
        else:
            print("Status  : Issued")


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book)

        print("Book added successfully.")

    def add_member(self):
        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")

        member = Member(member_id, name)
        self.members.append(member)

        print("Member added successfully.")

    def lend_book(self):
        book_id = input("Enter Book ID to lend: ")

        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return

        print("Book not found.")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return

        print("Book not found.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books in library.")
        else:
            for book in self.books:
                print()
                book.display()


library = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.add_member()

    elif choice == 3:
        library.lend_book()

    elif choice == 4:
        library.return_book()

    elif choice == 5:
        library.display_books()

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
