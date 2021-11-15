#Gaven Romine
#EZbank 1
import basics

app = basics.newProgram()

user = basics.newUser()

app.balance = 1000

while app.running:
    print(app.balance)
    user.choice = input("withdraw 1, deposit 2, quit 3")
    if user.choice == "1":
        user.withdraw = input("how much would you like to withdraw")
        user.withdraw = int(user.withdraw)
        if user.withdraw > app.balance:
            print("You do not have enough money to withdraw")
        else:
            app.balance -= user.withdraw
    elif user.choice == "2":
        user.deposit = input("How much would you like to deposit")
        user.deposit = int(user.deposit)
        app.balance = (app.balance + user.deposit)
        print("here is your new balance:",app.balance)
    elif user.choice == "3":
        app.running = False
    else:
        print("that was not a choice, please select withdraw, deposit, quit ")
