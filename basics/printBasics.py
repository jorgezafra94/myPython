# here we are going to see print method and its features

# custom message
print("Hello this is my first print statement")
print()

# we can have two messages separated by commas and the message is going to print the message separated by space
# this is because there is a parameter in the print method call "sep" and its default value is space
print("Hello", "My name is Jorge")
print()

# if We want We can change the value of the parameter sep
print("Hello", "My name is Jorge", sep="*")
print()

# different ways to insert a variable in a print statement
myVar = "My name is Jorge"
print("Hello %s" % myVar)
print(f"Hello {myVar}")
print("Hello {}".format(myVar))

# sometimes We need to specify what type of variable it is
print("Actual number %d" % 15)  # decimal format
print("Actual number with scientific annotation %e" % 15)  # scientific annotation
print("Actual number as floating point value %f" % 15)  # floating point annotation
print("Actual number in octal base %o" % 15)  # octal value
print("Actual number in hexadecimal base %x" % 15)  # hexadecimal value
print()

# in case of floating numbers we can limit their precision numbers
print("%f" % 5.12312312)  # by default, it will print 6 precision digits
print("%.2f" % 5.12312312)  # this configuration will print only 2 precision digits
print()

# if we want to specify a Width
print("%15d" % 541)  # by default, it is going to move to the right
# if we want to fill the rest of the number with zeros we can do this
print("%015d" % 541)
print()

# sometimes they can ask to print the sign no matter if it is positive or negative
print("%+d" % 51)
print("%+d" % -51)
print()

# as we could see the + is to show the sign but the - is to align to the left
print("%+15d" % 541)
print("%-15d" % 541)
