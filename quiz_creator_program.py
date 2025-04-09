# General flow of quiz creator program:
# Ask for the filename (if user wants to create/open another quiz)
# Ask user for input
# Store data into text file
# Loop the program until user chooses to exit


# Function to set filename var (for creating/opening a file)
def file_naming():
    filename = input("\nInput your filename (w/o extension): ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"
    return filename

# Function to ask user for input then store the collected data
def quiz_creator(filename):
    with open(filename, "a") as file:
        # Input question
        print("\n>>> QUIZ CREATOR <<<")
        question = input(f"Input question: ")

        # Input possible answers
        print("\nNote: No need to put letters in the choices. Let the quiz creator run it's magic!✨")
        choices_a = input("Possible answer: ").lower()
        choices_b = input("Possible answer: ").lower()
        choices_c = input("Possible answer: ").lower()
        choices_d = input("Possible answer: ").lower()

        # Input correct answer
        correct_ans = input("\nCorrect answer: ").lower()

        # Store data into text file
        file.write(f"\nQuestion: {question}")
        file.write(f"\na) {choices_a}")
        file.write(f"\nb) {choices_b}")
        file.write(f"\nc) {choices_c}")
        file.write(f"\nd) {choices_d}")
            
        letter = ""
        if correct_ans == choices_a:
            letter = 'a)'
        elif correct_ans == choices_b:
            letter = 'b)'
        elif correct_ans == choices_c:
            letter = 'c)'
        elif correct_ans == choices_d:
            letter = 'd)'

        file.write(f"\nCorrect answer: {letter} {correct_ans}\n")

    file.close()

# Function for main menu
def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        num_1 = print("👆 Press 1 to create new or edit an existing quiz file")
        num_2 = print("👆 Press 2 to view a quiz file")
        num_3 = print("👆 Press 3 to exit")

        try:
            choice = int(input("\n⭐ Enter your choice: "))
        except ValueError:   # Error if user input isn't in the choices
            print("Invalid input. Try again.")
            continue

        if choice == 1:
            filename = file_naming()   # Will ask for a filename
            add_questions(filename)   # Loop to ask user for question/s
        elif choice == 2:
            filename = input("\nEnter filename to open (with extension): ")
            try:
                with open(filename, "r") as file:   # Open file to read
                    print(f"\n>>> QUIZ ({filename}) <<<")
                    print(file.read())
                    
                    back = input("Go back to main menu? (yes/no): ")
                    if back == "yes":
                        continue
                    else:
                        break
            except FileNotFoundError:
                print("File not found. Try again.")
        elif choice == 3:
            print("\nGoodbye, user!👋")
            break

# Function to add more questions in a file
def add_questions(filename):
    while True:
        quiz_creator(filename)
            
        add_input = input("\nDo you want to add more questions? (yes/no): ").lower()
        if add_input == "yes":
            print()
            continue
        else:
            main_menu()
        
# Start the program
if __name__ == "__main__":
    main_menu()