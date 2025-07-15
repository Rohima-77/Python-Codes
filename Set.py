
Write a Python program that takes two sets from the user and computes their union, intersection, and difference.

A = {1, 2, 3, 4, 5}

B = {4, 5, 6, 7, 8}

Solve:

First_set = input("Enter Set A: ")
Second_set = input("Enter Set B: ")

A = set(map(int, First_set.split(',')))
B = set(map(int, Second_set.split(',')))

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
