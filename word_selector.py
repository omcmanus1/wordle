import random

def word_selector():
    with open("5_letter_words.txt", "r") as file:
        all_words = file.read()
        words = list(map(str, all_words.split()))
        global word
        word = random.choice(words)
        print(word)

word_selector()
print(word)
    
