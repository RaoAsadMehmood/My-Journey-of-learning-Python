# Operators in Python

# In Python, operators are symbols that execute operations on variables and values. Python supports a variety of operators:



# 1. Arithmetic Operators: Used for fundamental math operations.

a = 10
b = 5


# Addition
print(a + b)   

# Subtraction
print(a - b)

# Multiplication
print(a * b)

# Division
print(a / b)

# Modulus
print(a % b)

# Exponentiation
print(a ** b)

# Floor Division
print(a // b)



# 2. Comparison (Relational) Operators
# Used to compare two values.

print(a == b)   
print(a != b)   
print(a > b) 
print(a < b)
print(a >= b)
print(a <= b)




# 3. Logical Operators
# Used to combine conditional statements.

x:bool = True
y:bool = False

print( x and y)
print( x or y)
print(not x)



# 4. Assignment Operators
# Used to assign values to variables.

x: int = 5

x += 3
print(x)


x -= 3
print(x)

x *= 3
print(x)

x /= 3  
print(x)

x %= 3
print(x)

x //= 3
print(x)

x **= 3 
print(x)


# 5. Identity Operators (is): are used to compare memory locations.
# Operator Name Example:
# Returns If two items have the same memory location, x is the same as y. 
# Otherwise, they are not.
# Returns True if objects do not share the same memory location (x is not y).

x:list = ["apple", "banana"]
y:list = ["apple", "banana"]
z:list = x

print(x is z)
print(x is y)
print(x == y)
print (x is not y)


# 6. Membership Operators (in): are used to test if a sequence is present in an object.
# Operator Name Example:    

fruits = ["apple", "banana", "mango"]

print("banana" in fruits)  # Output: True
print("grapes" in fruits)  # Output: False

# 7. Bitwise Operators: are used to compare binary numbers.
# Operator Name Example:    

a = 60
b = 13  