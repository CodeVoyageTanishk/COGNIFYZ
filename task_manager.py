class Task:
    def __init__(self, task_id, description, status):
        self.task_id = task_id
        self.description = description
        self.status = status
    def __str__(self):
        return f"Task ID: {self.task_id}, Description: {self.description}, Status: {self.status}"
class TaskManager:
    def __init__(self):
        self.tasks = []
    def create_task(self, task_id, description, status):
        task = Task(task_id, description, status)
        self.tasks.append(task)
        print("Task created successfully!")
    def read_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)
    def update_task(self, task_id, new_description, new_status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.description = new_description
                task.status = new_status
                print("Task updated successfully!")
                return
        print("Task not found.")
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task not found.")
def main():
    task_manager = TaskManager()
    while True:
        print("\n===== Task Manager Menu =====")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            task_id = int(input("Enter Task ID: "))
            description = input("Enter Description: ")
            status = input("Enter Status: ")
            task_manager.create_task(task_id, description, status)
        elif choice == "2":
            print("\n===== List of Tasks =====")
            task_manager.read_tasks()
        elif choice == "3":
            task_id = int(input("Enter Task ID to update: "))
            new_description = input("Enter New Description: ")
            new_status = input("Enter New Status: ")
            task_manager.update_task(task_id, new_description, new_status)
        elif choice == "4":
            task_id = int(input("Enter Task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()
