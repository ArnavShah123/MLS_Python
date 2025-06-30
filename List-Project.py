tasks = []

def add_task():
    task = input("What task do you want to add? ").strip()
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append(task)
    print(f"'{task}' has been added to your list.")

def show_task():
    if tasks:
        print("\nYour Tasks:")
        for count, task in enumerate(tasks, 1):
            print(f"{count}. {task}")
    else:
        print("No tasks are added.")

def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return
    show_task()
    try:
        remove1 = int(input("Enter the task number you want to remove: "))
        if remove1 in range(1, len(tasks) + 1):
            a = tasks.pop(remove1 - 1)
            print(f"'{a}' was removed successfully.")
        else:
            print("Enter a valid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_complete():
    if not tasks:
        print("No tasks to mark complete.")
        return
    show_task()
    try:
        complete = int(input("Enter the task number you completed: "))
        if complete in range(1, len(tasks) + 1):
            task = tasks[complete - 1]
            if task.endswith("✔"):
                print("This task is already marked as complete.")
            else:
                tasks[complete - 1] = task + " ✔"
                print(f"Task {complete} marked as complete.")
        else:
            print("Enter a valid task number.")
    except ValueError:
        print("Please enter a valid number.")

def choice():
    print("\n------ Task Manager ------")
    print("Choose 1 to Add a Task")
    print("Choose 2 to Show Tasks")
    print("Choose 3 to Remove a Task")
    print("Choose 4 to Mark Task as Complete")
    print("Choose 5 to Exit\n")

choice()
while True:
    try:
        i = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number (1–5).")
        continue

    if i == 1:
        add_task()
        print("--------")
    elif i == 2:
        show_task()
        print("--------")
    elif i == 3:
        remove_task()
        print("--------")
    elif i == 4:
        mark_task_complete()
        print("--------")
    elif i == 5:
        print("Bye!")
        break
    else:
        print("Enter a valid choice from 1–5.")