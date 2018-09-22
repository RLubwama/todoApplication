todo_list = []
finished =[]

tasks = input("Enter an item:")

def create_task(task):
    for task in todo_list:
        todo_list.append(task)
        return create_task

def delete_task(task):
    tsk = input("Enter task to delete:")
    for task in todo_list:
        delete = todo_list.pop()
        return delete_task

def mark_as_finished(task):
    if task in todo_list:
        finished.append(task) + ("finished")
        return mark_as_finished

def delete_all_task():
    

 





        


