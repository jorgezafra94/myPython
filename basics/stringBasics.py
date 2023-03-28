# the Strings are one of the most used objects in python
# to build a string in python is so easy we can use single cuotes, double cuotes or triple cuotes

s1 = 'Hi everyone'  # normally we use single cuotes to char, but the char object doesnt exist here in python
s2 = "Hi everyone"
s3 = """Hi everyone"""  # these triple cuotes is important if we wantto print a message with specific format

"""
this is a block comment

\ with this back slash we can skyp special characters
\n this is a new line
\t this is tab
"""

# -------------------------------------- String methods ------------------------------------------------------------
txt = "python is FUN!"

# ---------------------------Capitalize method
x = txt.capitalize()
print(f"Original - {txt}, Capitalize method - {x}")
print()

# -------------------------- Center method
# this method help us to center a string giving a width number and an optional fill element
x = txt.center(20, '*')
print(f"Original - {txt}, Center method - {x}")
print()

# --------------------------- Count method
# this method help us to count how many times is a string inside another string
# this method has 3 parameters, 1 the string to search, 2 the start index, 3 the final index.
# this last two parameters are optional
x = txt.capitalize().count('n')
print(f"Original - {txt}, Count method with one parameter - {x}")

x = txt.capitalize().count('n', 6)
print(f"Original - {txt}, Count method with two parameters - {x}")

x = txt.capitalize().count('n', 6, 8)
print(f"Original - {txt}, Count method with three parameters - {x}")
print()

# -------------------------- Encode method
# this encodes method help us to encode a string, and pass it to bytes, it has two parameters
# 1 de base to encode by default it is UTF-8
# 2 a strategy to encode

encode = txt.encode()
print(f"Originsl - {txt}, Encode method without parameters {encode}")
encode = txt.encode(encoding="ascii")
print(f"Originsl - {txt}, Encode method with 1 parameter {encode}")
print()

# ------------------------- EndsWith method
# this method helps us to know if ome string ends with some character sequential
x = txt.endswith("FUN!")
print(f"Original - {txt}, Endswith method {x}")
x = txt.endswith("z")
print(f"Original - {txt}, Endswith method {x}")
print()

# ------------------------- Find method
# this method help us find a character sequential inside a string
# this method returns -1 if the sequential doesn't exist inside the string
# otherwise it will return the start index where the sequential begins
# furthermore it has 3 parameters
# 1 - the string to search
# 2 - the starting position to search
# 3 - the ending position to search
# the las two parameters are optionals, by default it takes 0 as it's starting point and the end of the string
# as its ending point
x = txt.find("python")
print(f"Original - {txt}, Find method with 1 parameter {x}")
x = txt.find("python", 4)
print(f"Original - {txt}, Find method with 2 parameter {x}")
x = txt.find("python", 4, 8)
print(f"Original - {txt}, Find method with 3 parameter {x}")
print()

# ----------------------------- Format method
# this method help us to insert variables in a String
x = "My name is {fname}, I'm {age}".format(fname="Jhon", age=24)
print(x)
x = "My name is {1}, I'm {0}".format("Jhon", 24)
print(x)
x = "My name is {}, I'm {}".format("Jhon", 24)
print(x)
print()

# --------------------------- Index Method
# this method works the same as find, the only difference is index method
# raise an exception if the element is not found while find return -1
x = txt.index("python")
print(f"Original - {txt}, Find method with 1 parameter {x}")
try:
    x = txt.index("python", 4)
except ValueError as e:
    x = "Exception raise so we catch to continue the program " + str(e)
print(f"Original - {txt}, Find method with 2 parameter {x}")
print()

# -------------------------- isalnum method
# this method verify if a string is composed by alphanumeric characters
# special characters doesnt count
x = txt.isalnum()
print(f"Original - {txt}, isalnum method - {x}")
other_input = "1asd455"
print(f"Original - {other_input}, isalnum method - {other_input.isalnum()}")
print()

# -------------------------- isalpha method
# this method verify if a string is composed only by letters
x = txt.isalpha()
print(f"Original - {txt}, isalpha method - {x}")
other_input = "askdhdaksj"
print(f"Original - {other_input}, isalpha method - {other_input.isalpha()}")
print()

# -------------------------- isascii method
# this method verify if a string is composed only by ascii characters
x = txt.isascii()
print(f"Original - {txt}, isalpha method - {x}")
print()

# -------------------------- isdigit method
# this method verify if a string is composed only by numbers
# + and - dont count as digits so BE CAREFUL
x = txt.isdigit()
print(f"Original - {txt}, isdigit method - {x}")
other_input = "123982"
print(f"Original - {other_input}, isdigit method - {other_input.isdigit()}")
other_input = "-123982"
print(f"Original - {other_input}, isdigit method - {other_input.isdigit()}")
print()


# --------------------------- islower method
# this method verify if all characters of a string are in lower case
x = txt.islower()
print(f"Original - {txt}, islower method - {x}")
print()

# --------------------------- isupper method
# this method verify if all characters of a string are in upper case
x = txt.isupper()
print(f"Original - {txt}, isupper method - {x}")
print()

# --------------------------- join method
# this method help us to join in a string elements from a collection
myCollection = ["1", "2", "3", "4"]
result = "*".join(myCollection)
print(f"Original - {myCollection}, join method - {result}")
print()

# -------------------------- lower method
# this method help us to transform a string into lowercase
x = txt.lower()
print(f"Original - {txt}, lower method - {x}")
print()

# -------------------------- replace method
# this method allow us to change some parts of a String
x = txt.lower().replace('n', "blabla")
print(f"Original - {txt.lower()}, replace method - {x}")
print()

# ------------------------ rfind method
# this method is the same as find but instead of bringing the first occurrence it will bring the last one
txt1 = "hello, is a greetings so hello"
normal_find = txt1.find("hello")
r_find = txt1.rfind("hello")
print(f"Original - {txt1}, normal find to word hello - {normal_find}, r-find with word hello - {r_find}")
print()

# ----------------------- rindex method
# it is the same as rfind but it raises an exception if the word or character is not found
normal_index = txt1.index("hello")
r_index = txt1.rindex("hello")
print(f"Original - {txt1}, normal index to word hello - {normal_index}, r-index with word hello - {r_index}")
print()

# ------------------------ split method
# this method help us to separate a String by a specific character and turn it into a list of elements
txt2 = "hello, my name is jorge, I want to be the best python developer, only hard work and experience could help me reach that"
split = txt2.split(",")
print(f"Original - {txt2} \n now split - {split}")
print()

# ------------------------- splitlines method
# this method help us to split a string by new lines
txt2 = "hello\nmy name is Jorge\nI want to be the best python developer\n only hard work and experience could help me reach that"
split = txt2.splitlines()
print(f"Original - {txt2} \nnow splitlines - {split}")

txt2 = """hello
my name is Jorge
I want to be the best python developer
only hard work and experience could help me reach that"""

split = txt2.splitlines()
print(f"Original - {txt2} \nnow splitlines - {split}")
print()

# --------------------------- startswith method
x = txt.startswith("pyth")
print(f"Original - {txt}, startswith method, start with 'pyth' - {x}")
print()

# -------------------------- strip method
txt3 = "                    HI                      "
x = txt3.strip()
print(f"Original - {txt3}, strip method {x}")
print()

# -------------------------- swapcase method
x = txt.swapcase()
print(f"Original - {txt}, swapcase method - {x}")
print()

# ------------------------ upper method
x = txt.upper()
print(f"Original - {txt}, upper method - {x}")
print()