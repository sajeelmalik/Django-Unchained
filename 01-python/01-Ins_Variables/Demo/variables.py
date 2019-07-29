"""
This is a multiline comment! You can say whatever you want in here.
It accounts for line breaks
"""

# Variables
###################################################################
# variables in python, unlike javascript, do not need variable assignment
# print() is equivalent to console.log()

# Creates a variable with a string "Kitkat"
title = "Kitkat eater"

# Creates a variable with an integer 80
years = 80

# Creates a variable with the boolean value of True
expert_status = True

# Prints a statement adding the variable
print("Danny is a professional " + title)

# Convert the integer years into a string and prints
print("He has been coding for " + str(years) + " years")

# Converts a boolean into a string and prints
print("Expert status: " + str(expert_status))

# An f-string accepts all data types without conversion
# f-strings are similar to template literals within javascript
print(f"Expert status: {expert_status}")

# Interesting stuff - operations

 # Normal division
print(42 / 8)

# `Floor` division - we round DOWN to the nearest integer. A built-in Math.floor
print(42 // 8) 

# Exponentiation - for (a ** b), we bring a to the exponent of b, or a^b
print(23 ** 2) 

