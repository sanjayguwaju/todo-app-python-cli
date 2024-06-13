class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def run(self):
        while True:
            print("\nTodo App")
            print("1. Add task")
            print("2. Remove task")
            print("3. View tasks")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                task = input("Enter a task: ")
                self.add_task(task)
            elif choice == "2":
                task = input("Enter a task to remove: ")
                self.remove_task(task)
            elif choice == "3":
                self.view_tasks()
            elif choice == "4":
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    TodoApp().run()