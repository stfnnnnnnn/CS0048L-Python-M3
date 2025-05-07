import os
import time
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    print('========================================================================') 
    print('                               GAME MENU') 
    print('========================================================================')
    print('Main Menu:') 
    print('[1] Play Number Guessing Game') 
    print('[2] Exit\n')

def play_game():
    clear()
    print('========================================================================') 
    print('                      PLAY NUMBER GUESSING GAME') 
    print('========================================================================')

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number (1-100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number within the range 1 to 100.")
                continue

            if guess < number_to_guess:
                time.sleep(0.5)
                print("Too low!")
            elif guess > number_to_guess:
                time.sleep(0.5)
                print("Too high!")
            else:
                print("\nLoading Score Log......")
                time.sleep(1)
                print("Retrieving Attempts......")
                time.sleep(1)
                print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    time.sleep(0.5)
    input("\nPress Enter to continue...")

def main():
    while True:
        clear()
        show_main_menu()
        choice = input('--- Your Choice ---\nSelect a choice (1-2): ')
        time.sleep(1)

        if choice == '1':
            play_game()
        elif choice == '2':
            clear()
            print("Thank you for playing the Number Guessing Game. Goodbye!")
            time.sleep(2)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
            time.sleep(2)

if __name__ == "__main__":
    main()