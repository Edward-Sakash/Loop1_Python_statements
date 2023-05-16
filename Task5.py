"""Task 5 - count digits and letters
Your task is to write a Python program using for loop, that counts digits and letters.
User should be prompted to enter her/his characters with the keyboard, even without looking at it.
Store the information about number of digits and letters in some variables.

Hint: use one of the string's method and try to type only letters and digits!

Your results could look like this:
Input your characters: dgbudf8gsdf7g8sd7fg7dsf7g7y7df7ygsdfg775uybgfbfdug8fdsugdfsguf7g7df7g7ydf7yg7rye7gy7eryg
Number of digits:  21
Number of letters:  67 """

# Solution 1
# Prompt the user to enter characters
characters = input("Input your characters: ")

# Initialize variables to store the count of digits and letters
digit_count = 0
letter_count = 0

# Iterate over each character in the input using a for loop
for char in characters:
    # Check if the character is a digit using the isdigit() method
    if char.isdigit():
        digit_count += 1
    # Check if the character is a letter using the isalpha() method
    elif char.isalpha():
        letter_count += 1

# Print the counts of digits and letters
print("Number of digits:", digit_count)
print("Number of letters:", letter_count)

print("_____________________________________________")

# Solution 2
# Prompt the user to enter characters
characters = input("Input your characters: ")

# Initialize variables to store the count of digits and letters
digit_count = 0
letter_count = 0

# Iterate over each character in the input using a for loop
for char in characters:
    # Check if the character is a digit
    if '0' <= char <= '9':
        digit_count += 1
    # Check if the character is a letter
    elif char.isalpha():
        letter_count += 1

# Print the counts of digits and letters
print("Number of digits:", digit_count)
print("Number of letters:", letter_count)

