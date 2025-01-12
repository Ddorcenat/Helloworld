class ToDoList:
    def __init__ (self):
        self.task = []

    def add_task (self, task):
        self.task.append({"task": task, "completed": False})
        print(f'Task "{task}" added to your to-do list. Feel free to proceed.')

    def view_tasks(self):
        if not self.tasks:  
            print("Your to-do list is empty Plaese add a task to your to-do list.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")

    