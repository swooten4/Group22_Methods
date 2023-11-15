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
        print("-_-_- Log In -_-_-")
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
        self.UserID = cursor.fetchall()[0][0]

        connection.close()

        return self.isLoggedIn
       

    def logout(self):
       self.UserID = 0
       self.isLoggedIn = 0

       return self.isLoggedIn


    def createAccount(self):
        print("-_-_- Create Account -_-_-")
        try:
            connection = sqlite3.connect("shopping.db")
        except:
            print("Connection to users database failed")
            sys.exit()

        cursor = connection.cursor()

        # How I am handling UserID: literally just add 1 to the number of rows.
        # i.e. the first user is "1" and so on and so forth.
        cursor.execute("SELECT COUNT(UserID) FROM user")
        numRows = cursor.fetchall()
        userID = numRows[0][0] + 1

        # Email needs to be unique so that login can function properly. Plus, if they already have an
        # account, why let them make another?
        Email = input("What is your email? > ")
        cursor.execute(f'SELECT EXISTS(SELECT UserID from user WHERE Email = "{Email}")')
        isUnique = cursor.fetchall()[0][0]
        while(isUnique != 0):
            Email = input("A user exists with that email! Please input a different email! > ")
            cursor.execute(f'SELECT EXISTS(SELECT UserID from user WHERE Email = "{Email}")')
            isUnique = cursor.fetchall()[0][0]

        Password = input("What is your password? > ")
        FirstName = input("What is your first name? > ")
        LastName = input("What is your last name? > ")
        Address = input("What is your address? > ")
        City = input("What city do you live in? > ")
        State = input("What state do you live in? > ")

        Zip = int(input("What is your zip code? > "))
        while (len(str(Zip)) != 5):
            Zip = int(input("There should be 5 digits in a zip code. Please try again > "))

        Payment = input("What is your credit card number (Enter 16 digits with no spaces) > ")
        while (len(Payment) != 16):
            Payment = int(input("There should be 16 digits. Please try again > "))


        # insertion into the database table. Hooray!
        cursor.execute(f'INSERT INTO {self.table} (UserID, Email, Password, FirstName,\
                        LastName, Address, City, State, Zip, Payment)\
                        VALUES ("{userID}", "{Email}", "{Password}", "{FirstName}",\
                        "{LastName}", "{Address}", "{City}", "{State}", "{Zip}", "{Payment}")')

        connection.commit()

        connection.close()
    

    def viewAccountInformation(self):
        try:
            connection = sqlite3.connect("shopping.db")
        except:
            print("Connection to users database failed")
            sys.exit()

        cursor = connection.cursor()

        try:
            # Thank goodness this query returns data in the same order every time. 
            cursor.execute(f'SELECT * FROM user WHERE UserID = "{self.UserID}"')
            results = cursor.fetchall()
            print(f'UserID: {results[0][0]}')
            print(f'Email: {results[0][1]}')
            print(f'Password: {results[0][2]}')
            print(f'First Name: {results[0][3]}')
            print(f'Last Name: {results[0][4]}')
            print(f'Address: {results[0][5]}')
            print(f'City: {results[0][6]}')
            print(f'State: {results[0][7]}')
            print(f'Zip Code: {results[0][8]}')
            print(f'Credit Card Number: {results[0][9]}')
        except:
            print("Error! User is not in the database!")

        connection.close()

    def getUserID(self):
        return self.UserID

    def getLoggedIn(self):
        return self.isLoggedIn
        
