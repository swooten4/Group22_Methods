##### user class ####
import sqlite3
import sys

class user:
    def __init__(self, databaseName = "", tableName = ""):
        self.database = databaseName
        self.table = tableName
        self.UserID = 0
        self.isLoggedIn = 0

    def login(self):
        email = input("What is your email? > ")
        password = input("What is your password? > ")

        try:
            connection = sqlite3.connect(self.database)
        except:
            print("Connection to users database failed")
            sys.exit()

        cursor = connection.cursor()
        cursor.execute(f'SELECT EXISTS(SELECT * FROM {self.table} WHERE Email = "{email}" AND Password = "{password}")')
    
        # Takes the resulting boolean out of the list of tuples it exists in.
        self.isLoggedIn = cursor.fetchall()[0][0]

        # Prevents an error when getting the UserID. After all, if the user does not exist,
        # how are you supposed to fetch their ID? Stop here before that happens!
        if(self.isLoggedIn == 0):
            print("User does not exist. Check email and password.")
            return self.isLoggedIn

        cursor.execute(f'SELECT UserID FROM {self.table} WHERE Email = "{email}" AND Password = "{password}"')
        # Takes UserID out of the list of tuples and stores it as a class variable for later use!
        self.UserID = cursor.fetchall()[0][0]

        connection.close()

        return self.isLoggedIn
       
    def logout(self):
       self.UserID = 0
       self.isLoggedIn = 0

       return self.isLoggedIn

    def createAccount(self):
        try:
            connection = sqlite3.connect("shopping.db")
        except:
            print("Connection to users database failed")
            sys.exit()

        cursor = connection.cursor()

        userID = 0
        Email = input("What is your email? > ")
        Password = input("What is your password? > ")
        FirstName = input("What is your first name? > ")
        LastName = input("What is your last name? > ")
        Address = input("What is your address? > ")
        City = input("What city do you live in? > ")
        State = input("What state do you live in? > ")
        Zip = int(input("What is your zip code? > "))
        Payment = int(input("What is your credit card number (Enter 16 digits with no spaces) > "))

        cursor.execute(f'INSERT INTO user (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES ("{userID}", "{Email}", "{Password}", "{FirstName}", "{LastName}", "{Address}", "{City}", "{State}", "{Zip}", "{Payment}")')
        connection.commit()

        connection.close()