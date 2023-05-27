def division(x, y):
    return x / y

def multiplication(x, y):
    return x * y
1
def addition(x, y):
    return x + y

operations = {
    "div": division,
    "mul": multiplication,
    "sum": addition
}

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
user_operation = input("Enter div(division), mul(multiplication), sum(addition): ")

print("the result is: {}".format(operations.get(user_operation)(num1, num2)))