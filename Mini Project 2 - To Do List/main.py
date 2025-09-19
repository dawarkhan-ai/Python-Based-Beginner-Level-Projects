todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task(task):
    todo_list.append(task)
    print("Task added.")

def delete_task(position):
    if 0 < position <= len(todo_list):
        removed = todo_list.pop(position-1)
        print(f"Deleted: {removed}")
    else: 
        print("Invalid task number.")

while True:
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option(1-4): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '3':
        show_tasks()
        position = int(input("Enter ordered no. of task: "))
        delete_task(position)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
