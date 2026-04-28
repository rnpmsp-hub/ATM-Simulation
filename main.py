from deposit_money import deposit
from show_balance import show
from withdraw_money import withdraw

def ATM():
    while True:
        print("\n1.deposite money")
        print("2.show money")
        print("3.withdraw money")
        print("4.Exit")
        choice = int(input("Enter your choice:"))

        if choice==1:
            deposit()
        elif choice==2:
            show()
        elif choice==3:
            withdraw()
        elif choice==4:
            print("thank you for visit")
            break
        else:
            print("invalid choice")
ATM()

