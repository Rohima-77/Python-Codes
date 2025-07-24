Example: 6 → 1 + 2 + 3 = 6


num = int(input("Enter a number: "))
sum_divisors = sum(i for i in range(1, num) if num % i == 0)

print("Perfect number" if sum_divisors == num else "Not perfect")
