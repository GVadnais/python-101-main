# What data type is the variable `mystery` at the end of the script?            float
# What data types does it hold at certain points earlier in the script?         NoneType, string, integer

mystery = None
x = 1

print("type", x, "is", type(mystery))
x = x + 1
mystery = "Sommerfeld"
print("type", x, "is", type(mystery))
x = x + 1
mystery = 137
print("type", x, "is", type(mystery))
x = x + 1
mystery = mystery + 0.0
print("type", x, "is", type(mystery))

##questions : why do I get a space after type in my results ?