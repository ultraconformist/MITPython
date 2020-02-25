###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Morgan
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================
# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    
    choice_list = []
    
    # First, check to see if this problem is already solved.
    try:
        return memo[target_weight]
    # If memo[target_weight] doesn't exist, then solve for this weight
    except KeyError:
        # Base case
        if target_weight == 0:
            return 0
        # Choose a weight in the list of egg weights, subturact it from target,
        # and if the updated weight isn't below 0, then we're not done yet;
        # recursively call egg weight.
        # Finally, return the recursive call that has the lowest weight, + 1
        # because this call was one additional egg, obviously.
        # Also add this solution to the memo.
        else:
            for weight in egg_weights:
                if target_weight - weight >= 0:
                    updated_weight = target_weight - weight
                    choice_list.append(dp_make_weight(egg_weights, updated_weight, memo))
            memo[target_weight] = (min(choice_list) + 1)
            return (min(choice_list) + 1)

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected output: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()