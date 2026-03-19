# Write a program with this list:
pythonscores = [45, 78, 92, 55, 38, 81, 100, 23]

# Loop through and use break to stop when you hit a score above 90
# Loop through and use continue to skip any scores below 50, print the rest
# Write an empty function called calculate_bonus using pass as placeholder

for number in pythonscores:
    if(number>90):
        break
    print(number)

for number in pythonscores:
    if(number<50):
        continue
    print(number)