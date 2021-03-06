# Problem Set 4B
# Name: Morgan

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        new_valid_words = self.valid_words.copy()
        return new_valid_words

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Uppercase alphabet
        lowercase = 'abcdefghijklmnopqrstuvwxyz' # Lowercase alphabet
        shift_dict = {} # Create empty dictionary
        
        # Iterate over each index in both UPPERCASE and LOWERCASE,
        # creating a key for the index being iterated on,
        # and setting it equal to the value at index in the string + shift
        # subtracting the length of the string being iterated if string + shift
        # will exceed the length of that string
        
        for i in range(len(UPPERCASE)):
            if (i + shift) >= len(UPPERCASE):
                shift_dict[UPPERCASE[i]] = UPPERCASE[(i+shift)-len(UPPERCASE)]
            else:
                shift_dict[UPPERCASE[i]] = UPPERCASE[(i + shift)]

        for i in range(len(lowercase)):
            if (i + shift) >= len(lowercase):
                shift_dict[lowercase[i]] = lowercase[(i+shift)-len(lowercase)]
            else:
                shift_dict[lowercase[i]] = lowercase[(i + shift)]                

        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift) # Create dictionary for shift
        
        shifted_message = '' # Empty string to build shifted message upon
        
        # For each character in the message_text of this object,
        # check if the character exists in the dictionary of shifted characters
        # and if so, append the shifted character to the shifted message;
        # else, pass the original unmodified character through 
        # to shifted_message
        for char in self.message_text:
            if char in shift_dict.keys():
                shifted_message += shift_dict[char]
            else:
                shifted_message += char
        
        return shifted_message                
        
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        new_encryption_dict = self.encryption_dict.copy()
        return new_encryption_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # Both data attributes inherited from Message
        Message.__init__(self, text)
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        match_dict = {} # Dict to add key, value pairs 
                        # of shift-value: number-of-matches  
        
        for shift in range(1,27):
            # Create a test shift of the message using an iteration of shift
            # Split that test shift into words, test how many words
            # exist in both test_shift and word_list, and add to the dict
            # the shift value and the number of word matches
            test_shift = self.apply_shift(shift)
            test_shift = test_shift.lower()
            test_shift_split = test_shift.split()
            matches = 0
            for word in test_shift_split:
                if is_word(self.valid_words, word):
                    matches += 1
            match_dict[shift] = matches
 
        # For each entry in match_dict, find the key with the highest value
        # & set it to best_shift
        best_shift = max(match_dict, key=match_dict.get)
        decrypted_message = self.apply_shift(best_shift)
        
        return (best_shift, decrypted_message)
                            
if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    # Test cases
    plaintext = PlaintextMessage('jaguar', 5)
    print('Expected Output: oflzfw')
    print('Actual Output: ', plaintext.get_message_text_encrypted())
    plaintext = PlaintextMessage('attack at dawn', 15)
    print('Expected Output: piiprz pi splc')
    print('Actual Output: ', plaintext.get_message_text_encrypted())
    
    # Decrypt story string
    story_string = CiphertextMessage(get_story_string())
    print(story_string.decrypt_message())
    
