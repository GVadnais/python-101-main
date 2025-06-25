# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

# 1)
number_of_potatoes = 2
print(type(number_of_potatoes))
number_of_potatoes = float(number_of_potatoes)
print(type(number_of_potatoes))

# 2)
number_of_potatoes = int(number_of_potatoes)
print(type(number_of_potatoes))

# 3)
result = 2 / 1.0 
print(result)

# 4)
variable1 = 2
variable2 = 4
variable3 = variable1 * variable2

print(variable3)


#from float to int, we lose the decimals
