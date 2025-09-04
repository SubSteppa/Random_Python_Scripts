def main():
    tasks = []  # list to store tasks

    while True:
        # Menu options
        print("\n--- Main Menu ---")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Mark Tasks As Finished")
        print("4. Exit App")

        choice = input("Enter Choice: ")

        if choice == '1':
            # Add tasks
            task_name = input("Enter the task: ")
            tasks.append({"task": task_name, "done": False})
            print("Task Added!")

        elif choice == '2':
            # View tasks
            print("\nTasks:")
            if not tasks:
                print("No tasks yet.")
            else:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            # Mark tests as complete
            if not tasks:
                print("No tasks to mark as done.")
            else:
                tasks_index = int(
                    input("Enter the task number to mark as done: ")) - 1
                if 0 <= tasks_index < len(tasks):
                    tasks[tasks_index]["done"] = True
                    print("Task marked as done!")
                else:
                    print("Invalid task number.")

        elif choice == '4':
            # Exit program
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
main()
