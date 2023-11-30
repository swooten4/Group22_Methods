import sqlite3
import sys

class BookInventory:
    def __init__(self, databaseName = "", tableName = ""):
        self.database = databaseName
        self.table = tableName
    


    def view_inventory(self):

        try:
            connection = sqlite3.connect(self.database)
        except:
            print("Connection to users database failed")
            sys.exit()
        
        cursor = connection.cursor()

        query = f"SELECT * FROM {self.table}"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print("ISBN:", row[0])
            print("Title:", row[1])
            print("Author:", row[2])
            print("Genre:", row[3])
            print("Pages:", row[4])
            print("ReleaseDate:", row[5])
            print("Stock:", row[6])
            print()
        
        connection.close()

    def search_inventory(self):
        title = input("Enter the Title to search: ")

        try:
            connection = sqlite3.connect(self.database)
        except:
            print("Connection to users database failed")
            sys.exit()

        cursor = connection.cursor()

        query = f"SELECT * FROM {self.table} WHERE Title LIKE ?"
        cursor.execute(query, ('%' + title + '%',))
        result = cursor.fetchall()

        if result:
            for row in result:
                print("ISBN:", row[0])
                print("Title:", row[1])
                print("Author:", row[2])
                print("Genre:", row[3])
                print("Pages:", row[4])
                print("ReleaseDate:", row[5])
                print("Stock:", row[6])
                print()
        else:
            print("Book not found in inventory.")

        connection.close()

    def decrease_stock(self, isbn):

        try:
            connection = sqlite3.connect(self.database)
        except:
            print("Connection to users database failed")
            sys.exit()

        cursor = connection.cursor()

        query_check_stock = f"SELECT Stock FROM {self.table} WHERE ISBN = ?"
        cursor.execute(query_check_stock, (isbn,))
        current_stock = cursor.fetchone()

        if current_stock:
            current_stock = current_stock[0]
            if current_stock > 0:
                new_stock = current_stock - 1
                query_update_stock = f"UPDATE {self.table} SET Stock = ? WHERE ISBN = ?"
                cursor.execute(query_update_stock, (new_stock, isbn))
                connection.commit()
                print(f"Stock for {isbn} decreased. New stock: {new_stock}")
            else:
                print(f"Sorry, {isbn} is out of stock.")
        else:
            print("Book not found in inventory.")

        connection.close()
    