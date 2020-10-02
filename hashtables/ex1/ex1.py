#INPUT: weights in a list, the limit of weights, and the length, all as integers
    # weights = [4, 6, 10, 15, 16]
#OUTPUT: a TUPLE of integers of two of the WEIGHTS in the list. 
    # Higher value should be at index 0, smaller at index 1
    # # (3, 1)
#Store each weight in list as KEYS
# Each weight's list index is its value
#Trying to find the two numbers in the list whose weights sum up to the limit
# LIMIT is the number that the two "packages" should add up to.


def get_indices_of_item_weights(weights, length, limit): #not working, come back to
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    index = 0

    #keys are the weights
    #values are the indexes
    for num in weights:
        if num in cache:
            cache[num, 'dupe'] = index
        else:
            cache[num] = index
        index += 1

        return cache

    for key in cache:
        if (limit - key) in weights and (limit - key) == key:
            greater_index = cache[key, 'dupe']
            smaller_index = cache[key]
            return [greater_index, smaller_index]
        if (limit - key) in weights:
            smaller_index = cache[key]
            greater_index = cache[limit - key]
            return [greater_index, smaller_index]


    return None


weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
print(answer_3) #should be (15, 6)