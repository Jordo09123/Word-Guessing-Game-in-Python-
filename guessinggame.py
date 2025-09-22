import random

# open the wordbank.txt so the program can select a random word
with open("wordbank.txt", "r") as file:
    word_bank = [line.strip() for line in file if line.strip()]

# select a random word from the bank
word = random.choice(word_bank)

guessedWord = ['_'] * len(word)

# give the user 10 attempts
attempts = 10

# game loop
while attempts > 0:

    print('\nCurrent word: ' + ''.join(guessedWord))

    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess

        print("Great guess! Attempts left: {0}".format(str(attempts)))

    else:
        attempts -= 1
        print("Wrong guess! Attempts left: {0}".format(str(attempts)))

    if '_' not in guessedWord:
        print("\nCongratulations!! You guessed the word: {0}".format(word))
        break

    if attempts == 0 and '_' in guessedWord:
        print("\nYou have run out of attempts! The word was {0}".format(word))
