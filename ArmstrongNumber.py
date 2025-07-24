Example: 153 = 1³ + 5³ + 3³ = 153

python
Copy
Edit
num = int(input("Enter a number: "))
digits = len(str(num))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

print("Armstrong" if total == num else "Not Armstrong")
