import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

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

def main():
    while True:
        clear()
        show_main_menu()
        choice = input('--- Your Choice ---\nSelect a choice: ')
        time.sleep(1)

        if choice == '1':
            clear()
            print('========================================================================') 
            print('                      WELCOME TO ADDITION CALCULATOR') 
            print('========================================================================')
            a = float(input("Enter first number: "))
            time.sleep(1)
            b = float(input("Enter second number: "))
            time.sleep(1.5)
            print("\nCalculating Input...")
            time.sleep(1.5)
            result = add(a, b)
            print(f"\nThe sum of {a} and {b} is: {result}")
            time.sleep(0.5)
            input("\nPress Enter to continue...")

        elif choice == '2':
            clear()
            print('========================================================================') 
            print('                     WELCOME TO SUBTRACTION CALCULATOR') 
            print('========================================================================')
            a = float(input("Enter first number: "))
            time.sleep(1)
            b = float(input("Enter second number: "))
            time.sleep(1.5)
            print("\nCalculating Input...")
            time.sleep(1.5)
            result = subtract(a, b)
            print(f"\nThe difference of {a} and {b} is: {result}")
            time.sleep(0.5)
            input("\nPress Enter to continue...")

        elif choice == '3':
            clear()
            print('========================================================================') 
            print('                   WELCOME TO MULTIPLICATION CALCULATOR') 
            print('========================================================================')
            a = float(input("Enter first number: "))
            time.sleep(1)
            b = float(input("Enter second number: "))
            time.sleep(1.5)
            print("\nCalculating Input...")
            time.sleep(1.5)
            result = multiply(a, b)
            print(f"\nThe product of {a} and {b} is: {result}")
            time.sleep(0.5)
            input("\nPress Enter to continue...")

        elif choice == '4':
            clear()
            print('========================================================================') 
            print('                       WELCOME TO DIVISION CALCULATOR') 
            print('========================================================================')
            a = float(input("Enter first number: "))
            time.sleep(1)
            b = float(input("Enter second number: "))
            if b == 0:
                print("\nError: Cannot divide by zero.")
            else:
                time.sleep(1.5)
                print("\nCalculating Input...")
                time.sleep(1.5)
                result = divide(a, b)
                print(f"\nThe quotient of {a} and {b} is: {result}")
            input("\nPress Enter to continue...")

        elif choice == '5':
            clear()
            time.sleep(2)
            print("Thank you for using the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
            time.sleep(2)

if __name__ == "__main__":
    main()