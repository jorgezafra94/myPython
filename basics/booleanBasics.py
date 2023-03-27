# bool values there are only two values True and False
x = True
y = False

# We can get bool values from any kind of element
# If there is somo 0, or empty collection or empty string we can get a False otherwise it is a True
b1, b2, b3 = bool(0), bool(""), bool([])
b4, b5, b6 = bool(5), bool("poi"), bool(["a", 98])
print(f"all False b1:{b1} - b2:{b2} - b3:{b3}")
print(f"all True b4:{b4} - b5:{b5} - b36:{b6}")

print(dir(b1))


