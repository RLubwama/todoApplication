todo_list = []
finished =[]

def create_task(tasks):
    task = input("Enter an item:")
    #for task in todo_list:
    if task not in todo_list:
        todo_list.append(task)
        return todo_list

        
def delete_task(task):
    task = input("Enter task to delete:")
    if task in todo_list == task:
        todo_list.pop(task)
        return todo_list

def mark_as_finished(task):
    if task in todo_list:
        finished.append(task) + ("finished")
        return finished

def delete_all_tasks(task):
    todo_list.clear()
    print("You have deleted all tasks")
    

 





        


