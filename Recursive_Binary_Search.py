"""
returns the index position of the target if found, else returns None.
Assume an ordered list
"""
import math

def Recursive_Binary_Search(lst, target):
    if len(lst) == 0:
        return False
    else:
        mid = len(lst)//2

        if lst[mid] == target:
            return True
        else:
            if lst[mid] < target:
                return Recursive_Binary_Search(lst[mid + 1:], target)
            else:
                return Recursive_Binary_Search(lst[:mid], target)
def verify(result):
    print("The target was found: ", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = Recursive_Binary_Search(numbers, 15)
verify(result)

