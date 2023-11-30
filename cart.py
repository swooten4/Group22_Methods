##CART CLASS##
import sqlite3
import sys
from Inventory import BookInventory

class cart:
    
    def __init__(self, databaseName, tableName):
        self.database = databaseName
        self.table = tableName
        
    def viewCart(self, userID, inventoryDatabase):
    ##VIEWfor loop to repeat through have many items there are select from cart ISBN andQuantity userid=to [person looged in]
        try: 
            connection = sqlite3.connect(self.database)
        except:
            print("Error: Connection to database failed")
            sys.exit()
        cursor = connection.cursor()
    ## WEEK 7
        query = f"SELECT * FROM {inventoryDatabase} WHERE ISBN in (SELECT ISBN FROM cart WHERE userID = ?)"
        cursor.execute(query,(userID,))
        results = cursor.fetchall()

        if results:
            for row in results:
                print("ISBN:", row[0])
                print("Title:", row[1])
                print("Author:", row[2])
                print("Genre:", row[3])
                print("Pages:", row[4])
                print("ReleaseDate:", row[5])
                print("Stock:", row[6])
                print()
            
        else:
            print("Error: Cart does not exist")
            
        connection.close()
        
    def addItem(self, userID, isbn):
        try: 
            connection = sqlite3.connect(self.database)
        except:
            print("Error: Connection to database failed")
            sys.exit()
        cursor = connection.cursor()
        quantity = int(input("Preferred quantity of this item:"))
        ##INSERT week 8 videos 
        ##FIX ME
        query = "INSERT INTO cart (userID, ISBN, Quantity) VALUES (?, ?, ?)"
        cursor.execute(query, (userID, isbn, quantity))
        connection.commit()
        
        print(cursor.rowcount, "table  updated")
        print()
        
        connection.close()
            
    def removeItem(self, userID, isbn):
        try:
            connection = sqlite3.connect(self.database)
            ##print("SUCCESS")
        except:
            print("failed connection")
            
        cursor = connection.cursor()
        cursor.execute("DELETE FROM cart WHERE ISBN = ? AND userID = ?'", (isbn, userID))
        
        connection.commit()
        
        print(cursor.rowcount,"item deleted")
        print()
        ##quantity-1 print statement 
    
    def checkOut(self, userID):
        ##atler invertory and cart to checkout
        try:
            connection = sqlite3.connect(self.database)
            print("Connected")
        except:
            print("Failed")
            sys.exit()
            print()
            
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cart")
        results = cursor.fetchall()
        inventory = BookInventory()
        
        if result:
            for row in result:
                isbn = row[0]
                quantity = row[1]
                    
                for i in range(quantity):
                    inventory.decrease_stock(isbn)

            query = "DELETE FROM cart WHERE userID = ?"
            data = (userID)
            cursor.execute(query, data)
            connection.commit()

        else:
            print("Cart is empty")
        
        print("Checkout is complete")
        
        connection.close()
        
        
        
        
        ++++++++++++++++++++++++++++++++++++++++++++
