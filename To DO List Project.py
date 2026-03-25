#project : TO DO LIST Import os

print("_ TO DO List _".center(60))

record = {}

# ---------------- MENU ----------------
def show():
    print("\nChoose 1 : Add task")
    print("Choose 2 : View tasks")
    print("Choose 3 : Save tasks and exit")
    print("Choose 4 : Delete task")


# ---------------- ADD TASK ----------------
def add_task(name, desc):
    record[name] = desc
    print("Task added successfully.")


# ---------------- LOAD TASK ----------------
def load_task():
    global record
    try:
        with open("task.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, desc = parts
                    record[name] = desc
    except FileNotFoundError:
        pass


# ---------------- VIEW TASK ----------------
def view_task():
    if not record:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, (name, desc) in enumerate(record.items(), start=1):
            print(f"{i}. {name} - {desc}")


# ---------------- SAVE TASK ----------------
def save_exit():
    with open("task.txt", "w") as file:
        for name, desc in record.items():
            file.write(f"{name},{desc}\n")

    print("Tasks saved successfully.")


# ---------------- DELETE TASK ----------------
def delete_task():
    if not record:
        print("No tasks to delete.")
        return

    view_task()
    task_name = input("Enter the task name to delete: ")

    if task_name in record:
        del record[task_name]
        print("Task deleted successfully.")
    else:
        print("Task not found.")


# ---------------- LOAD SAVED TASKS ----------------
load_task()


# ---------------- MAIN LOOP ----------------
while True:
    show()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        name = input("Enter your task name: ")
        desc = input("Enter the description of your task: ")
        add_task(name, desc)

    elif choice == 2:
        view_task()

    elif choice == 3:
        save_exit()
        break

    elif choice == 4:
        delete_task()

    else:
        print("Please enter a valid choice!")

