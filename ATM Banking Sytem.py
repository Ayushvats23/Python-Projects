print("------------Wecome to ATM Banking System------------")

Name = input("Enter your full name :")
Account_number = input("Enter your account number :")
balance = 10000
pin = 1234

entered_pin = int(input("Please enter pin of 4 digits :"))

if entered_pin == pin:
    print("\nLogin Successfully")

    while  True:
        print("\n--------------------Menu--------------------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change Pin")
        print("5. Mini Statement")
        print("6. Exit")

        choice = int(input("\n Enter your choice : "))

        if choice == 1:
            print("Your available Balance is : ₹", balance)

        elif choice == 2:
            amount = float(input("Enter the amount you want to deposit:"))

            if amount > 0 :
                balance = amount + balance
                print("₹",amount ,"deposited successfully")
                print("updated balance is ₹",balance)
            else:
                print("Enter valid amount to be deposited")

        elif choice == 3:
            amount = float(input("Enter the amount yo want to withdraw : ₹"))

            if amount <= balance and amount > 0:
                balance = balance-amount
                print("Please collect your cash : ₹",amount)
                print("updated balance is ₹", balance)

            elif amount > balance:
                print("Insufficicent balance")
            else :
                print("Invalid amount")

        elif choice == 4:
            old_pin = int(input("Enter the old pin"))

            if old_pin == pin:
                new_pin = int(input("Enter the new 4 digit pin:"))
                confirm_pin = int(input("Re-enter the new pin:"))

                if new_pin == confirm_pin:
                    pin = new_pin
                    print("Pin changed successfully")

                else:
                    print("Pin doesnot match!")

            else:
                    print("Incorrect old pin! ")

        elif choice == 5:
           print("\n========== MINI STATEMENT ==========")
           print("Account Holder : ",Name)
           print("Account Number : ", Account_number)
           print("Current Balance: ₹", balance)
           print("Thank you for banking with us!")

        elif choice == 6:
            print("\nThankyou for banking with python ATM")
            print("Please visit again!")
            break
        else:
            print("Invalid Choice! Please Try Again.")

else:
    print("\nIncorrect PIN!")
    print("Access Denied!")

