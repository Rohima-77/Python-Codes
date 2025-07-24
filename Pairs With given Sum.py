Problem: Ekta list e jodi target sum thake, se sum banay emon sob pairs ber koro.
Solve:

nums = [2, 4, 3, 5, 7, 8, 1]
target = 9
pairs = []

seen = set()
for num in nums:
    diff = target - num
    if diff in seen:
        pairs.append((num, diff))
    seen.add(num)

print("Pairs:", pairs)
