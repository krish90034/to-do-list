todo_list = []

#function to add a task
def add_task():
    task = input("enter your task")
    todo_list.append({"task":task,"status":"pending"})
    print("new task added successfully \n")

#function to view all tasks
def view_task():
    print("your to do list :")
    if len(todo_list) ==0:
        print("no tasks found")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index} : {task["task"]} - {task["status"]}")
            print("\n")

#fuction to remove a task 
def remove_task():
    if len(todo_list) == 0:
        print("no task found")
    else:
        try:

                search_index = int(input("enter the task no. that you want to remove = ")) - 1
                if 0 <= search_index < len(todo_list):
                    remove_task = todo_list.pop(search_index)
                    print(f"task removed : {remove_task}")
                else:
                    print("invalid task number, please try again")
        except ValueError:
            print("invalid input,please enter a number")
    
#function to mark a task as completed
def mark_task():
    if len(todo_list) == 0:
        print("no task found")
    else:
        try:
            search_index = int(input("enter the task no. that you want to mark as completed = ")) -1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]["status"] = "completed"
                print(f"task marked as completed : {todo_list[search_index]['task'] }")
            else:
                print("invalid task number, please try again")
        except ValueError:
            print("invalid input, please enter a number")
            

#function to display menu
def menu():
    while(True):
        print("***menu***")
        print("1. Add a new Task")
        print("2. View All Task ")
        print("3. Remove a Task")
        print("4. mark a Task")
        print("5.Exit")
        



        choice = int(input("enter your choice = "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            mark_task()
        elif choice == 5:
            print("exiting the program")
            exit()
        else:
            print("invalid choice please try again")


menu()
