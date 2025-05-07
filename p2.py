import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

celtofar = lambda c: (c * 9/5) + 32
fartocel = lambda f: (f - 32) * 5/9

def show_main_menu():
    print('========================================================================') 
    print('                         TEMPERATURE CONVERTER') 
    print('========================================================================')
    print('Main Menu:') 
    print('[1] Convert Celsius to Fahrenheit') 
    print('[2] Convert Fahrenheit to Celsius') 
    print('[3] Exit\n')

while True:
    clear()
    show_main_menu()
    choice = input('--- Your Choice ---\nSelect a choice (1-3): ')
    time.sleep(1)

    if choice == '1':
        clear()
        print('========================================================================') 
        print('                     CELSIUS TO FAHRENHEIT CONVERTER') 
        print('========================================================================')
        try:
            c = float(input("Enter temperature in Celsius: "))
            time.sleep(1.5)
            print("\nCalculating Temperature...")
            time.sleep(1.5)
            print("Converting from Celsius To Farenheit..")
            time.sleep(1.5)
            result = celtofar(c)
            print(f"\nTemperature in Fahrenheit: {result:.2f}")
        except ValueError:
            print("\nInvalid input. Please enter a numeric value.")
        time.sleep(0.5)
        input("\nPress Enter to continue...")

    elif choice == '2':
        clear()
        print('========================================================================') 
        print('                     FAHRENHEIT TO CELSIUS CONVERTER') 
        print('========================================================================')
        try:
            f = float(input("Enter temperature in Fahrenheit: "))
            time.sleep(1.5)
            print("\nCalculating Temperature...")
            time.sleep(1.5)
            print("Converting from Farenheit To Celsius ..")
            result = fartocel(f)
            print(f"Temperature in Celsius: {result:.2f}")
        except ValueError:
            print("\nInvalid input. Please enter a numeric value.")
        time.sleep(0.5)
        input("\nPress Enter to continue...")

    elif choice == '3':
        clear()
        print("Thank you for using the Temperature Converter. Goodbye!")
        time.sleep(2)
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        time.sleep(2)