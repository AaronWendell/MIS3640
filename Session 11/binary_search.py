def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list

    my_list: an ordered list of numbers from smallest to largest

    x: a number

    returns the index of x if x is in my_list, None if not.
    '''
    
    # Set the lower to the first index of the list, the upper to the last, and the middle to the average of them
    lower = 0
    upper = len(my_list) - 1
    middle = int((upper + lower) / 2)
    

    # Check that the split has not resulted in only two indexes for the three variables
    # If there are only two values, the loop could get stuck when the upper index holds the value we are looking for
    # (because we round down when assigning middle)
    # Every time we redefine the bounds of the range, we set the new middle to the average of upper and lower 
    while (upper - lower > 1):
        if(my_list[middle] == x):
            return middle
        elif(my_list[middle] < x):
            lower = middle
            middle = int((upper + lower) / 2)
        elif(my_list[middle] > x):
            upper = middle
            middle = int((upper + lower) / 2)

    # When there are less than 3 values left, we can simply check if the value is held by the upper or lower index
    # and return the corresponding index, and if it is not in the list, return None
    if (my_list[upper] == x):
        return upper
    elif (my_list[lower] == x):
        return lower
    else:
        return None


test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None
