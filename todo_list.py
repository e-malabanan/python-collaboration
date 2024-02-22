print("""   Enter:
              1. Add new task
              2. View all tasks
              3. Mark task as completed
              4. Delete task
              5. Exit""")

class to_do:
    def __init__(self):
        self.tasks = []
    
    def add(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                stat = "Done" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} - {stat}")
        else:
            print("To-Do list is empty.")
            
    def complete(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            print("Task is completed.")
        else:
            print("Invalid index.")
        
    def delete(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted.")
        else:
            print("Invalid index.")

def main():
    todo_list = to_do()

    while True:
        
        dec = input("Enter the option you would like to execute: ")

        if dec == '1':
            task = input("Enter new task:")
            todo_list.add(task)
        elif dec == '2':
            todo_list.view()
        elif dec == '3':
            index = int(input("Enter the task's index to mark as completed: "))
            todo_list.complete(index)
        elif dec == '4':
            index = int(input("Enter the task index you would like to delete: "))
            todo_list.delete(index)
        elif dec == '5':
            print("Done.")
            break
        else:
            print("Invalid choice.")


main()