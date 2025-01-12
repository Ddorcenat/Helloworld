class ToDoList:
    def __init__ (self):
        self.task = []

    def add_task (self, task):
        self.task.append({"task": task, "completed": False})
        print(f'Task "{task}" added to your to-do list. Feel free to proceed.')
        # Take peek at what is in your list of task.
    def view_tasks(self):
        if not self.tasks:  
            print("Your to-do list is empty Plaese add a task to your to-do list.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")
        #Remove section 
    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):  
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task["task"]}" removed from your to-do list.')
        else:
            print("Invalid task number. Please select a number from the display list.")
            # complete task
    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):  
            self.tasks[task_number - 1]["completed"] = True
            print(f'Task "{self.tasks[task_number - 1]["task"]}" marked as completed.')
        else:
            print("Invalid task number. Remember to select a number from the list. ")

    