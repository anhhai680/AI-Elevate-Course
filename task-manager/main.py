tasks = []

# Simple Task Manager Application
def add_task(description):
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    task = {"id": task_id, "description": description, "completed":
    False}
    tasks.append(task)
    print(f"Task '{description}' added with ID {task_id}.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {status}")

def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task ID {task_id} marked as completed.")
            return
    print(f"Task ID {task_id} not found.")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    print(f"Task ID {task_id} deleted.")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to complete: "))
            complete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()