# Write a program that:

# Creates this list:
pythonscores = [45, 78, 92, 55, 38, 81]

# Print the first and last score using indexes
# Print the total number of scores
# Print the highest and lowest score
# Add a new score 70 to the list
# Check if 92 is in the list and print the result

print(pythonscores[0],pythonscores[5])
print(len(pythonscores))
print(min(pythonscores), max(pythonscores))
result=pythonscores.append(70)
print(result)
if 92 in pythonscores :
    print(pythonscores)