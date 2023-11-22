class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_book(self, isbn, title, author, genre, pages, release_date, stock, price):
        if isbn in self.inventory:
            print(f"Book with ISBN {isbn} already exists in the inventory.")
        else:
            self.inventory[isbn] = {
                'Title': title,
                'Author': author,
                'Genre': genre,
                'Pages': pages,
                'ReleaseDate': release_date,
                'Stock': stock,
                'Price': price
            }
            print(f"Book with ISBN {isbn} added to the inventory.")

    def get_book_info(self, isbn):
        if isbn in self.inventory:
            return self.inventory[isbn]
        else:
            print(f"Book with ISBN {isbn} not found in the inventory.")
            return None

    def update_stock(self, isbn, new_stock):
        if isbn in self.inventory:
            self.inventory[isbn]['Stock'] = new_stock
            print(f"Stock for book with ISBN {isbn} updated to {new_stock}.")
        else:
            print(f"Book with ISBN {isbn} not found in the inventory.")

    def remove_book(self, isbn):
        if isbn in self.inventory:
            del self.inventory[isbn]
            print(f"Book with ISBN {isbn} removed from the inventory.")
        else:
            print(f"Book with ISBN {isbn} not found in the inventory.")

    def get_all_books(self):
        return self.inventory

# Example Usage:
inventory = Inventory()

# Add books to the inventory
inventory.add_book(123456789, "Sample Book 1", "John Doe", "Fiction", "300", "2023-01-01", 10, 19.99)
inventory.add_book(987654321, "Sample Book 2", "Jane Smith", "Non-Fiction", "250", "2023-02-01", 15, 29.99)

# Get information about a specific book
book_info = inventory.get_book_info(123456789)
print("Book Info:", book_info)

# Update stock for a book
inventory.update_stock(123456789, 15)

# Remove a book from the inventory
inventory.remove_book(987654321)

# Get information about all books in the inventory
all_books = inventory.get_all_books()
print("All Books:", all_books)