# Create a list of numbers
numbers = [2, 4, 6, 8, 10, 10]
print(numbers)

numbers.remove(10)
print(numbers)

# Print the list
print("Original list:", numbers)

# Access elements by index
first_element = numbers[0]
print("The first element is:", first_element)

# Slice the list to get a subset
subset = numbers[1:4]
print("Subset of the list:", subset)

# Modify an element in the list
numbers[2] = 1
print("Modified list:", numbers)

# Append (add) an element to the end of the list
numbers.append(12)
print("List after appending 12:", numbers)

# Remove an element by value
numbers.remove(1)
print("List after removing 1:", numbers)

# Find the index of an element
index_of_12 = numbers.index(12)
print("Index of 12:", index_of_12)

# Check if an element is in the list
contains_11 = 11 in numbers
print("Does the list contain 11?", contains_11)

# Sort the list
numbers.sort()
print("Sorted list:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)
