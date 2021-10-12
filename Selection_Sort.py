import random

"""
Selection Sort
"""

numbers = []
attempts = 0

number_of_values = int(input("Please enter the number of values you would like to Selection Sort: "))

for i in range(number_of_values):
    numbers.append(random.randint(0,10))

print(numbers)

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def selection_sort(values):
    attempts = 0
    if len(values) > 0:
        minval = values[0]
    sorted_vals = []
    while len(values) > 0:
        attempts += 1
        for i in values:
            if i < minval:
                minval = i
        sorted_vals.append(minval)
        values.remove(minval)
        if len(values) > 0:
            minval = values[0]
    return sorted_vals, attempts



sorted_vals, attempts = selection_sort(numbers)
print(sorted_vals)
print("Number of attempts to selection sort into order: ", attempts)
        
