## Choices to be selected.
def display_menu():
    print("\nMenu: ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. View Completed Tasks")
    print("5. Exit\n")
    
def add_task(tasks):
    task = input("Enter task description: ")
    if task = '':
        print("You have entered nothing.Please write something to add to Task List.")
        add_task(tasks)
    else:
        tasks.append(task)
        print("Task added.\n")
    
    
def view_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
        
def mark_as_done(tasks, completed):
    view_tasks(tasks)
    index = int(input("Enter index number of the Task to mark as done: "))-1
    removed_item = tasks.pop(index)
    completed.append(removed_item)
    
def view_completed(completed):
    for i,task in enumerate(completed, start=1):
        print(f"{i}. {task} is completed.")
        
        
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