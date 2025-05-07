import os
import time
import p1 
import p2
import p3  
import p4  
import p5 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    print('========================================================================') 
    print('                            MAIN MENU') 
    print('========================================================================')
    print('Actions:') 
    print('[1] Calculator') 
    print('[2] Temperature Converter') 
    print('[3] To-Do List')
    print('[4] Number Guessing Game')
    print('[5] Grade Calculator')
    print('[6] Exit\n')

while True:
    time.sleep(2)
    clear()
    show_main_menu()
    choice = input('--- Your Choice ---\nSelect a choice (1-6): ')
    time.sleep(1)

    if choice == '1':
        p1.main()
    elif choice == '2':
        p2.main()
    elif choice == '3':
        p3.main()
    elif choice == '4':
        p4.main()
    elif choice == '5':
        p5.main()
    elif choice == '6':
        clear()
        print("Thank you for using the program. Goodbye!")
        time.sleep(2)
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
        time.sleep(2)
