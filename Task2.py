"""Task 2 - pattern with loop
Your task is to write a Python program to construct the following pattern, using a for loop.

Note: Don't type numbers manually. Use the loop!

Your results should look like this:
1
22
333
4444
55555
666666
7777777
88888888
999999999"""

# Solution 1

# Use a for loop to iterate from 1 to 9
for i in range(1, 10):
    # Repeat the current number i times
    pattern = str(i) * i
    
    # Print the pattern
    print(pattern)

print("___________________________________________")

# Solution 2

# Use nested loops to construct the pattern
for i in range(1, 10):
    # Inner loop to repeat the current number i times
    for _ in range(i):
        print(i, end="")
    print()

print("___________________________________________")

# Solution 3

# Use a single loop to construct the pattern
pattern = ""
for i in range(1, 10):
    pattern += str(i) * i + "\n"

# Print the pattern
print(pattern)
