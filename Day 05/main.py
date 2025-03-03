# Dictionaries in Python 
# Introduction to Dictionaries
# A dictionary is a collection of key-value pairs.
# It is: # Ordered (since Python 3.7): Items are stored in the order they were inserted.
# Mutable: Items can be added, removed, or modified after the dictionary is created. 
# Un-indexed: Items are accessed using keys, not indices.
# Without duplicates: Keys must be unique, but values can be duplicated.
# Before Python 3.7, dictionaries were unordered, meaning that items were not stored in a specific order.
# However, with the introduction of Python 3.7, dictionaries now maintain their insertion order.
# OrderedDict vs dict in Python: The Right Tool for the Job 
# 2. Creating a Dictionary # Dictionaries are created using curly braces {} with key-value pairs separated by commas. 
#  The syntax is:

student : dict =  {
"name":"Rao Asad Mehmood",
"age" : "20",
"courses" : "Web & App development"
}



# 3. Accessing Values
# You can access the value associated with a key using square brackets [] or the get() method.

# Example Code:
print(student["name"])
print(student.get("name"))


# Modifying a Dictionary
# You can add new key-value pairs or modify existing ones.

# Example Code:
student["name"] = "Saad Naseem"
print(student["name"])



# 5. Deleting Items
# You can remove a key-value pair using the del keyword or the pop() method.

# Note that pop() returns the value of the removed key-value pair, whereas del does not return anything.

# You can also use pop() with a default value, in case the key is not found in the dictionary:

# Example Code:

student.pop("age")
print(student)