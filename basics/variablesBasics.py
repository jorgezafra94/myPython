# variables, in python we dont need to specify the type they are dynamic variables
# We can change the type everytime we want
name = "Juan"
name = 90
name = [1, 5, 8]

# multiple assignment same value
var1 = var2 = var3 = "Value"
print("{}, {}, {}".format(var1, var2, var3))
print()

# multiple assignment different values
a, b = 14, "other"
print("{}, {}".format(a, b))
print()

# pythonic ways to write a value
x = 5000000
print(x)
x = 5_000_000
print(x)
print()

x = 0.35
print(x)
x = .35
print(x)
print()

x = 10000.0
print(x)
x = 10e3
print(x)
print()

# Swap variable values
x = 23
y = 60
print(f"{x}, {y}")
x, y = y, x
print(f"{x}, {y}")
