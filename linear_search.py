"""
returns the index position of the target if found, else returns None.
"""
def linear_search (lst, target):
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return None
    

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 9)
verify(result)
