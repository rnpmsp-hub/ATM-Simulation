from deposit_money import deposit
from show_balance import show
from withdraw_money import withdraw

def ATM():
    while True:
        print("\n1.Add money")
        print("2.Check balance")
        print("3.Withdraw Cash")
        print("4.Exit ATM")
        choice = int(input("Enter your choice:"))

        if choice==1:
            deposit()
        elif choice==2:
            show()
        elif choice==3:
            withdraw()
        elif choice==4:
            print("Thank you for using our ATM")
            break
        else:
            print("Please enter a valid choice")
ATM()

