##CART CLASS##
import sqlite3
import sys

class cart:
    
    def __init__(self, databaseName, tableName):
        self.database = databaseName
        self.table = tableName
        
    def viewCart(self, userID, inventoryDatabase):
    ##VIEWfor loop to repeat through have many items there are select from cart ISBN andQuantity userid=to [person looged in]
        try: 
            connection = sqlite3.connect("shopping.db")
        except:
            print("Error: Connection to database failed")
            sys.exit()
        cursor = connection.cursor()
            
        try:
            cursor.execute(f'SELECT * FROM cart WHERE)
            results = cursor.fetchall()
            print("userID:",row[0])
            print("ISBN:",row[1])
            print("Quantity",row[2])
            
        except:
            print("Error: Cart does not exist")
            
        connection.close()
        
    def addItem(self, userID, isbn):
        try: 
            connection = sqlite3.connect("shopping.db")
        except:
            print("Error: Connection to database failed")
            sys.exit()
        cursor = connection.cursor()
        ##INSERT week 8 videos 
        cursor.execute("INSERT INTO cart(userID, ISBN, Quantity) VALUES ('','','')")
        connection.commit()
        
        print(cursor.rowcount, "table  updated")
        print()
        
        connection.close()
            
    def removeItem(self, userID, isbn):
        try:
            connection = sqlite3.connect("shopping.db")
            print("SUCCESS")
        except:
            print("failed connection")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM cart WHERE Quantity=' '")
        
        connection.commit()
        
        print(cursor.rowcount,"item deleted")
        print()
    
    def checkOut(self, userID):
        ##atler invertory and cart to checkout
        try:
            connection = sqlite3.connect("databaseName.db")
            print("Connected")
        except:
            print("Failed")
            sys.exit()
            print()
            
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT USBN, Quantity FROM cart WHERE userID = 'something'")
            result = cursor.fetchall()
            for row in result:
                Inventory.decreaseStock(ISBN, Quantity)
                query = "DELETE FROM cart WHERE userID = ?"
                data = ("userID Number",)
                cursor.execute(query, data)
        except:
            print("Cart is empty")
            sys.exit()
            print()
        
        cursor = connection.cursor
        connection.commit()
        
        cursor.closr()
        connection.close()
        
        inventory = Inventory()
        
        inventory.checkOut('your_user_id')
        
        
        
        ++++++++++++++++++++++++++++++++++++++++++++