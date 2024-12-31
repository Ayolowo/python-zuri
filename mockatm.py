username = input("Enter your username: \n")

allowedUsers = ['Seyi', 'Mike', 'Love', 'Ayo']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove', 'passwordAyo']
userBalance = [10000, 20000, 30000, 40000]

if username in allowedUsers:
    password = input("Enter your password: \n")
    userId = allowedUsers.index(username)
    
    if password == allowedPassword[userId]:
        print("Welcome %s" % username)
        print("\nThese are the available options:")
        availableOptions = [1, 2, 3]
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")
        
        selectedOption = int(input("\nPlease select an option: "))
        
        if selectedOption == 1:
            withdrawalAmount = int(input("\nHow much would you like to withdraw? "))
            if withdrawalAmount <= userBalance[userId]:
                userBalance[userId] -= withdrawalAmount
                print("Take your cash")
                print("Your balance is %d" % userBalance[userId])
            else:
                print("Insufficient funds")
        
        elif selectedOption == 2:
            depositAmount = int(input("\nHow much would you like to deposit? "))
            userBalance[userId] += depositAmount
            print("Your balance is %d" % userBalance[userId])
        
        elif selectedOption == 3:
            complaint = input("\nWhat issue will you like to report? ")
            print("Thank you for contacting us, we will get back to you shortly")
            
        elif selectedOption != availableOptions:
            print("\nInvalid option selected, please try again")
    else:
        print("\nPassword incorrect, please try again")
else:
    print("\nUsername not found, please try again")