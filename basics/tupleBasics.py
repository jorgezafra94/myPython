# tuples, they are like the lists but immutable
# ----------------------- tuple creation
x = ()  # empty tuple
y = (12,)  # tuple with one element
z = tuple([1, 4, 5])  # convert a list to a tuple

# ----------------------- get an element from a tuple
print(f"Original tuple - {z}, getting element of position 1 - {z[1]}")
print(f"Original tuple - {z}, getting element of position -1 - {z[-1]}")
print()

# ----------------------- add an element into a tuple
# As we already know, the tuple is not mutable so we cant change their content
# To change elements we have to split the tuple and create a new one
tuple1 = ("a", 2, "b")
tuple2 = tuple1[:1] + ("b", 2, 4)
print(f"Original - {tuple1}, new - {tuple2}")
print()

# ----------------------- unpack a tuple
# We can unpack the tuple into elements, this is a faster way to get elements
e1, e2, e3, e4 = tuple2
print(f"from a tuple - {tuple2}, we got these elements, {e2}, {e4}, {e1}, {e3}")
print()

# ------------------------------------------------- methods
# ------------------- count
# this method returns how many times is an element in a tuple
tuplex = (4, "a", 2, "b", "a", 3)
a_count = tuplex.count("a")
print(f"my tuple - {tuplex}, number of 'a' in the tuplex - {a_count}")
print()

# ------------------- index
# this method returns the index of the first occurrence of an element
a_index = tuplex.index("a")
print(f"my tuple - {tuplex}, first index of element 'a' - {a_index}")
print()
