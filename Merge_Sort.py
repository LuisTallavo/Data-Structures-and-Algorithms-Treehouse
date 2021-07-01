"""
sorts a list in ascending order O(nlogn)
"""
def merge_sort(lst):
    # Base Case
    if len(lst) <= 1:
        return lst

    mid = len(lst)//2
    left_half = lst[:mid]
    right_half = lst[mid:]
    
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    merged_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    while i < len(left):
        merged_list.append(left[i])
        i += 1

    while j < len(right):
        merged_list.append(right[j])
        j += 1
        
    return merged_list


def verify_sorted(lst):
    n = len(lst)
    if n == 0 or n == 1:
        return True

    return lst[0] < lst[1] and verify_sorted(lst[1:])
