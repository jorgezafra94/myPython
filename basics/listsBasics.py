# the lists are a collection of values, list an hold different type of elements
# to create a list you can
a = [1, 3, "asd", 'a', ["a"]]
b = []  # empty list

# how concatenate two lists
c = [1, 5, 9, 23]
d = ['b', 'c', 'a']
e = d + c
print(e)
print()

# operator * with list
e = c * 4
print(e)
print()

# ---------------------------------- Methods
# ------------- append method
# append method help us to insert an element at the end of the list
my_list = []
print(f"Empty list - {my_list}")
my_list.append("hello")
my_list.append("bye")
my_list.append("Jorge")
my_list.append("bye")
print(f"List with elements - {my_list}")

# ------------ clear method
# this method clear the list
print(f"list with element - {my_list}")
my_lists2 = my_list.copy()
my_lists2.clear()
print(f"list without elements - {my_lists2}")
print()

# ------------ copy method
# this method help us to create a copy of a list
my_clone = my_list.copy()
print(f"copy of list - {my_clone}")

# ------------ count method
# this method help us to count how many times an element is in a list
my_count = my_list.count("bye")
print(f"original - {my_list}, count of 'bye' - {my_count}")

# -------------- extend method
# this method help us to add the elements of one list into another
# this method affects the list itself
my_second_list = ["a", 4, 5, "b"]
print(f"Original list - {my_second_list}")
my_second_list.extend(my_list)
print(f"list after extend method - {my_second_list}")
print()

# -------------- index method
# This method returns the index of an element inside a list
# if the element is more than one time in the list, it is going to return the first occurrence.
index_bye = my_second_list.index("bye")
print(f"my list is {my_second_list}, position of 'bye' element - {index_bye}")

# -------------- insert method
# this method allows us to insert an element in a specific position
print(f"my list - {my_second_list}")
my_second_list.insert(2, "new element")
print(f"with the new element in the second position - {my_second_list}")

# ----------------- pop method
# this method help us to remove an element from a list
print(f"my list - {my_second_list}")
my_second_list.pop()
print(f"after pop without index, it will remove the last element - {my_second_list}")
my_second_list.pop(3)
print(f"after pop the index 3, it will remove the element in the 3th position - {my_second_list}")
print()

# ---------------- remove method
# this method helps us to remove an element by value, it will remove the firs occurrence
print(f"my list before remove an element - {my_second_list}")
my_second_list.remove("bye")
print(f"my list after remove 'bye' element - {my_second_list}")
print()

# ----------------- reverse method
# this method reverse a list
reversed_list = my_second_list.copy()
reversed_list.reverse()
print(f"original list - {my_second_list},\nreversed list - {reversed_list}")
print()

# ----------------- sort method
# this method help us to sort a list
# we can sort a list in natural order by default without passing any parameter to the sort method
sorted_list = sorted(my_list)
print(f"original {my_list}\nSorted list by default - {sorted_list}")
print()

# if we want to sort by some logic we can create a function or method or lambda
# lambda is a easy way to create a function is like a map in JAVA
sorted_list = sorted(my_second_list, key=lambda element: len(str(element)), reverse=True)
print(f"original {my_second_list}\nSorted list by len of elements and reversed - {sorted_list}")
print()

# ---------------------------- access an element in a list
# we can access an element of a list using its position
# remember that the list begins in position 0
my_element = my_list[2]
print(f"Original list {my_list}, the element in position 2 is {my_element}")

# --------------------------- the lists are mutable
# that means that we can modify their content
print(f"original list - {my_list}")
my_list[0] = "replaced element"
print(f"changed list, we change the first element - {my_list}")
print()