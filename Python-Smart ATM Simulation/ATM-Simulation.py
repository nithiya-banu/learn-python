pin_number = 123456
username = str(input("Enter your username:"))
balance = 10
user_pin = int(input("Enter your 6 digit pin number:"))

if user_pin != pin_number:
    print("Invalid Pin")
else:
    print(f"\n Welcome {username}!")   
    print("\n")
    while True:
        print(f"-------ATM Menu-------")
        print(f"1. Check Balance")
        print(f"2. Deposit Money")
        print(f"3. Withdraw Money")
        print(f"4. Exit")
        print(f"----------------------")
        print("\n")
        user_choice = int(input("Enter the Option no. from the menu:"))
        

        if user_choice == 1:
            print("Account Balance: Rs.",balance)
            print("\n")
            user_enter = str(input("Go to menu [Yes/No]:"))
            print("\n")
            if user_enter == "Yes" or user_enter =="yes":
                continue
            else:
                print("Successfully exited! Thank You for using our ATM, Visit us Again!")
                break
        elif user_choice == 2:
            deposit_amount = int(input("Enter Amount:"))
            balance = balance + deposit_amount
            print(f"\nRs.{deposit_amount} Deposited Successfully!,\nCurrent Balance:Rs.{balance}")
            print("\n")
            user_enter = str(input("Go to menu [Yes/No]:"))
            print("\n")
            if user_enter == "Yes" or user_enter =="yes":
                continue
            else:
                print("Successfully exited! Thank You for using our ATM, Visit us Again!")
                break
        elif user_choice == 3:
            withdrawal_amount = int(input("Enter Amount:"))
            if withdrawal_amount <= balance and balance > 500:
                balance = balance - withdrawal_amount
                print(f"Rs.{withdrawal_amount} Debited. \nCurrent Balance: Rs.{balance}")
                user_enter = str(input("Go to menu [Yes/No]:"))
                print("\n")
                if user_enter == "Yes" or user_enter =="yes":
                    continue
                else:
                    print("Successfully exited! Thank You for using our ATM, Visit us Again!")
                    break
            elif withdrawal_amount >= balance or balance <= 500:
                print("Insufficient Balance")
                user_enter = str(input("Go to menu [Yes/No]:"))
                print("\n")
                if user_enter == "Yes" or user_enter =="yes":
                    continue
                else:
                    print("Successfully exited! Thank You for using our ATM, Visit us Again!")
                    break
            else:
                print("Invalid Number")
                user_enter = str(input("Go to menu [Yes/No]:"))
                print("\n")
                if user_enter == "Yes" or user_enter =="yes":
                    continue
                else:
                    print("Successfully exited! Thank You for using our ATM, Visit us Again!")
                    break
        elif user_choice == 4:
            print("Successfully exited! Thank You for using our ATM, Visit us Again!")
            break
        else:
            print("Kindly enter only the option no. from the menu")
            user_enter = str(input("Go to menu [Yes/No]:"))
            print("\n")
            if user_enter == "Yes" or user_enter =="yes":
                continue
            else:
                print("Successfully exited! Thank You for using our ATM, Visit us Again!")
                break