import random

"""
Quick Sort Algorithm
"""

numbers = []
attempts = 0
sorted_vals = []

number_of_values = int(input("Please enter the number of values you would like to Quick sort: "))

for i in range(number_of_values):
    numbers.append(random.randint(0,10))

print(numbers)


def QuickSort(values):
    if len(values) <= 1:
        return values
    pivot = values[0]
    less_than_pivot = []
    greater_than_pivot = []

    for i in values[1:]:
        if i <= pivot:
            less_than_pivot.append(i)
        else:
            greater_than_pivot.append(i)

    return QuickSort(less_than_pivot) + [pivot] + QuickSort(greater_than_pivot)

print(QuickSort(numbers))
