from user import user
from Inventory import BookInventory
# add other statements to include finished classes later

user = user("shopping.db","user")
inventory = BookInventory("shopping.db", "inventory")

# First Menu
while(1):
    print("1. Login")
    print("2. Create Account")
    print("3. Logout")
    option = int(input("Please select an option. > "))

    while(option not in {1, 2, 3}):
        option = int(input("Please select a valid option. > "))

    if(option == 1):
        user.login()
        print()

    elif(option == 2):
        user.createAccount()
        print()

    else:
        break

    # Enter second menu upon successful login.
    while(user.getLoggedIn() == 1):
        
        print("Login successfuL!")
        print("1. Logout")
        print("2. View Account Information")
        print("3. Inventory Information")
        print("4. Cart Information")
        option = int(input("Please select an option > "))

        while(option not in {1, 2, 3, 4}):
            option = int(input("Please select a valid option. > "))

        if(option == 1):
            user.logout()
            print("Logged out!")

        elif(option == 2):
            user.viewAccountInformation()
            print()

        # Another menu for inventory interaction.
        elif(option == 3):
            print("1. View Inventory")
            print("2. Search Inventory")
            print("3. Go Back")
            inventory_option = int(input("Please select an option > "))

            while inventory_option not in {1, 2, 3}:
                inventory_option = int(input("Please select a valid option. > "))

            if inventory_option == 1:
                inventory.view_inventory()

            elif inventory_option == 2:
                inventory.search_inventory()

            else:
                break


        # Another menu in this loop for cart interaction.
        else:
            print("1. View Cart")
            print("2. Add Items to Cart")
            print("3. Remove an Item from Cart")
            print("4. Check Out")
            print("5. Go Back")
            cartChoice = int(input("Please select an option "))

            while (cartChoice != 1 or 2 or 3 or 4 or 5):
                cartChoice = int(input("Please select a vaild option "))
                
            if(cartChoice == 1):
                ID = user.getUserID()
                cart.viewCart(ID, "inventory")
                print()
                
            elif(cartChoice == 2):
                addUserChoice = int(input("Please enter the ISBN of the item you want added "))
                ID = user.getUserID()
                cart.addItem(ID, isbn)
                print()
        
            elif(cartChoice == 3):
                removeUserChoice = int(input("Please enter the ISBN of the item you want removed "))
                ID = user.getUserID()
                cart.removeItem(ID, isbn)
                print()
            
            elif(cartChoice == 4):
                ID = user.getUserID()
                cart.checkOut(ID)
                print()
            
            elif(cartChoice == 5):
                break
            

                
        


# when selecting logout on the outermost menu, the while loop is broken.
print()
print("Goodbye!")
