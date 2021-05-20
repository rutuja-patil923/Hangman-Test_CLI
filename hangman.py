import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            return False
    return True

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word



def isValid(ip_character):
    if ip_character == "hint":
        return False

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    if len(ip_character) != 1:
        print("You can enter only one letter at a time!")
        return False
    elif ip_character not in alphabets:
        print("Please Enter valid character")
        return False
    else:
        return True



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    available_letters = ""
    letters_left = string.ascii_lowercase
    for i in range(len(letters_left)):
        if letters_left[i] not in letters_guessed:
            available_letters += letters_left[i]
    return available_letters


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []
    remaining_lives = 8
    hintTaken = 0

    while (True):

        while (True):
            available_letters = get_available_letters(letters_guessed)
            print("Available letters: {} ".format(available_letters))

            guess = input("Please guess a letter: ")
            letter = guess.lower()
            if letter not in get_available_letters(letters_guessed):
                print("You have entered this letter previously!")
                continue
            if (isValid(letter)):
                break
            if(letter=="hint") & (hintTaken==0):
                for let in secret_word:
                    if let not in letters_guessed:
                        print("Hint : {}".format(let))
                        hintTaken = 1
                        break
            elif(letter=="hint") & (hintTaken==1):
                print("Oops:( You have already taken hint!")
            

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)
            print(IMAGES[8-remaining_lives])
            remaining_lives -= 1
            print("You have {} live left!".format(remaining_lives))
        if(remaining_lives==0):
            print("You are out of your lives!")
            print("The correct word is {}".format(secret_word))
            break

    print("---------------------------------------------------")
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
