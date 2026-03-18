# Your Practice Question
# Write a program that:

# Generates and prints a random number between 1 and 100
# Creates this list:

pythonstudents = ["Alice", "Birasa", "Charlie", "Diana", "Eve"]

# Picks and prints one random student
# Picks 3 unique random students using sample()
# Shuffles the list and prints it
# Use seed(10) at the top — so your results are predictable

import random as random
random.seed(10)
print(random.randint(1,100))
print(random.choice(["Alice", "Birasa", "Charlie", "Diana", "Eve"]))
print(random.sample(pythonstudents, k=3))
print(random.shuffle(["Alice", "Birasa", "Charlie", "Diana", "Eve"]))