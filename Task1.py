"""Task 1 - multiplication table
Your task is to write a Python program to create the multiplication table (from 1 to 10) of a number.
Number is prompted by the user.
Print results.

Some of your results could look like this:
Input a number: 6

Results of multiplication by  6:

6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60"""
print("___________________________________________________")

# Solution 1
# Prompt the user to enter a number
number = int(input("Input a number: "))

# Print the header
print("Results of multiplication by", number, ":\n")

# Iterate from 1 to 10 and calculate the product
for i in range(1, 11):
    product = number * i
    print(number, "x", i, "=", product)

print("___________________________________________________")

# Solution 2
# Prompt the user to enter a number
number = int(input("Input a number: "))

# Create the multiplication table using list comprehension
table = [f"{number} x {i} = {number * i}" for i in range(1, 11)]

# Print the results
print("Results of multiplication by", number, ":\n")
print('\n'.join(table))

print("___________________________________________________")

# Solution 3
# Prompt the user to enter a number
number = int(input("Input a number: "))

# Print the header
print("Results of multiplication by", number, ":\n")

# Iterate from 1 to 10 and calculate the product
for i in range(1, 11):
    # Calculate the product
    product = number * i
    
    # Print the multiplication equation
    print(f"{number} x {i} = {product}")

