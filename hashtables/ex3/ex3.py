#UPER
#Input: 'arrays' list that contains sub-lists of integers
#Output: 'result' list that contains the numbers that exist in all sub-lists

#Trying to find the number(s) that appear(s) in all of the sub-lists in the list. 
#Once it is found in multiple lists, add it to the count
#Use dictionary or hash tables to solve


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    match = len(arrays)
    result = []

    for each_list in arrays:
        #check the elements inside each list
        for each_num in each_list:
            # check if the number isn't in the cache yet
            if each_num not in cache:
                #if the value is not yet in cache, set it to 1
                cache[each_num] = 1
            #otherwise, its already in cache, so increment the counter
            else:
                cache[each_num] += 1
    
    #check the keys in the cache dict to see if key appears as many times as length of arrays
    #because the key must be present in all sub-arrays in order to be appended to result list
    #so if the key is found an equal number of times as the length of arrays, it must be in all sub-arrays
    for each_key in cache:
        if cache[each_key] == match:
            #add that key to the 'result' list
            result.append(each_key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
