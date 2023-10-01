class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ToDoList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def view_tasks(self):
        if not self.head:
            print("No tasks in the to-do list.")
        else:
            current = self.head
            print("To-Do List:")
            while current:
                print(current.data)
                current = current.next

    def update_task(self, old_task, new_task):
        if not self.head:
            print("No tasks in the to-do list.")
            return

        current = self.head
        while current:
            if current.data == old_task:
                current.data = new_task
                print(f"Updated task '{old_task}' to '{new_task}'.")
                return
            current = current.next

    def remove_task(self, task):
        if not self.head:
            print("No tasks in the to-do list.")
            return

        if self.head.data == task:
            self.head = self.head.next
            print(f"Removed task: '{task}'")
            return

        current = self.head
        while current.next:
            if current.next.data == task:
                current.next = current.next.next
                print(f"Removed task: '{task}'")
                return
            current = current.next

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Update a task")
        print("4. Remove a task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("\nEnter the task: ")
            todo_list.add_task(task)
            print("\tTASK ADDED\n\n")
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            old_task = input("\nEnter the task to update: ")
            new_task = input("\nEnter the new task: ")
            todo_list.update_task(old_task, new_task)
            print("\tTASK UPDATED!\n\n")
        elif choice == "4":
            task = input("\nEnter the task to remove: ")
            todo_list.remove_task(task)
            print("\tTASK REMOVED!\n\n")
        elif choice == "5":
            print("\nExiting the to-do list application. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()