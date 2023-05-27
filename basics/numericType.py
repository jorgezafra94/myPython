# there are 4 types of numeric variables
intType = 98
print(f"{intType} - {type(intType)}")

floatType = 19.98
print(f"{floatType} - {type(floatType)}")

complexType = 1 + 2j
print(f"{complexType} - {type(complexType)}")

# Arithmetic operations
x = 1
x += x  # x = x + 1
x -= x  # x = x - 1
x *= 2  # x =  x * 2
x /= 2  # x = x / 2
x //= 2  # x = x // 2
x **= 4  # x = x ** 4
x %= 2  # x = x % 2

# Another Way to get a number in base 10 from another base we can use int() but it has to be a String
decimal_base = int("D", 16)
print(decimal_base)