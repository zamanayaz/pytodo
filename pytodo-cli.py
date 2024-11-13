 ## Choices (Options) to be selected.
def display_menu():
    print("\nMenu: ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. View Completed Tasks")
    print("5. Exit\n")

# Functions to add the tasks to the list.
def add_task(tasks):
    task = input("Enter task description: ")
    if task == '':
        print("You have entered nothing.Please write something to add to Task List.")
        add_task(tasks)
    else:
        tasks.append(task)
        print("Task added.\n")
    
#Function to view the tasks
def view_tasks(tasks):
    if len(tasks) >= 1:
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No Tasks to view.")

#Function to  transfer completed task from mail list to completed task list.
def mark_as_done(tasks, completed):
    view_tasks(tasks), print("\n")
    index = int(input("Enter index number of the Task to mark as done: "))
    if index in range(1, len(tasks) + 1):
        removed_item = tasks.pop(index - 1)
        completed.append(removed_item)
        print(f"The task ({index}.{removed_item}) is marked as done.")
    else:
        print("Index out of range.")
        if index == 0:
            print("Index should not be 0.")
        elif index < 0:
            print("Index should not be in negative.")
        else:
            print("Index should not exceed the length limit of tasks.")

#Function to view tasks from completed list.
def view_completed(completed):
    if len(completed) == 0:
        print("No tasks are completed.")
    else:
        for i,task in enumerate(completed, start=1):
            print(f"{i}. {task} is completed.")
        
#Main loop of the functions.
def main():
    tasks = []
    completed = []
    
    while True:
        display_menu()
        choice = input("Enter a choice from the menu: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_as_done(tasks, completed)
        elif choice == '4':
            view_completed(completed)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Enter a valid choice from given menu.")
if __name__ == "__main__":
    main()
