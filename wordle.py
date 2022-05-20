### FUNCTIONS ###
import random

def instructions():
    print("""Hi there, welcome to worldle!
    This is a single player game where the aim is to guess a five letter word
    You have six attempts 
    Look out for the following: "✔❌❌✔➕"
    "✔" Indicates a correct letter in the right position
    "❌" Indicates an incorrect letter
    "➕" Indivates a correct letter in the wrong position
    """)

def word_selector():
    """Opens a text file of 5 letter words and converts it to a list of strings.
    Set global variables for the list of words and the answer.
    Pick a random string from the list and return as the answer."""
    with open("5_letter_words.txt", "r") as file:
        all_words = file.read()
        global words
        words = list(map(str, all_words.split()))
        global answer
        answer = random.choice(words)
        return answer

### MAIN PROGRAM ###

instructions()

def check_word():
    hidden_word = word_selector()
    attempt = 6
    while attempt > 0:
        guess = str(input("Guess the word: "))
        if guess == hidden_word:
            print("Congratulations, you guessed correctly!")
            break
        elif guess not in words:
            print("This word is not in the list - try again.")
        else:
            attempt = attempt - 1
            if attempt > 1:
                print(f"You have {attempt} attempts left \n")
            elif attempt == 1:
                print(f"You have {attempt} attempt left \n")
            for char, word in zip(hidden_word, guess):
                if word in hidden_word and word in char:
                    print(word + " ✔ ")
                elif word in hidden_word:
                    print(word + " ➕ ")
                else:
                    print(" ❌ ")
            if attempt ==0:
                print(f"\nGame over ! :'(")
    print(f"\nThe answer was: ")
    print(f"{answer}\n")

check_word()

