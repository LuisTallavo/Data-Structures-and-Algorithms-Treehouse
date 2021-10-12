import random

"""
Merge Sort Algorithm 2
"""

numbers = []
attempts = 0
sorted_vals = []

number_of_values = int(input("Please enter the number of values you would like to Merge Sort: "))

for i in range(number_of_values):
    numbers.append(random.randint(0,10))

print(numbers)

def Merge_Sort(values):
    if len(values) <= 1:
        return values

    mid = len(values)//2

    left_half = Merge_Sort(values[:mid])
    right_half = Merge_Sort(values[mid:])

    sorted_vals = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_vals.append(left_half[left_index])
            left_index += 1
        else:
            sorted_vals.append(right_half[right_index])
            right_index += 1

    sorted_vals += left_half[left_index:]
    sorted_vals += right_half[right_index:]

    return sorted_vals

print(Merge_Sort(numbers))
