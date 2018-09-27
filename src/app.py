from account import add_account,login,accounts
from tasks import *
#name = input("Enter your name: ")
#password = input("Enter your Password: ")
#if name == accounts['name'] and password == accounts['password']:
if __name__ == "__main__":
    #print("yes")
    print("Select Option:")
    print("1: Create Task")
    print("2: Delete Task")
    print("3: Delete All Tasks")
    print("4: Mark All Tasks as Finished")

    selection = input("selection: ")
    #print(selection)

elif selection == "1":
        create_task(input("Add new task: "))
        print(todo_list)

elif selection == "2":
        delete_task(input("Remove Task: "))
        print(todo_list)

elif selection == "3":
        delete_task(input("Remove Task: "))
        print(todo_list)

elif selection == "4":
        delete_task(input("Remove Task: "))
        print(todo_list)
