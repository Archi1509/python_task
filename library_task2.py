from datetime import date
import library_task1
class LibraryBorrowBooks:
    def __init__(self):
        self.borrow_books_data={}
        self.books={}
    # def add_book(self, title, author, quantity):
    #     if title in self.books:
    #         self.books[title] = (author, self.books[title][1] + quantity)
    #     else:
    #         self.books[title] = (author, quantity)
    #     print(f'Book "{title}" added successfully.')

    def borrow_book(self,username,title,borrowdate,duedate):
        if username in self.borrow_books_data and len(self.borrow_books_data[username])>=2:
            print(f"{username} have already borrowed 2 books.")
            return

        if title in self.books and self.books[title][1]>0:
            self.books[title] = (self.books[title][0], self.books[title][1] - 1)
            if username not in self.borrow_books_data:
                self.borrow_books_data[username] = {}
            self.borrow_books_data[username][title] = (borrowdate, duedate)
            print(f'Book "{title}" borrowed by {username}.')
        else:
            print(f'Book "{title}" is not available.')

    def return_book(self,username,title):
        if username in self.borrow_books_data and title in self.borrow_books_data[username]:
            del self.borrow_books_data[username][title]  # Remove from borrowed list
            if not self.borrow_books_data[username]:  # Clean up empty user records
                del self.borrow_books_data[username]

            if title in self.books:
                self.books[title] = (self.books[title][0], self.books[title][1] + 1)  # Increase quantity
            else:
                print(f'Error: {title} was not originally in the library.')

            print(f'Book "{title}" returned successfully by {username}.')
        else:
            print(f'Error: {username} did not borrow "{title}".')

    def display_borrowed_books(self):
        if not self.borrow_books_data:
            print("No books are currently borrowed.")
        else:
            for username, books in self.borrow_books_data.items():
                for title, (borrowdate, duedate) in books.items():
                    print(f'Username: {username}, Title: {title}, BorrowDate: {borrowdate}, DueDate: {duedate}')
    def track_due_date(self):
        for user,book in self.borrow_books_data.items():
            for title,(borrowdate,duedate) in book.items():
                if duedate>date.today():
                    print(f"Your book is overdue!{duedate}")
                else:
                    print(f"You could keep the book till {duedate}")
library = LibraryBorrowBooks()
task1=library_task1.LibraryInventory()
task1.add_book("Python Programming","John Andrew",3)
task1.add_book("Data Science", "Jane Smith", 2)
task1.add_book("Machine Learning", "Andrew Ng", 2)

library.borrow_book("Archi","Data Science",date(2025,2,25),date(2025,3,1))
library.borrow_book("Archi","Machine Learning",date(2025,2,25),date(2025,3,1))
library.borrow_book("Archi","Data Science",date(2025,2,25),date(2025,3,1))

library.display_borrowed_books()
library.track_due_date()
library.return_book("Archi","Data Science")














