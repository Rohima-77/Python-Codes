Task: Take a number as input and print its multiplication table up to 10.
Example:
Input: 5 →

Solve:
number = int(input("Enter a number: "))
print("Multiplication of {number}: ")
for i in range(1,11):
    print(f"{number}*{i} = {number*i}")
