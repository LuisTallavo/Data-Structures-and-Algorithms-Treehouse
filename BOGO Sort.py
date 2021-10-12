import random

"""
BOGO sort randomely rearranges the list of values until its sorted
Obviously very inefficient
"""
numbers = []
attempts = 0
sorted_vals = []

number_of_values = int(input("Please enter the number of values you would like to BOGO sort: "))

for i in range(number_of_values):
    numbers.append(random.randint(0,10))

print(numbers)

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        random.shuffle(values)
        attempts += 1
    return values, attempts

sorted_vals, attempts = bogo_sort(numbers)
print(sorted_vals)
print("Number of attempts to randomely shuffle into order: ", attempts)
        
