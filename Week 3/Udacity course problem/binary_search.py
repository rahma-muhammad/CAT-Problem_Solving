def binary_search(input_array, value):
    """Your code goes here."""
    n = len(input_array)
    left = 0
    right = n - 1
    mid = 0
    
    while left <= right:
        mid = (left+right) // 2
        guess = input_array[mid]
        if guess < value:
            left = mid + 1
        elif guess > value:
            right = mid - 1
        else:
            return mid
    return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))