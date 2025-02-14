accounts = {
    1001 : [1000,2408,"user1@gmail.com","user1"],
    1002 : [2000,1234,"user2@gmail.com","user2"],
    1003 : [10000,None,"user3@gmail.com","user3"]
    }
print(accounts)
while True:
    print("*******************************")
    print("Choose your Option: ")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini Statement")
    print("5. Pin change")
    print("6. Exit")
    x = int(input("Enter Your Option: "))
    print("********************************")
    if x == 1:
        print("********************************")
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            if accounts[acc][1] is None:
                print(f"Dear {accounts[acc][3]}, Pin Not Genearted !")
            else:
                pin = int(input("Enter your Pin: "))
                if accounts[acc][1] == pin:
                    amt = int(input("Enter Amount: "))
                    if accounts[acc][0] >= amt:
                        accounts[acc][0] = accounts[acc][0]-amt
                        print("Amount Withdraw sucessfull !")
                        print(f"Balance: {accounts[acc][0]}")
                    else:
                        print("Insufficient Balance")
                else:
                    print("Invalid Pin !")
        print("********************************")
    elif x == 2:
        print("********************************")
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            amt = int(input("Enter Amount: "))
            accounts[acc][0] += amt
            print("Deposit Sucessfull !")
            print(f"Balance: {accounts[acc][0]}")
        print("********************************")
    elif x == 3:
        print("********************************")
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            if accounts[acc][1] is not None:
                print("Pin Already Generated !")
            else:
                pin = int(input("Enter New Pin: "))
                accounts[acc][1] = pin
                print("Pin Generated Sucessfully !")
        print("********************************")
    elif x == 4:
        print("********************************")
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            pin = int(input("Enter your Pin: "))
            if accounts[acc][1] == pin:
                print(f"Name: {accounts[acc][-1]}")
                print(f"Email: {accounts[acc][-2]}")
                print(f"Balance: {accounts[acc][0]}")
            else:
                print("Invalid Pin !")
        print("********************************")
    elif x == 5:
        print("********************************")
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            inp=input("Pin change request: Yes or NO?")
            if inp == "Yes":
                pin2=input("Enter Pin:")
                if len(pin2)==4:
                    accounts[acc][1] == pin2
                    print("Pin Changed Sucessfully !")
                    print(f"Pin: {pin2}")
                else:
                    print(f"pin: {accounts[acc][1]}")
                    print("Pin not changed!")
        print("********************************")
    elif x==6:
        print("*****************************")
        print("Thank You")
        print("Visit Again")
        print("*****************************")
        break
