# Write a program that:

# Writes a function find_smallest(numbers) that finds the smallest number without using min()
# Writes a function linear_search(items, target) that returns the index of the target or -1 if not found
# Test both functions with:
pythonnumbers = [45, 78, 12, 92, 33, 67]

def find_smallest(numbers):
    for num in pythonnumbers:
        if(num[i]>num[i-1]):
            biggestnum=num[i]
        else :
            biggestnum=num[i-1]
            return biggestnum