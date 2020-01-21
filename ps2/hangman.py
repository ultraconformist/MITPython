# Problem Set 2, hangman.py
# Name: Morgan
# Collaborators:
# Time spent: 5 and a half hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def lowerChar(char):
    '''
    char: char or string, the user input;
    returns: char, lowercase conversion of input passed
    '''
    return char.lower()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word
    are in letters_guessed;
      False otherwise
    '''
    matches = 0
    for char in secret_word:
        if char in str(letters_guessed):
            matches +=1
    if matches == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), 
    and spaces that represents which letters in secret_word 
    have been guessed so far.
    '''
    guessed_word = ''
    for char in secret_word:
        if char in str(letters_guessed):
            guessed_word += char
        else:
            guessed_word += '_ '
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which 
    letters have not yet been guessed.
    '''
    available_letters = ''
    for char in string.ascii_lowercase:
        if char not in str(letters_guessed):
            available_letters += char
        else:
            pass
    return available_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Initialize gameplay variables
    guesses_left = 6
    warnings_left = 3
    letters_guessed = ''
    vowels = 'aeiou'
    
    # Introduce game
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')

    # Game loop to repeat until break conditions are met
    while guesses_left > 0: 
            print('-----------')
            print('You have', guesses_left, 'guesses left.')
            print('Available letters: ', get_available_letters(letters_guessed))
            guess = input('Please guess a letter: ')       
            guess = lowerChar(guess)    # Convert input to lowercase
            
            if guess in str(letters_guessed) and warnings_left >= 0:
                print('Oops! You\'ve already guessed that letter.' \
                      'You now have', warnings_left, 'warnings: ')
                warnings_left -= 1
            
            elif guess in str(letters_guessed) and warnings_left < 0:
                print('Oops! You\'ve already guessed that letter.' \
                       'You have no warnings left, so you lose one guess:')
                guesses_left -= 1
            
            elif guess not in string.ascii_letters and warnings_left >= 0:
                print('Oops! That is not a valid letter. You have'\
                       , warnings_left, 'warnings left:')
                warnings_left -= 1
            
            elif guess not in string.ascii_letters and warnings_left < 0:
                print('Oops! That is not a valid letter. \
                      You have no warnings left, so you lose one guess:')
                guesses_left -= 1
                
            elif guess in secret_word:
                print('Good guess: ', )
                letters_guessed += guess
            
            elif guess in vowels:
                print('Oops! That letter is not in my word, and is a vowel,\
                      so you lose two guesses:')
                guesses_left -= 2
            
            else:
                print('Oops! That letter is not in my word.')
                letters_guessed += guess
                guesses_left -= 1
                
            print(get_guessed_word(secret_word, letters_guessed))
            
            if is_word_guessed(secret_word, letters_guessed):
                break
            
    # End game win/loss check
    if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!\n')
        print('Your total score for this game is:',\
              (guesses_left * len(secret_word)))
    else:
        print('Sorry, you ran out of guesses. The word was', secret_word)
        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special 
        symbol _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # Remove extra space before processing
    my_word = my_word.replace(' ','')
    
    if len(my_word) != len(other_word):
        return False
    
    for i in range(len(my_word)):
        if my_word[i] == other_word[i]:
            continue
        # The hidden letter(_ ) cannot be one of the letters in the word
        # that has already been revealed
        elif my_word[i] == "_" and other_word[i] not in my_word:
            continue
        else: 
            return False

    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word 
             in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, 
             all the positions at which that letter occurs in the secret word 
             are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters 
             in the word that has already been revealed.

    '''
    possible_matches = ''
    for i in wordlist:
        if match_with_gaps(my_word, i):
            possible_matches += (i + ' ')
    if possible_matches != '':
        return possible_matches
    else:
        return False


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. 
    Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Initialize gameplay variables
    guesses_left = 6
    warnings_left = 3
    letters_guessed = ''
    vowels = 'aeiou'
    
    # Introduce game
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')

    # Game loop to repeat until break conditions are met
    while guesses_left > 0: 
            print('-----------')
            print('You have', guesses_left, 'guesses left.')
            print('Available letters: ', \
                  get_available_letters(letters_guessed))
            guess = input('Please guess a letter: ')       
            guess = lowerChar(guess)    # Convert input to lowercase
            
            if guess in str(letters_guessed) and warnings_left >= 0:
                print('Oops! You\'ve already guessed that letter.' \
                      'You now have', warnings_left, 'warnings: ')
                warnings_left -= 1
            
            elif guess in str(letters_guessed) and warnings_left < 0:
                print('Oops! You\'ve already guessed that letter.' \
                       'You have no warnings left, so you lose one guess:')
                guesses_left -= 1
                
            # If user asks for hint
            elif guess == '*':
                print('Possible word matches are: ', \
                      show_possible_matches(get_guessed_word(secret_word, \
                                                             letters_guessed)))
                
            elif guess not in string.ascii_letters and warnings_left >= 0:
                print('Oops! That is not a valid letter. You have'\
                       , warnings_left, 'warnings left:')
                warnings_left -= 1
            
            elif guess not in string.ascii_letters and warnings_left < 0:
                print('Oops! That is not a valid letter.' \
                      'You have no warnings left, so you lose one guess:')
                guesses_left -= 1
                
            elif guess in secret_word:
                print('Good guess: ', )
                letters_guessed += guess
            
            elif guess in vowels:
                print('Oops! That letter is not in my word, and is a vowel,\
                      so you lose two guesses:')
                guesses_left -= 2
            
            else:
                print('Oops! That letter is not in my word.')
                letters_guessed += guess
                guesses_left -= 1
                
            print(get_guessed_word(secret_word, letters_guessed))
            
            if is_word_guessed(secret_word, letters_guessed):
                break
            
    # End game win/loss check
    if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!\n')
        print('Your total score for this game is:',\
              (guesses_left * len(secret_word)))
    else:
        print('Sorry, you ran out of guesses. The word was', secret_word)

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word) 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
