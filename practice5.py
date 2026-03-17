# Write a program that:

# Creates this list:
pythonscores = [45, 78, 92, 55, 38, 81]

# Loop through the list and print each score
# Loop through again and print only scores above 50
# Use range() to print numbers from 1 to 10
# Use enumerate() to print each score with its index
for numbers in pythonscores:
  print(numbers)
print("------------------------------------")
for i in range(10):
 print(i)
print("------------------------------------")
for number in pythonscores:
  if number>50 :
    print(number)
    print("------------------------------------")
for index,number in enumerate(pythonscores):
  print(index,number)