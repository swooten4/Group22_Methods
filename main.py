from user import user
# add other statements to include finished classes later

user = user("shopping.db","user")

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
            print("placeholder!")

        # Another menu in this loop for cart interaction.
        else:
            print("placeholder!")
                
        


# when selecting logout on the outermost menu, the while loop is broken.
print()
print("Goodbye!")