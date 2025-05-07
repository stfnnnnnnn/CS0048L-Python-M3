import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def add(a,b):
    print('========================================================================') 
    print('                      WELCOME TO ADDITION CALCULATOR') 
    print('========================================================================')
    return a + b

def subtract(a,b):
    print('========================================================================') 
    print('                     WELCOME TO SUBTRACTION CALCULATOR') 
    print('========================================================================')
    return a - b

def multiply(a,b):
    print('========================================================================') 
    print('                   WELCOME TO MULTIPLICATION CALCULATOR') 
    print('========================================================================')
    return a * b

def divide(a,b):
    print('========================================================================') 
    print('                       WELCOME TO DIVISION CALCULATOR') 
    print('========================================================================')
    return a / b


# ---------------- MAIN MENU ----------------

def show_main_menu():
    print('========================================================================') 
    print('                         WELCOME TO MY CALCULATOR') 
    print('========================================================================')
    print('Main Menu:') 
    print('[1] Add') 
    print('[2] Subtract') 
    print('[3] Multiply') 
    print('[4] Divide')
    print('[5] Exit\n')

while True:
    clear()
    show_main_menu()
    choice = input('--- Your Choice ---\nSelect a choice: ').strip()

    if choice == '1':
        add(a,b)
    elif choice == '2':
        subtract(a,b)
    elif choice == '3':
        multiply(a,b)
    elif choice == '4':
        divide(a,b)
        print("Thank you for using the program. Goodbye!")
        break
    elif choice == '5':
        print("Thank you for using the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        time.sleep(2)