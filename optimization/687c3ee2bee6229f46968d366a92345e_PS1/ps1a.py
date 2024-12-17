###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:
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

    result = {}
    with open('ps1_cow_data.txt', 'r') as file:
        for line in file:
            name, weight = line.strip().split(',')
            result[name] = weight

    return result

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
    trips = []

    work = cows.copy()
    sort = sorted(work.items(), key=lambda x: x[1], reverse=True)

    while len(sort) > 0:
        trip = []
        remaining_limit = limit
        for name, weight in sort[:]:
            if int(weight) <= remaining_limit:
                trip.append(name)
                remaining_limit -= int(weight)
                sort.remove((name, weight))

        trips.append(trip)

    return trips


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
    working = cows.copy()

    names = [item[0] for item in working.items()]

    partitions = get_partitions(names)

    allowed = []

    for variant in partitions:
        valid = True
        for trip in variant:
            weight = sum(int(working[name]) for name in trip)
            if weight > limit:
                valid = False
                break
        if valid:
            allowed.append(variant)

    if allowed:
        shortest = min(allowed, key=len)
        return shortest
    else:
        return None

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
    cows = load_cows('ps1_cow_data.txt')
    time_greedy_start = time.time()
    result_greedy = greedy_cow_transport(cows, limit=10)
    time_greedy = time.time() - time_greedy_start
    greedy_len = len(result_greedy)

    print(f"Greedy Cow Transport Algorithm: {greedy_len}, Time: {time_greedy:.2f}")

    time_brute_force_start = time.time()
    result_brute = brute_force_cow_transport(cows, limit=10)
    time_brute = time.time() - time_brute_force_start
    brute_force_len = len(result_brute)

    print(f"Brute-Force Cow Transport Algorithm: {brute_force_len}, Time: {time_brute:.2f}")



compare_cow_transport_algorithms()



