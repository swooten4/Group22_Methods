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
        
        query = f"SELECT * FROM {self.tableName}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def search_inventory(self, isbn):

        try:
            connection = sqlite3.connect(self.database)
        except:
            print("Connection to users database failed")
            sys.exit()

        query = f"SELECT * FROM {self.tableName} WHERE ISBN = ?"
        self.cursor.execute(query, (isbn,))
        row = self.cursor.fetchone()
        if row:
            print(row)
        else:
            print("Book not found in inventory.")

    def decrease_stock(self, isbn):

        try:
            connection = sqlite3.connect(self.database)
        except:
            print("Connection to users database failed")
            sys.exit()

        query_check_stock = f"SELECT Stock FROM {self.tableName} WHERE ISBN = ?"
        self.cursor.execute(query_check_stock, (isbn,))
        current_stock = self.cursor.fetchone()

        if current_stock:
            current_stock = current_stock[0]
            if current_stock > 0:
                new_stock = current_stock - 1
                query_update_stock = f"UPDATE {self.tableName} SET Stock = ? WHERE ISBN = ?"
                self.cursor.execute(query_update_stock, (new_stock, isbn))
                self.connection.commit()
                print(f"Stock for {isbn} decreased. New stock: {new_stock}")
            else:
                print(f"Sorry, {isbn} is out of stock.")
        else:
            print("Book not found in inventory.")

    def __del__(self):
        self.connection.close()