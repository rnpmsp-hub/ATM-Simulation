import utils
def deposit():
    
    amount= float(input("enter the amount you want to deposit:"))
    if amount < 0:
        print("not valid input")
        return 0
    utils.money += amount
    print("deposite successfully")