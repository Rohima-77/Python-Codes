Task: Take a number and calculate the sum of its digits using a loop.
Example:
Input: 1234 → Output: 10

Solve:
number = 1234
total = 0

while number>0:
    total+=number%10
    number=number//10
    print("sum of total numbers: ",total)
