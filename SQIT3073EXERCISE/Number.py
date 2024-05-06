# Get user input for integer and floating-point number
x = int(input("Please enter a number for x:"))
y = float(input("Please enter a number for y:"))
z = int(input("Please enter a number for z:"))

# Perform arithmetic operations
sum_xy = x + y
difference_xy = x - y
product_xy = x * y
quotient_xy = x / y
modulus_xy = x % y
exponentiation_xy = x ** y

# Print the results
print("x + y = ", sum_xy)
print("x - y = ", difference_xy)
print("x * y = ", product_xy)
print("x / y = ", "{:.2f}".format(quotient_xy))
print("x % y = ", modulus_xy)
print("x ** y = ", exponentiation_xy)

# Combine Operators
combine_xyz = (x + y) - z ** y
print("(x + y) - z ** y = ",combine_xyz)

# Use built-in functions for numerical operations
absolute_z = abs(z)
rounded_y = round(y)
max_value = max(x, y, z)
min_value = min(x, y, z)

print("Absolute value of z:", absolute_z)
print("Rounded value of y:", rounded_y)
print("Max value:", max_value)
print("Min value:", min_value)

# Import the math module for more advanced math operations
import math

square_root_y = math.sqrt(y)
logarithm_base_10_x = math.log10(x)
factorial_z = math.factorial(abs(z))

print("Square root of y:", square_root_y)
print("Logarithm base 10 of x:", logarithm_base_10_x)
print(f"Factorial of |z| ({abs(z)}):", factorial_z)



#Exercise1forNumberSQIT3073