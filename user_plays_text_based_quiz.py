# General flow of quiz creator program:
# a. Ask for the filename (if user wants to create/open another quiz)
#    Ask user for input
#    Store data into text file
#    Loop the program until user chooses to exit
# b. View quiz file
# c. Questions will be randomly answered by the user
#    Program will check if the answer is correct

import random
import os
import time

# Function to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to set filename var (for creating/opening a file)
def file_naming():
    filename = input("\nInput your filename (w/o extension): ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"
    return filename

# Function to ask user for input then store the collected data
def quiz_creator(filename):
    with open(filename, "a") as file:
        clear_screen()
        # Input question
        print(">>> QUIZ CREATOR <<<")
        question = input(f"\nInput question: ").strip()

        # Input possible answers
        choices_a = input("\nPossible answer: a) ").strip().lower()
        choices_b = input("Possible answer: b) ").strip().lower()
        choices_c = input("Possible answer: c) ").strip().lower()
        choices_d = input("Possible answer: d) ").strip().lower()

        # Input correct answer
        while True:
            correct_ans = input("\nCorrect answer (a/b/c/d): ").strip().lower()
            if correct_ans in ["a", "b", "c", "d"]:
                break
            else:
                print("🚫 Invalid choice. Please enter only 'a', 'b', 'c', or 'd'.")

        # Store data into text file
        file.write(f"\nQuestion: {question}")
        file.write(f"\na) {choices_a}")
        file.write(f"\nb) {choices_b}")
        file.write(f"\nc) {choices_c}")
        file.write(f"\nd) {choices_d}")
        file.write(f"\nCorrect answer: {correct_ans}\n")

# Function to add more questions in a file
def add_questions(filename):
    while True:
        quiz_creator(filename)

        while True:
            clear_screen()
            add_input = input("\nDo you want to add more questions? (yes/no): ").strip().lower()

            if add_input == "yes":
                print()
                break  # Break inner loop and continue outer loop
            elif add_input == "no":
                return  # Exit function entirely
            else:
                print("🚫 Invalid input. Please answer with 'yes' or 'no'.")

# Load to quiz from file
def load_quiz(filename):
    with open(filename, "r") as file:
        # to remove empty lines
        lines = [line.strip() for line in file if line.strip()]
        
    quiz = []
    index = 0
    while index < len(lines):
        question = lines[index]
        choices = [lines[index+1], lines[index+2], lines[index+3], lines[index+4]]
        answer_line = lines[index+5]
        answer = answer_line.split(":")[1].strip()
        quiz.append({
            "question": question,
            "choices": choices,
            "answer": answer
        })
        index += 6     # move to the next question block
    return quiz

# Run the quiz
def run_quiz(quiz):
    random.shuffle(quiz)     # Shuffle questions
    score = 0
    total = len(quiz)
    unanswered = total
    
    index = 0
    while index < total:
        entry = quiz[index]
        print(entry["question"])
        for choice in entry["choices"]:
            print(choice)
            
        user_input = input("\nYour answer (a/b/c/d): ").strip().lower()
        
        if user_input == entry["answer"]:
            score += 1
            print(f"""\n✅ Correct! +1 point!
📊 Your current score: {score}/{len(quiz)}""")
            time.sleep(1.5)
            clear_screen()
        else:
            print(f"""\n❌ Wrong! The answer was {entry['answer']}
📊 Your current score: {score}/{len(quiz)}""")
            time.sleep(1.5)
            clear_screen()
            
        index += 1
        
        unanswered -= 1
        if unanswered == 0:
            clear_screen()
            print(f"🏁 Quiz finished! Your final score: {score}/{total}")
            time.sleep(2)
            
    while True:
        print("\n❗ Entering 'no' will exit the program.")
        back = input("Do you want to go to main menu? (yes/no): ")
            
        if back == "yes":
            return
        elif back == "no":
            print("\nGoodbye, user!👋")
            exit()
        else:
            print("🚫 Invalid input. Please answer with 'yes' or 'no'.")

# Function for main menu
def main_menu():
    while True:
        clear_screen()
        print("""WELCOME TO QUIZMATE!
Loading...""")
        time.sleep(2)
        clear_screen()
        print("""===== MAIN MENU =====
👆 Press 1 to start a quiz
👆 Press 2 to create new or edit an existing quiz file
👆 Press 3 to view a quiz file
👆 Press 4 to exit""")

        try:
            choice = int(input("\n⭐ Enter your choice: "))
            
            if choice not in [1, 2, 3, 4]:
                raise ValueError("🚫 Invalid input. Please enter a number from 1 to 4.")

            if choice == 1:
                while True:
                    try:
                        filename = input("\nEnter filename to open (with extension): ").strip()
                        print("📂 Loading quiz...")
                        time.sleep(2)
                        quiz = load_quiz(filename)
                        clear_screen()
                        run_quiz(quiz)
                        break
                    except FileNotFoundError:
                        print("\n🚫 File not found. Try again.")
                        time.sleep(1.5)
                        continue
                
            elif choice == 2:
                filename = file_naming()   # Will ask for a filename
                add_questions(filename)   # Loop to ask user for question/s
                print(f"\n📝 Quiz '{filename}' created or updated successfully!")
                time.sleep(2)
                    
            elif choice == 3:
                while True:
                    filename = input("\nEnter filename to open (with extension): ").strip()
                    time.sleep(1.5)
                    clear_screen()
                    try:
                        with open(filename, "r") as file:   # Open file to read
                            print(f"\n>>> QUIZ ({filename}) <<<")
                            print(file.read())
                    except FileNotFoundError:
                        print("🚫 File not found. Try again.")
                        time.sleep(1.5)
                        continue
                    
                    print("\n❗ Entering 'no' will exit the program.")        
                    back = input("Go back to main menu? (yes/no): ").strip().lower()
                    if back == "yes":
                        time.sleep(1)
                        clear_screen()
                        break
                    elif back == "no":
                        print("\nExiting...")
                        exit()
                    else:
                        print("\n🚫 Invalid input. Returning to main menu...")
                        time.sleep(1)
                        break
            
            elif choice == 4:
                print("\nGoodbye, user!👋")
                time.sleep(2)
                break
            
        except ValueError as error:   # Error if user input isn't in the choices
            print(error)
            time.sleep(1.5)
            continue
        
# Start the program
if __name__ == "__main__":
    main_menu()