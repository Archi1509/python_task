class LibraryInventory:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, quantity):
        if title in self.books:
            self.books[title] = (author, self.books[title][1] + quantity)
        else:
            self.books[title] = (author, quantity)
        print(f'Book "{title}" added successfully.')

    def remove_book(self, title):
        try:
            if title in self.books:
                del self.books[title]
                print(f'Book "{title}" removed successfully.')
            else:
                raise KeyError("Book not found in inventory.")
        except KeyError as e:
            print(e)

    def update_book(self, title, author=None, quantity=None):
        try:
            if title in self.books:
                current_author, current_quantity = self.books[title]
                new_author = author if author else current_author
                new_quantity = quantity if quantity is not None else current_quantity
                self.books[title] = (new_author, new_quantity)
                print(f'Book "{title}" updated successfully.')
            else:
                raise KeyError("Book not found in inventory.")
        except KeyError as e:
            print(e)

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available Books:")
            for title, (author, quantity) in self.books.items():
                print(f'Title: {title}, Author: {author}, Quantity: {quantity}')

    def search_book(self, title):
        try:
            if title in self.books:
                author, quantity = self.books[title]
                print(f'Book Found - Title: {title}, Author: {author}, Quantity: {quantity}')
            else:
                raise KeyError("Book not found in inventory.")
        except KeyError as e:
            print(e)
if __name__ == "__main__":

    library = LibraryInventory()
    library.add_book("Python", "John Doe", 5)
    library.add_book("java", "Jane Smith", 3)
    library.display_books()
    library.search_book("Python")
    library.update_book("Python ", quantity=10)
    library.remove_book("java")
    library.display_books()
