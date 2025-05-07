import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    print('========================================================================') 
    print('                            GRADE CALCULATOR') 
    print('========================================================================')
    print('Main Menu:') 
    print('[1] Add Score') 
    print('[2] Calculate Average') 
    print('[3] Exit\n')

def add_score(scores):
    clear()
    print('========================================================================') 
    print('                              ADD SCORE') 
    print('========================================================================')
    subject = input("Enter the subject: ")
    time.sleep(0.5)
    try:
        score = float(input("Enter the score (1-100): "))
        if 1 <= score <= 100:
            scores.append(score)
            print("\nCreating Subject....")
            time.sleep(1)
            print("Adding Score....")
            time.sleep(1)
            print("\n**Score added to database.**")
        else:
            print("\nInvalid score. Please enter a value between 1 and 100.")
    except ValueError:
        time.sleep(1)
        print("\nInvalid input. Please enter a numeric value.")
    time.sleep(0.5)
    input("\nPress Enter to continue...")

def calculate_average(scores):
    clear()
    print('========================================================================') 
    print('                          CALCULATE AVERAGE') 
    print('========================================================================')
    if scores:
        average = sum(scores) / len(scores)
        print("\nCompiling Scores....")
        time.sleep(1)
        print("Calculating Average....")
        time.sleep(1)
        print(f"\nAverage Grade: {average:.2f}")
    else:
        time.sleep(1)
        print("\nNo scores entered yet.")
    time.sleep(0.5)
    input("\nPress Enter to continue...")

def main():
    scores = []
    while True:
        choice = ''
        valid_choices = ['1', '2', '3']
        
        while choice not in valid_choices:
            clear()
            show_main_menu()
            choice = input('--- Your Choice ---\nSelect a choice (1-3): ')
            if choice not in valid_choices:
                print("\nInvalid choice. Please enter 1, 2, or 3.")
                time.sleep(2)

        if choice == '1':
            add_score(scores)
        elif choice == '2':
            calculate_average(scores)
        elif choice == '3':
            clear()
            time.sleep(1)
            print("Thank you for using the Student Grade Calculator. Goodbye!")
            time.sleep(2)
            break

if __name__ == "__main__":
    main()