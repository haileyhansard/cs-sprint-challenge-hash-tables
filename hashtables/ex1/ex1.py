# UPER
# INPUT: weights (integers) in a list, the length of list, and the limit of weights (the sum of two weights)
    # weights = [4, 6, 10, 15, 16], 5, 21
# OUTPUT: a TUPLE of integers of the 2 INDEXES of the WEIGHTS in the list that sum to the limit.
    # Higher value should be at index 0 of output list, smaller at index 1
    # (3, 1)
    # (greater_weight_index, smaller_weight_index)

# Store each weight in list as KEYS
# Each weight's list index is its VALUE
# Trying to find the two numbers in the list whose weights sum up to the limit
# LIMIT is the number that the two "weights" should add up to.


def get_indices_of_item_weights(weights, length, limit): 
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    #keys are the weights
    #values are the indexes
    # {weight: index0, weight: index1, weight: index2}

    #enumuerate loops through the index and the elements in the 'weights' list
    #enumerate is perfect because I'm keeping track of the index and the element value
    for index, first_weight in enumerate(weights):
        #the total weight limit minus the first_weight gives us the second_weight
        print(index, first_weight)
        #assign the value of the limit - first_weight to 'second_weight' so we know what number we are looking for
        second_weight = limit - first_weight
        print(second_weight)

        #the first_weight and its index will be added to cache, and each time it iterates, it will subtract limit - first_weight and return the answer, which is the second_weight, our target for the next item we want to add to our tuple.
        #once if finds the second_weight target in the cache, it will return the first index, then the second_weights' index
        if second_weight in cache:
            return (index, cache[second_weight])
        cache[first_weight] = index
        #print(index)
        print(cache)
        print("Next iteration")

    #it will print in order of the higher index because it will already have the second_weight in the cache, so it will print its index first which will be FURTHER down the array, meaning HIGHER INDEX. Then when its done looping through the first_weights to find the missing weight that adds to sum, it's index will be entered in next in the tuple
    return None


weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
print(answer_3) #should be values 15, 6, which would be INDEXES (3, 1)

weights_hh = [10, 4, 7]
answer_hh = get_indices_of_item_weights(weights_hh, 3, 11)
print(answer_hh) #should be INDEXES (2, 1)