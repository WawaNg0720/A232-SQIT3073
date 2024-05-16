# Create a tuple
fruits = ("apple", "orange", "strawberry", "grape")
print(fruits)

# Access elements by index
third_fruit = fruits[2]
second_fruit = fruits[1]

# Iterate through the tuple
print("Fruits:")
for fruit in fruits:
    print(fruit)

# Check if an element is in the tuple
contains_cherry = "cherry" in fruits

# Find the length of the tuple
num_fruits = len(fruits)

# Concatenate two tuples
more_fruits = ("cherry", "kiwi")
all_fruits = fruits + more_fruits

# Nested tuple
nested_tuple = (1, (2, 3))

# Print the results
print("Third fruit:", third_fruit)
print("Second fruit:", second_fruit)
print("Does it contain 'cherry'? ", contains_cherry)
print("Number of fruits:", num_fruits)
print("All fruits:", all_fruits)
print("Nested tuple:", nested_tuple)