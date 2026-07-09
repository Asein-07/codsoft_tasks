# -----------------------------
# Author: Asein
# Project: To-Do List
# -----------------------------

tasks = []

while True:
    print("\n=== TO-DO LIST ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available to update.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            num = int(input("Enter task number to update: "))

            if 1 <= num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            num = int(input("Enter task number to delete: "))

            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"'{removed}' deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")