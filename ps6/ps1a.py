###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Morgan

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cow_data = open(filename, 'r')  # Open file for reading
    cow_dict = {}   # Open empty dict to return at end
    
    # Iterate over each line of cow_data, stripping the newline char from end
    # of each line, and splitting the line into a list at the comma.
    # Cast second value to int, and create new key with value of name in dict
    for line in cow_data:
        line = line.rstrip()
        splitline = line.split(',')
        cow_dict[splitline[0]] = int(splitline[1])
    
    cow_data.close()    # Close file to clear up memory
    
    return cow_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_dict = cows.copy()
    encumbrance = 0
    
    cows_list = sorted(cows_dict.items(), key=lambda i: i[1], reverse=True)
    trips_list = []
    
    while len(cows_list) > 0:
        current_trip = []
        for cow in cows_list:
            if encumbrance == limit:
                break
            elif (cow[1] + encumbrance) <= limit:
                current_trip.append(cow[0])
                encumbrance += cow[1]
            else:
                continue
        trips_list.append(current_trip)
        new_cows_list = []
        
        # Remove cows that have already been shipped off from cows_list, update
        for cow in cows_list:
            if cow[0] in current_trip:
                pass
            else:
                new_cows_list.append(cow)
        cows_list = new_cows_list
        
        encumbrance = 0
    
    return trips_list

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_dict = cows.copy()
    cows_list = [(cow, weight) for cow, weight in cows_dict.items()]

    partitions_list = [partition for partition in get_partitions(cows_list)]
    for partition in partitions_list:
        oversize = False
        for trip in partition:
            encumbrance = 0
            print(trip)
            for cow in trip:
                encumbrance += cow[1]
                print(encumbrance)
                if encumbrance > limit:
                    oversize = True
                    break
                elif oversize != True:
                    optimal_partition = partition
                    print(optimal_partition, 'should be optimal?')
                    break
        # NOT DONE YET I'M CONFUSED AND TIRED!
    
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass
