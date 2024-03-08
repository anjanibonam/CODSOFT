class ToDoItem:
  """Represents a single task in the To-Do List."""

  def __init__(self, title, status="pending"):
    """Initializes a new ToDoItem object.

    Args:
        title: The title of the task.
        status (str, optional): The initial status of the task (default: "pending").
    """
    self.title = title
    self.status = status

  def set_incomplete(self):
    """Sets the task status to "pending" (incomplete)."""
    self.status = "pending"


class ToDoList:
  """Represents a collection of ToDoItem objects."""

  def __init__(self):
    """Initializes a new ToDoList object."""
    self.items = []

  def add_item(self, item):
    """Adds a new ToDoItem to the list.

    Args:
        item: The ToDoItem object to add.
    """
    self.items.append(item)

  def update_item_status(self, title, new_status):
    """Updates the status of a specific task by title.

    Args:
        title: The title of the task to update.
        new_status: The new status for the task.

    Returns:
        bool: True if the status is updated successfully, False otherwise.
    """
    for item in self.items:
      if item.title == title:
        item.status = new_status
        return True
    return False

  def display_items(self):
    """Prints all tasks in the list with their titles and statuses."""
    if not self.items:
      print("No tasks in the To-Do List.")
    else:
      for item in self.items:
        print(f"{item.title} - Status: {item.status}")

  def remove_item(self, title):
    """Removes a specific task by title from the list.

    Args:
        title: The title of the task to remove.

    Returns:
        bool: True if the task is removed successfully, False otherwise.
    """
    for i, item in enumerate(self.items):
      if item.title == title:
        del self.items[i]
        return True
    return False


def main():
  """Runs the main To-Do List application."""
  todo_list = ToDoList()

  while True:
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. Update Task Status")
    print("3. Display Tasks")
    print("4. Mark Task Incomplete")
    print("5. Remove Task")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
      task_name = input("Enter task title: ")
      new_task = ToDoItem(task_name)  # Pass argument to constructor
      todo_list.add_item(new_task)
      print("Task added successfully!")

    elif choice == "2":
      task_name = input("Enter task title: ")
      new_status = input("Enter new status (pending/completed): ")
      if todo_list.update_item_status(task_name, new_status):
        print("Task status updated successfully!")
      else:
        print("Task not found!")

    elif choice == "3":
      todo_list.display_items()

    elif choice == "4":
      task_name = input("Enter task title to mark incomplete: ")
      if todo_list.update_item_status(task_name, "pending"):
        print("Task marked incomplete successfully!")
      else:
        print("Task not found!")

    elif choice == "5":
      task_name = input("Enter task title to remove: ")
      if todo_list.remove_item(task_name):
        print("Task removed successfully!")
      else:
        print("Task not found!")

    elif choice == "6":
      print("Exiting the To-Do List application. Goodbye!")
      break

    else:
      print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
  main()