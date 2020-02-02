# Problem Set 4A
# Name: Morgan

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    try:
        assert isinstance(sequence, str)    # Break if sequence is not a string
        
        if len(sequence) == 1:  # Base case; if sequence is only one character
            return [sequence]   # return a singleton list containing 
                                # that character
        else:
            perm_list = []          # List of all permutations
        
        # Loop for all permutations not including last character in string
            for perm in get_permutations(sequence[:-1]):
                for i in range(len(perm)+1):
                    perm_list.append(perm[:i] + sequence[-1] + perm[i:])
                    
            return perm_list
        
            
    except AssertionError:
        print(sequence,'is not a string')
        
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['cba,','bca', 'bac', 'cab', 'acb', 'abc'])
    print('Actual Output:', get_permutations(example_input))
    if get_permutations(example_input) == ['cba','bca', 'bac', 'cab', 'acb', 'abc']:
        print ('Test 1 passed.')
    else:
        print ('Test 1 failed.')
    
    example_input = 'a'
    print('Input:', example_input)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example_input))
    if get_permutations(example_input) == ['a']:
        print ('Test 2 passed.')
    else:
        print ('Test 2 failed.')   
    
    example_input = 10
    print('Input:', example_input)
    print('Expected Output:', None)
    print('Actual Output:', get_permutations(example_input))
    if get_permutations(example_input) == None:
        print ('Test 3 passed.')
    else:
        print ('Test 3 failed.')