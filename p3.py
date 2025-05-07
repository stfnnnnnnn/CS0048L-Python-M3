import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    print('========================================================================') 
    print('                             MY TO DO LIST') 
    print('========================================================================')
    print('Main Menu:') 
    print('[1] Add Task') 
    print('[2] Remove Task')
    print('[3] View Tasks') 
    print('[4] Exit\n')

tasks = []

while True:
    clear()
    show_main_menu()
    choice = input('--- Your Choice ---\nSelect a choice (1-4): ')
    time.sleep(1)

    if choice == '1':
        clear()
        print('========================================================================') 
        print('                              ADD TASK') 
        print('========================================================================')
        task = input("Enter the task to be added: ")
        time.sleep(0.5)
        if task.strip():
            tasks.append(task.strip())
            print("\nSaving Task....")
            time.sleep(1)
            print("Adding Task....")
            time.sleep(1)
            print("\n**Task added to list.**")
        else:
            print("\nInvalid task. Please enter a non-empty description.")
        time.sleep(0.5)
        input("\nPress Enter to continue...")

    elif choice == '2':
        clear()
        print('========================================================================') 
        print('                            REMOVE TASK') 
        print('========================================================================')
        if tasks:
            task = input("Enter the exact task to be removed: ")
            time.sleep(0.5)
            if task in tasks:
                tasks.remove(task)
                print("\nLoading Task....")
                time.sleep(1)
                print("Removing Task....")
                time.sleep(1)
                print("\n**Task removed successfully.**")
            else:
                time.sleep(0.5)
                print("\nTask not found in the list.")
        else:
            time.sleep(0.5)
            print("\nNo tasks to remove.")
        time.sleep(0.5)
        input("\nPress Enter to continue...")

    elif choice == '3':
        clear()
        print('========================================================================') 
        print('                             VIEW TASKS') 
        print('========================================================================')
        if tasks:
            print("\nLoading Tasks....")
            time.sleep(1)
            print("Compiling Tasks....")
            time.sleep(1)
            print("\nTASK LIST")
            print("------------------------------------------------------------------------")
            for index, task in enumerate(tasks, start=1):
                print(f"{index:<3} | {task:<60}")
            print("------------------------------------------------------------------------")
        else:
            print("\nNo tasks in your to-do list.")
        time.sleep(0.5)
        input("\nPress Enter to continue...")

    elif choice == '4':
        clear()
        time.sleep(1)
        print("Thank you for using the To-Do List App. Goodbye!")
        time.sleep(2)
        break

    else:
        time.sleep(1)
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        time.sleep(2)