"""
returns the index position of the target if found, else returns None.
Assume an ordered list
"""
import math

def Binary_Search(lst, target):
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = math.ceil((first + last) / 2)
        if (lst[mid] == target):
            return mid
        elif (lst[mid] < target):
            first = mid
        else:
            last = mid - 1
        if mid == len(lst) - 1:
            return None
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = Binary_Search(numbers, 7)
verify(result)



    
