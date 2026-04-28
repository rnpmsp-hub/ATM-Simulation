import utils
def withdraw():
    amount= float(input("enter the amount you want to withdraw:"))
    if amount>utils.money:
        print("not enuff money")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    utils.money -= amount
    print("withdraw successful")
