# You're building a simple student report system. Instead of writing everything in one block, decompose it into small functions:

# Write a function get_grade(score) that returns:

# "A" for 90+
# "B" for 80+
# "C" for 70+
# "D" for 50+
# "F" for below 50


# Write a function print_report(name, score) that:

# Calls get_grade() internally
# Prints "Student: Birasa"
# Prints "Score: 75"
# Prints "Grade: C"


# Call print_report() with two students:

# "Birasa" with score 75
# "Alice" with score 45

def get_grade(score):
    if(score>=90):
        return("A")
    elif(score>=80):
        return("B")
    elif(score>=70):
        return("C")
    elif(score>=50):
        return("D")
    else:
        return("F")
def print_report(name, score):
    grade=get_grade(score)
    print("Student : " ,name)
    print("Score:" , score)
    print("Grade:" ,grade)

print_report("Birasa",75)