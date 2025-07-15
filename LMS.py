import datetime

books = {
    "B001": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": True, "borrower_id": None, "due_date": None},
    "B002": {"title": "1984", "author": "George Orwell", "available": True, "borrower_id": None, "due_date": None},
    "B003": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "available": True, "borrower_id": None, "due_date": None},
    "B004": {"title": "Moby Dick", "author": "Herman Melville", "available": True, "borrower_id": None, "due_date": None},
    "B005": {"title": "Pride and Prejudice", "author": "Jane Austen", "available": True, "borrower_id": None, "due_date": None}
}

members = {
    "M001": {"name": "0001", "borrowed_books": []},
    "M002": {"name": "0002", "borrowed_books": []},
    "M003": {"name": "0003", "borrowed_books": []},
    "M004": {"name": "0004", "borrowed_books": []},
    "M005": {"name": "0005", "borrowed_books": []}
}


# Book management
def add_book(book_id, title, author):
    if book_id in books:
        print("Book ID already exists.")
        return
    books[book_id] = {
        "title": title,
        "author": author,
        "available": True,
        "borrower_id": None,
        "due_date": None
    }
    print("Book added successfully.")

def update_book(book_id, title=None, author=None):
    if book_id not in books:
        print("Book not found.")
        return
    if title:
        books[book_id]["title"] = title
    if author:
        books[book_id]["author"] = author
    print("Book updated successfully.")

def delete_book(book_id):
    if book_id not in books:
        print("Book not found.")
        return
    if not books[book_id]["available"]:
        print("Cannot delete a borrowed book.")
        return
    del books[book_id]
    print("Book deleted.")

def search_books(keyword):
    found = False
    for book_id, book in books.items():
        if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
            print_book(book_id, book)
            found = True
    if not found:
        print("No books found.")

def list_books():
    if not books:
        print("No books in the library.")
        return
    for book_id, book in books.items():
        print_book(book_id, book)

def print_book(book_id, book):
    status = "Available" if book["available"] else f"Borrowed by Member ID {book['borrower_id']} until {book['due_date']}"
    print(f"[{book_id}] {book['title']} by {book['author']} - {status}")

# Member management
def add_member(member_id, name):
    if member_id in members:
        print("Member ID already exists.")
        return
    members[member_id] = {
        "name": name,
        "borrowed_books": []
    }
    print("Member added successfully.")

def delete_member(member_id):
    if member_id not in members:
        print("Member not found.")
        return
    if members[member_id]["borrowed_books"]:
        print("Cannot delete member with borrowed books.")
        return
    del members[member_id]
    print("Member deleted.")

def search_members(keyword):
    found = False
    for member_id, member in members.items():
        if keyword.lower() in member["name"].lower():
            print_member(member_id, member)
            found = True
    if not found:
        print("No members found.")

def list_members():
    if not members:
        print("No members in the system.")
        return
    for member_id, member in members.items():
        print_member(member_id, member)

def print_member(member_id, member):
    print(f"[{member_id}] {member['name']} - Borrowed books: {member['borrowed_books']}")

# Borrow and return
def borrow_book(book_id, member_id):
    if book_id not in books:
        print("Book not found.")
        return
    if member_id not in members:
        print("Member not found.")
        return
    if not books[book_id]["available"]:
        print("Book is already borrowed.")
        return
    due_date = datetime.date.today() + datetime.timedelta(days=14)
    books[book_id]["available"] = False
    books[book_id]["borrower_id"] = member_id
    books[book_id]["due_date"] = due_date
    members[member_id]["borrowed_books"].append(book_id)
    print(f"Book borrowed successfully. Due date: {due_date}")

def return_book(book_id, member_id):
    if book_id not in books:
        print("Book not found.")
        return
    if member_id not in members:
        print("Member not found.")
        return
    if books[book_id]["borrower_id"] != member_id:
        print("This member did not borrow this book.")
        return
    books[book_id]["available"] = True
    books[book_id]["borrower_id"] = None
    books[book_id]["due_date"] = None
    members[member_id]["borrowed_books"].remove(book_id)
    print("Book returned successfully.")

# Menu
def main():
    while True:
        print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Books")
        print("5. List All Books")
        print("6. Add Member")
        print("7. Delete Member")
        print("8. Search Members")
        print("9. List All Members")
        print("10. Borrow Book")
        print("11. Return Book")
        print("12. Exit")
        choice = input("Select an option (1-12): ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")
            add_book(book_id, title, author)

        elif choice == '2':
            book_id = input("Enter Book ID to update: ")
            title = input("Enter new title (or leave blank): ")
            author = input("Enter new author (or leave blank): ")
            update_book(book_id, title if title else None, author if author else None)

        elif choice == '3':
            book_id = input("Enter Book ID to delete: ")
            delete_book(book_id)

        elif choice == '4':
            keyword = input("Enter keyword to search books: ")
            search_books(keyword)

        elif choice == '5':
            list_books()

        elif choice == '6':
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            add_member(member_id, name)

        elif choice == '7':
            member_id = input("Enter Member ID to delete: ")
            delete_member(member_id)

        elif choice == '8':
            keyword = input("Enter keyword to search members: ")
            search_members(keyword)

        elif choice == '9':
            list_members()

        elif choice == '10':
            book_id = input("Enter Book ID to borrow: ")
            member_id = input("Enter Member ID: ")
            borrow_book(book_id, member_id)

        elif choice == '11':
            book_id = input("Enter Book ID to return: ")
            member_id = input("Enter Member ID: ")
            return_book(book_id, member_id)

        elif choice == '12':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 12.")

if __name__ == "__main__":
    main()
