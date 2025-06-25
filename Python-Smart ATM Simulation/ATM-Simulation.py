pin_number = 123456
username = str(input("Enter your username:"))
balance = 10
user_pin = int(input("Enter your 6 digit pin number:"))

if user_pin != pin_number:
    print("Invalid Pin")
else:
    print(f"\n Welcome {username}!")   
    
    while True:
        print(f"-------ATM Menu-------")
        print(f"1. Check Balance")
        print(f"2. Deposit Money")
        print(f"3. Withdraw Money")
        print(f"4. Exit")
            
        user_choice = int(input("Enter the Option no. from the menu:"))
        
        if user_choice == 1:
            print("Account Balance: Rs.",balance)
            continue
        elif user_choice == 2:
            deposit_amount = int(input("Enter Amount:"))
            balance = balance + deposit_amount
            print(f"Rs.{deposit_amount} Deposited Successfully!,Current Balance:Rs.{balance}")
            continue
        elif user_choice == 3:
            withdrawal_amount = int(input("Enter Amount:"))
            if withdrawal_amount <= balance and balance > 500:
                balance = balance - withdrawal_amount
                print("Amount Debited","Current Balance: Rs.",balance)
                continue
            elif withdrawal_amount >= balance or balance <= 500:
                print("Insufficient Balance")
                continue
            else:
                print("Invalid Number")
                continue
        elif user_choice == 4:
            print("Successfully exited! Thank You for using our ATM, Visit us Again!")
            break
        else:
            print("Kindly enter only the option no. from the menu")
            continue