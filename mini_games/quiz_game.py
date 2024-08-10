def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1
    valid_guesses = {'A', 'B', 'C', 'D'}

    for key in questions:
        print("-----------------------")
        print(key)
        for i in options[question_number - 1]:
            print(i)

        valid_guess = False

        while not valid_guess:
            guess = input("Enter (A, B, C, or D): ")
            guess = guess.upper()
            if guess in valid_guesses:
                guesses.append(guess)
                correct_guesses += check_answer(questions.get(key), guess)
                valid_guess = True
            else:
                valid_guess = False
                print("Invalid input. Please enter A, B, C, or D.")

        question_number += 1

    display_score(correct_guesses, guesses)

    play_again()

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

def display_score(correct_guesses, guesses):
    print("-----------------------")
    print("RESULTS")
    print("-----------------------")

    print("ANSWERS: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")

    print("")
    print("GUESSES: ", end="")
    for i in guesses:
        print(i, end=" ")
    
    print("")
    score = int((correct_guesses / len(questions)) * 100)
    print("SCORE: " + str(score)+"%")

def play_again():
    print("-----------------------")
    response = input("Do you want to play again? (Y/N): ")
    response = response.upper()
    if response == 'Y':
        new_game()
    else:
        return False




questions = {
    "Who created Python?: ": "A",
    "What year was Pyhton created?: ": "B",
    "Python is tributed to which comedy group? :": "C",
    "Is the Earth round?: ": "A"
}

options = [[
    "A. Guido Van Rossum",
    "B. Elon Musk",
    "C. Bill Gates",
    "D. Mark Zuckerberg"
],
[
    "A. 1989",
    "B. 1991",
    "C. 2000",
    "D. 2016"
],
[
    "A. Lonely Island",
    "B. Smosh",
    "C. Monty Python",
    "D. SNL"
],
[
    "A. True",
    "B. False",
    "C. Sometimes",
    "D. Maybe"
]]

new_game()