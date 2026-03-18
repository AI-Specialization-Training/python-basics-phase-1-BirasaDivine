# Write a program that:

# Writes a function find_smallest(numbers) that finds the smallest number without using min()
# Writes a function linear_search(items, target) that returns the index of the target or -1 if not found
# Test both functions with:
pythonnumbers = [45, 78, 12, 92, 33, 67]

def find_smallest(numbers):
    smallest = numbers[0]       
    for num in numbers:
        if num < smallest:       
            smallest = num       
    return smallest             

def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i             
    return -1      