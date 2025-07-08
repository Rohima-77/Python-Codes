Task: Print the first n numbers in the Fibonacci series using a loop.
Example:
Input: 5 → Output: 0 1 1 2 3

Solve:
number = int(input("Enter a fibonacci number: "))
a = 0
b = 1
print("finbonacci series: ")
for i in range(number):
    print(a,end=" ")
    a,b=b,a+b
