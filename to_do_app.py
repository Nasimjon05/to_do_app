# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 18:57:37 2025

@author: Nasimjon
"""

# To Do app (CLI) 
# 1. Show tasks
# 2. Choose action


    
    
    
# Function to create a task dictionary with default status ❌
def create_task(name, due, status="❌"):
    return {'name': name, 'due': due, 'status': status}

# Function to add a new task to the list
def add_task(tasks):
    # Get user input for task details
    task_name = input('\n📝 Enter new task: ')
    task_due_date = input('📅 Enter due date (e.g., 30-August): ')
    task_status = input("🔘 Enter task status (optional, default ❌): ").strip()

    # If user doesn't enter status, default to "❌"
    if not task_status:
        task_status = "❌"

    # Create and append the task to the task list
    new_task = create_task(task_name, task_due_date, task_status)
    tasks.append(new_task)

    # Show confirmation message
    print(f"\n✅ New Task Added: {new_task['name']}    Due: {new_task['due']}    Status: {new_task['status']}")

# Function to display the list of tasks
def view_tasks(tasks):
    print('\n📋 Your To-Do List:')
    # If task list is empty
    if not tasks:
        print("🎉 You have no tasks!")
    # Loop through and display each task with its number
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']}    Due: {task['due']}    Status: {task['status']}")

# Function to mark a task as done
def mark_task_as_done(tasks):
    view_tasks(tasks)  # Show current tasks
    try:
        # Ask user which task to mark
        task_number = int(input('\n✅ Which task do you want to mark as done? (Enter number): '))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['status'] = '✅'
            print(f"🎉 Task {task_number} marked as done!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)  # Show current tasks
    try:
        # Ask user which task to delete
        task_number = int(input('\n🗑️ Which task do you want to delete? (Enter number): '))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)  # Remove task from list
            print(f"🗑️ Deleted: {removed['name']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# === Main Program Starts Here ===

# Predefined task list with one sample task
tasks = [{'name': 'Running', 'due': 'everyday', 'status': '❌'}]

# List of available actions
actions = ["Add task", "View tasks", "Mark task as done", "Delete task", "Exit"]

# Infinite loop to keep the program running
while True:
    # Display current tasks
    view_tasks(tasks)
    
    # Display menu of actions
    print("\n🔧 Actions:")
    for i, act in enumerate(actions, start=1):
        print(f"\t{i}. {act}")

    # Ask user to choose an action
    choice = input("👉 Choose an action (1–5): ")

    # Match user choice with corresponding action using match-case
    match choice:
        case "1":
            add_task(tasks)
        case "2":
            view_tasks(tasks)
        case "3":
            mark_task_as_done(tasks)
        case "4":
            delete_task(tasks)
        case "5":
            print("👋 Exiting... Goodbye!")
            break  # Exit the loop and end the program
        case _:
            print("❌ Invalid choice. Please enter a number from 1 to 5.")

    
    


