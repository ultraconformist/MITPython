###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Morgan
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================
eggs_taken = 0  # Tracking quantity taken
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
    #global eggs_taken   # Testing variable to test greedy algorithm
    
    # Greedy algorithm recursively done:
    # Base case 1: If target_weight == 0, return the number of eggs 
    # that have been taken. 
    # Base case 2: if there is room, take the largest egg, 
    # subtract it from target_weight, add one to number of eggs taken, 
    # and repeat. 
    # Recursive solution: Remove the largest egg from the list, and repeat, 
    # with the new list
    # Need to do this, and then memoize the recursive solution?

    #if target_weight == 0:
    #    return eggs_taken
    #elif target_weight - egg_weights[-1] >= 0:
    #    updated_target_weight = target_weight - egg_weights[-1]
    #    eggs_taken += 1
    #    return dp_make_weight(egg_weights, updated_target_weight)
    #else:
    #    return dp_make_weight(egg_weights[:-1], target_weight)
    
    # Okay, this works as expected; how can this be made dynamic?
    # Let's try to rewrite this as a brute force algorithm, recursively.
    # Base case 1: if target_weight == 0, return the number of eggs taken.
    # Recursive solution: For each weight in egg_weights, subtract that weight
    # from target_weight and = to updated_target_weight, add one to eggs taken,
    # and repeat with new target weight?
    #if target_weight == 0:
    #    return eggs_taken
    #for weight in egg_weights:
    #    updated_target_weight = target_weight-weight
    #    print(updated_target_weight)
    #    eggs_taken += 1
    #    return dp_make_weight(egg_weights, updated_target_weight)
    
    # This needs to be based on a decision tree that evaluates recursively...
    #eggs_taken = 0
    #if target_weight == 0:
    #    return eggs_taken
    #for weight in egg_weights:
    #    if weight <= target_weight:
    #       updated_target_weight = target_weight - weight
    #        return dp_make_weight(egg_weights, updated_target_weight)
    #        print(updated_target_weight)
    #    else:
    #        return dp_make_weight(egg_weights, target_weight)
    # Dynamic programming involves the same thing 
    
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