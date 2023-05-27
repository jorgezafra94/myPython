def average(sequence):
    return sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (1, 2, 3, 4, 5)},
    {"name": "Dan", "grades": (1, 12, 3, 10)}
]

for student in students:
    print("student {}, its average is {}".format(student["name"], average(student["grades"])))

# --------------------------------------------- LAMBDA ----------------------------------------------

average_pro = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (1, 2, 3, 4, 5)},
    {"name": "Dan", "grades": (1, 12, 3, 10)}
]

for student in students:
    print("student {}, its average is {}".format(student["name"], average(student["grades"])))
