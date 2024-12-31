username = input("Enter your username: \n")

allowedUsers = ['Seyi', 'Mike', 'Love', 'Ayo']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove', 'passwordAyo']
userBalance = [10000, 20000, 30000, 40000]

if username in allowedUsers:
    password = input("Enter your password: \n")
    userId = allowedUsers.index(username)
    
    if password == allowedPassword[userId]:
        print("Welcome %s" % username)
        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")
        
        selectedOption = int(input("Please select an option: "))
        
        if selectedOption == 1:
            withdrawalAmount = int(input("How much would you like to withdraw? "))
            if withdrawalAmount <= userBalance[userId]:
                userBalance[userId] -= withdrawalAmount
                print("Take your cash")
                print("Your balance is %d" % userBalance[userId])
            else:
                print("Insufficient funds")
        
        elif selectedOption == 2:
            depositAmount = int(input("How much would you like to deposit? "))
            userBalance[userId] += depositAmount
            print("Your balance is %d" % userBalance[userId])
        
        elif selectedOption == 3:
            complaint = input("What issue will you like to report? ")
            print("Thank you for contacting us")
    else:
        print("Password incorrect, please try again")
else:
    print("Username not found, please try again")