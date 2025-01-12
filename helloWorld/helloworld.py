class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added to your to-do list.')

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty. Please include a task to your to-do list.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task["task"]}" removed from your to-do list.')
        else:
            print("Invalid task number. Please a number based on the view list.")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f'Task "{self.tasks[task_number - 1]["task"]}" marked as completed.')
        else:
            print("Invalid task number. Please a number based on the view list.")

def main():
    todo = ToDoList()
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task to add: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            task_number = int(input("Enter the task number to remove: "))
            todo.remove_task(task_number)
        elif choice == "4":
            todo.view_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            todo.mark_task_completed(task_number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
