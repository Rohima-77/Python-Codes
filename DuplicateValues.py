Write a Python program that creates a new list containing only the duplicate elements from the given list: [1, 5, 6, 5, 1, 2, 3].

Solve:
numbers = [1, 5, 6, 5, 1, 2, 3]
duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Duplicate Numbers:", duplicates)
