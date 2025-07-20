# Task Manager

A simple command-line task management application built with Python that allows users to create, view, complete, and delete tasks.

## Features

- **Add Tasks**: Create new tasks with unique descriptions
- **View Tasks**: Display all tasks with their current status (Pending/Completed)
- **Complete Tasks**: Mark tasks as completed by their ID
- **Delete Tasks**: Remove tasks from the list by their ID

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation

1. Clone or download this repository:
   ```bash
   git clone <repository-url>
   cd task-manager
   ```

2. Ensure you have Python 3.6+ installed:
   ```bash
   python --version
   ```

## Usage

Run the application using Python:

```bash
python main.py
```

### Menu Options

The application provides an interactive menu with the following options:

1. **Add Task**: Enter a description for your new task
2. **View Tasks**: Display all existing tasks with their status
3. **Complete Task**: Mark a specific task as completed using its ID
4. **Delete Task**: Remove a task permanently using its ID
5. **Exit**: Close the application

### Example Usage

```
Task Manager
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

Choose an option: 1
Enter task description: Complete Python project
Task 'Complete Python project' added with ID 1.

Choose an option: 2
ID: 1, Description: Complete Python project, Status: Pending

Choose an option: 3
Enter task ID to complete: 1
Task ID 1 marked as completed.
```

## Code Structure

The application consists of several key functions:

- `add_task(description)`: Creates a new task with auto-incremented ID
- `view_tasks()`: Displays all tasks in a formatted list
- `complete_task(task_id)`: Marks a specific task as completed
- `delete_task(task_id)`: Removes a task from the list
- `main()`: Main application loop with interactive menu

## Data Structure

Tasks are stored as dictionaries with the following structure:
```python
{
    "id": int,          # Unique task identifier
    "description": str, # Task description
    "completed": bool   # Task completion status
}
```

## Error Handling

- Invalid menu selections are handled with appropriate error messages
- Non-existent task IDs are validated before operations
- Input validation prevents crashes from invalid data types