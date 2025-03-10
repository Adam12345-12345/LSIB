class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        self.borrowed_by = None

    def __str__(self):
        return f"'{self.title}' by {self.author} (Available: {self.available})"

    def borrow(self, member):
        if self.available:
            self.available = False
            self.borrowed_by = member
            return True
        else:
            return False

    def return_book(self):
        self.available = True
        self.borrowed_by = None
        return True


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name} (Borrowed Books: {len(self.borrowed_books)})"

    def borrow_book(self, book):
        if book.borrow(self):
            self.borrowed_books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        else:
            return False


class LibrarySystem:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        return book

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return True
        else:
            return False

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        return member

    def remove_member(self, member):
        if member in self.members:
            for book in member.borrowed_books[:]:
                book.return_book()
            self.members.remove(member)
            return True
        else:
            return False

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def display_books(self):
        for book in self.books:
            print(book)

    def display_members(self):
        for member in self.members:
            print(member)


def display_menu():
    print("\nLibrary Management System Menu:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Add Member")
    print("4. Remove Member")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Display Books")
    print("8. Display Members")
    print("9. Exit")


def get_book_info():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    return title, author


def get_member_name():
    name = input("Enter member name: ")
    return name


def get_book_by_title(library):
    title = input("Enter book title: ")
    return library.find_book(title)


def get_member_by_name(library):
    name = input("Enter member name: ")
    return library.find_member(name)


def main():
    library = LibrarySystem()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
            if choice == 1:
                title, author = get_book_info()
                library.add_book(title, author)
                print("Book added successfully.")
            elif choice == 2:
                book = get_book_by_title(library)
                if book:
                    library.remove_book(book)
                    print("Book removed successfully.")
                else:
                    print("Book not found.")
            elif choice == 3:
                name = get_member_name()
                library.add_member(name)
                print("Member added successfully.")
            elif choice == 4:
                member = get_member_by_name(library)
                if member:
                    library.remove_member(member)
                    print("Member removed successfully.")
                else:
                    print("Member not found.")
            elif choice == 5:
                member = get_member_by_name(library)
                book = get_book_by_title(library)
                if member and book:
                    if member.borrow_book(book):
                        print(f"{member.name} borrowed {book.title}.")
                    else:
                        print(f"{book.title} is not available.")
                else:
                    print("Member or book not found.")

            elif choice == 6:
                member = get_member_by_name(library)
                book = get_book_by_title(library)
                if member and book:
                    if member.return_book(book):
                        print(f"{member.name} returned {book.title}.")
                    else:
                        print(f"{member.name} did not borrow {book.title}.")
                else:
                    print("Member or book not found.")
            elif choice == 7:
                library.display_books()
            elif choice == 8:
                library.display_members()
            elif choice == 9:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
