from user import user
from Inventory import BookInventory
from cart import cart
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
        print()
        user.login()

        if(user.getLoggedIn() == 1):
            print("Login successfuL!")

    elif(option == 2):
        user.createAccount()

    else:
        break

    # Enter second menu upon successful login.
    while(user.getLoggedIn() == 1):
        print()
        print("1. Logout")
        print("2. View Account Information")
        print("3. Inventory Information")
        print("4. Cart Information")
        option = int(input("Please select an option > "))

        while(option not in {1, 2, 3, 4}):
            option = int(input("Please select a valid option. > "))

        if(option == 1):
            user.logout()
            print("Logged out!\n")

        elif(option == 2):
            print("\nAccount Information:")
            user.viewAccountInformation()

        # Another menu for inventory interaction.
        elif(option == 3):
            while(1):
                print()
                print("1. View Inventory")
                print("2. Search Inventory")
                print("3. Go Back")
                inventory_option = int(input("Please select an option > "))

                while inventory_option not in {1, 2, 3}:
                    inventory_option = int(input("Please select a valid option. > "))

                if inventory_option == 1:
                    print("\nBooks in inventory:")
                    inventory.view_inventory()

                elif inventory_option == 2:
                    inventory.search_inventory()

                else:
                    break


        # Another menu in this loop for cart interaction.
        else:
            cart = cart("shopping.db","cart")
            while(1):
                print()
                print("1. View Cart")
                print("2. Add Items to Cart")
                print("3. Remove an Item from Cart")
                print("4. Check Out")
                print("5. Go Back")
                cartChoice = int(input("Please select an option > "))

                while cartChoice not in {1, 2, 3, 4, 5}:
                    cartChoice = int(input("Please select a vaild option > "))
                
                if(cartChoice == 1):
                    ID = user.getUserID()
                    print("\nItems currently in cart:")
                    cart.viewCart(ID, "inventory")
                
                elif(cartChoice == 2):
                    addUserChoice = int(input("Please enter the ISBN of the item you want added > "))
                    ID = user.getUserID()
                    cart.addItem(ID, addUserChoice)
        
                elif(cartChoice == 3):
                    removeUserChoice = int(input("Please enter the ISBN of the item you want removed > "))
                    ID = user.getUserID()
                    cart.removeItem(ID, removeUserChoice)
            
                elif(cartChoice == 4):
                    ID = user.getUserID()
                    cart.checkOut(ID)
            
                elif(cartChoice == 5):
                    break
                
        


# when selecting logout on the outermost menu, the while loop is broken.
print()
print("Goodbye!")