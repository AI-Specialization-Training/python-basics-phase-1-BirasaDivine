# Write a program that:

# Writes a function count_vowels(text) that counts how many vowels are in a string without using any built-in count methods
# Writes a function is_palindrome(text) that checks if a word is a palindrome

def count_vowel(text):
    vowels=['a','e','i','o','u']
    count=0
    for char in text:
     if char in vowels:
        count +=1
    return count

print(count_vowel("Birasa"))

def is_palindrome(text):
    text = text.lower()
    reversed_text = ""
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]
    return text == reversed_text

print(is_palindrome("racecar"))