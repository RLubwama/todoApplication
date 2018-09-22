# Here the user creates an account

accounts = {}

name = input("Please enter your name:")
password = input("Please enter your password:")

def add_account(name,password):

    accounts[password] = name

    return add_account

print("success!!")

def login(name,password):
    if accounts[password] == name:
        return True
    else:
         print("Opps! First register")



app = (__name__)

