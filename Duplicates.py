Problem: Ekta list e jei elements duibar ba beshi ase, tader ber koro.

python
Copy
Edit
nums = [1, 2, 3, 4, 2, 5, 3, 6]
duplicates = set()
seen = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates:", list(duplicates))
