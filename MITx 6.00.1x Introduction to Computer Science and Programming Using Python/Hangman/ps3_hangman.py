# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"





abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


##Test 1:
#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

wordlist = loadWords()




def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

#Test 2:
#secretWord = random.choice(wordlist)
lettersGuessed = []

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guessed=True
    for letter in secretWord:
        if letter not in lettersGuessed: guessed=False
    return guessed
    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord_L=[]
    for letter in secretWord:
        if letter not in lettersGuessed: 
            guessedWord_L.append('_')
        else:
            guessedWord_L.append(letter)
    guessedWord=''.join(map(str,guessedWord_L))
    return guessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    availableABC_L=list(set(abc)-set(lettersGuessed))
    availableABC_L.sort()
    availableABC=''.join(map(str,availableABC_L))
    return availableABC
    

lettersGuessed = []
abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def isInLetter(secretWord, guessInLowerCase):
    goodguess=False
    for letter in secretWord:
        if letter == guessInLowerCase: goodguess=True
    return goodguess

def hangman(secretWord):
    lettersGuessed = []
    mistakesMade=8
    nextrun=False
    
    print("Welcome to the game, Hangman!")
    long=len(secretWord)
    print("I am thinking of a word that is",long,"letters long.")
    
    while nextrun==False:
        print("-----------")
        print ("You have",mistakesMade,"guesses left.")
        AvailableLetters=getAvailableLetters(lettersGuessed)
        print("Available Letters:", AvailableLetters)
        guess = input("Please guess a letter: ")
        
        guessInLowerCase = guess.lower()
        if guessInLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            continue
        
        if isInLetter(secretWord, guessInLowerCase)==True:
            lettersGuessed.append(guessInLowerCase)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(guessInLowerCase)
            mistakesMade-=1
            
            
        if mistakesMade==0:
            print("-----------")
            print("Sorry, you ran out of guesses. The word was", secretWord)
            break
                
        
        if isWordGuessed(secretWord, lettersGuessed)==False:
            nextrun=False
        else:
            nextrun=True
            print("-----------")
            print("Congratulations, you won!")
            
        


#print(isWordGuessed(secretWord, lettersGuessed))
#print(getGuessedWord(secretWord, lettersGuessed))
#print(getAvailableLetters(lettersGuessed))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()

secretWord="c"
#secretWord="zzz"
hangman(secretWord)

