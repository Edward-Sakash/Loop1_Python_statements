"""Task 3 - reverse word
Your task is to write a Python program that accepts a word from the user and reverses it, using a for loop.

Hint: the range() function accepts negative numbers!

Your results should look like this:
Input a word to reverse: hello
Reversed word: olleh"""

# Solution 1
# Prompt the user to enter a word
word = input("Input a word to reverse: ")

# Initialize an empty string to store the reversed word
reversed_word = ""

# Iterate over the characters in the word in reverse order
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

# Print the reversed word
print("Reversed word:", reversed_word)

print("_________________________________________________")

# Solution 2
# Prompt the user to enter a word
word = input("Input a word to reverse: ")

# Initialize an empty string to store the reversed word
reversed_word = ""

# Iterate over the characters in the word using a for loop
for char in word:
    reversed_word = char + reversed_word

# Print the reversed word
print("Reversed word:", reversed_word)

print("_________________________________________________")


# Solution 3 (without loop)
# Prompt the user to enter a word
"""word = input("Input a word to reverse: ")

# Reverse the word using string slicing
reversed_word = word[::-1]

# Print the reversed word
print("Reversed word:", reversed_word)"""

print("_________________________________________________")

