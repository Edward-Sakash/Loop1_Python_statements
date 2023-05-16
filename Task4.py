"""ask 4 - upper letters
Your task is to write a Python program using for loop, that iterates over given string and changes every occurence of 'o' letter into big letter 'O'.

Hint: use one of the string's method!

Note: You can use any text, for example from lyrics. My was "Hello, I love you, won't you tell me your name?" 😃

Your results should look like this:
 HellO, I lOve yOu, wOn't yOu tell me yOur name?"""

# Solution 1
# Define the input string
text = "Ukraine said all 18 missiles were shot down and footage showed air defences destroying targets over the city."

# Iterate over each character in the string using a for loop
modified_text = ""
for char in text:
    # Check if the character is 'o' (lowercase)
    if char == 'o':
        # Replace 'o' with 'O' (uppercase)
        char = 'O'
    modified_text += char

# Print the modified string
print(modified_text)

print("______________________________________________________")

# Solution 2
# Define the input string
text = "Hello, I love you, won't you tell me your name?"

# Initialize an empty string to store the modified text
modified_text = ""

# Iterate over each character in the string using a for loop
for char in text:
    # Check if the character is 'o' (lowercase)
    if char == 'o':
        # Replace 'o' with 'O' (uppercase) and concatenate to the modified text
        modified_text += 'O'
    else:
        # Append the character as it is to the modified text
        modified_text += char

# Print the modified text
print(modified_text)

print("______________________________________________________")

# Solution 3
# Define the input string
text = "Hello, I love you, won't you tell me your name?"

# Initialize an empty string to store the modified text
modified_text = ""

# Iterate over each character in the string using a for loop
for char in text:
    # Check if the character is 'o' (lowercase)
    if char == 'o':
        # Convert 'o' to uppercase using the upper() method and concatenate to the modified text
        modified_text += char.upper()
    else:
        # Append the character as it is to the modified text
        modified_text += char

# Print the modified text
print(modified_text)
