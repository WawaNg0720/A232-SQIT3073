# Define a string variable
message = "Good Morning Everyone!"

# Print the string
print(message)

# Access characters in the string (include space)
print("The third character until seventh character for the string is:", message[3 : 7])

# Find the length of the string
length = len(message)
print("The length of the string is:", length)

# Get user input for the name
name = input("Enter your name: ")
age = input("Enter your age: ")

print("The age for " + name + " is " + age)

# Concatenate (combine) two strings
greeting = "Hello, " + name + " ^-^"
print(greeting)

# Use string methods
lowercase_message = greeting.lower()
print("Lowercase message:", lowercase_message)

# Check if a substring is in the string
contains_Morning = "Morning" in message
print("Does the message contain 'Morning'? ", contains_Morning)

# Replace part of the string
new_message = message.replace("Morning", "Afternoon")
print("Updated message:", new_message)

#Exercise1forStringSQIT3073