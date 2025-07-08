Task: Take a string and count the number of vowels (a, e, i, o, u).
Example:
Input: "sunny" → Output: 1

Solve:
a = 'sunny'
vowels = "aeiou"
count = 0
for i in a:
    if i in vowels:
        count+=1
        print(count)
        
