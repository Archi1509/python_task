

from datetime import datetime,timedelta,date


class LibrarySystem:
    def __init__(self):
        self.books={}
        self.borrowed_book={}
        self.reserved_book={}

    def add_book(self,title,author,quantity):
        if title in self.books:
            self.books[title]=(author,self.books[title][1]+quantity)
        else:
            self.books[title]=(author,quantity)
        print(f"{title} book added successfully.")

    def remove_book(self,title):
        if title in self.books:
            del self.books[title]
            print(f"{title} book removed successfully")
        else:
            print(f"No book with name {title} is available in library.")

    def update_book(self,title,author=None,quantity=1):
        if title in self.books:
            current_author, current_quantity = self.books[title]
            new_author = author if author else current_author
            new_quantity = quantity if quantity !=1 else current_quantity
            self.books[title] = (new_author, new_quantity)
            print(f'Book "{title}" updated successfully.')
        else:
            print(f"no such book {title} is found.")

    def display_book(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available Books:")
            for title, (author, quantity) in self.books.items():
                print(f'Title: {title}, Author: {author}, Quantity: {quantity}')

    def borrow_books(self,username,title,borrowdate=date.today()):
        if username in self.borrowed_book and len(self.borrowed_book[username]) >= 3:
            print(f"{username} have already borrowed 3 books.")
            return
        if title in self.books and self.books[title][1]>0:
            duedate = date.today() + timedelta(days=14)
            self.books[title]=(self.books[title][0], self.books[title][1] - 1)
            if username not in self.borrowed_book:
                self.borrowed_book[username] = {}
            self.borrowed_book.setdefault(username, {})[title] = (borrowdate, duedate)
            print(f'"{title}" borrowed by {username}. Due date: {duedate}')

        else:
            print(f'Book "{title}" is not available.')

    def return_books(self,username,title):
        if username in self.borrowed_book and title in self.borrowed_book[username]:
            del self.borrowed_book[username][title]
            if not self.borrowed_book[username]:
                del self.borrowed_book[username]
                if title in self.books:
                    self.books[title] = (self.books[title][0], self.books[title][1] + 1)  # Increase quantity
                else:
                    print(f'Error: {title} was not originally in the library.')

                print(f'Book "{title}" returned successfully by {username}.')
            else:
                print(f'Error: {username} did not borrow "{title}".')

    def overdue_books(self,today = None):

        overdue_books = []
        if today is None:
            today = datetime.today().date()
        for user,books in self.borrowed_book.items():
            for title, (borrowdate, duedate) in books.items():
                if today > duedate:
                    overdue_books.append((user, title, duedate))
        if not overdue_books:
            return "No overdue books."
        else:
            print("Overdue Books:")
            for user, title, duedate in overdue_books:
                print(f"User: {user}, Book: {title}, Due Date: {duedate}")

        print("Borrowed Books Data:", self.borrowed_book)

    def penalty_system(self,borrowdate):
        duedate = borrowdate + timedelta(days=14)
        today=datetime.today().date()
        if today>duedate:
            print(f"Overdue! The due date was {duedate}. You are {today - duedate} days late.")
        elif today == duedate:
            print(f"Today is the last day to return the book!")
        else:
            print(f"You still have time! The due date is {duedate}.")

    def reserve_book(self,user,title):
        if title in self.books:
            author, quantity = self.books[title]
            if quantity < 1:
                self.reserved_book.setdefault(title, []).append(user)
                print(f"{user} has reserved '{title}'.")
            else:
                print(f"'{title}' is available. No need to reserve.")
        else:
            print(f"'{title}' does not exist in the library.")

    def borrowing_history(self,username):
        if username in self.borrowed_book:
            print(f'Borrowing History for {username}: {self.borrowed_book[username]}')
        else:
            print(f'No borrowing history found for {username}.')

l1=LibrarySystem()
l1.add_book("Harry Potter","JK Rowling",3)
l1.add_book("Python","John",5)
l1.add_book("Java","James",6)
l1.add_book("Back Benchers","Sidhart",1)
l1.borrow_books("Archi","Harry Potter")
l1.remove_book("Back Benchers")
l1.update_book("Python","James")
l1.display_book()
l1.return_books("Archi","Python")
l1.return_books("Archi","Harry Potter")
l1.overdue_books()
l1.borrow_books("Ayush", "Java", datetime(2024, 1, 1).date())
l1.overdue_books()
l1.penalty_system(datetime(2025, 2, 1).date())
l1.borrowing_history("Ayush")
l1.borrowing_history("Archi")

l1.reserve_book("Aryan","Marvel")

#


