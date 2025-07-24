Problem: Ekta 9-digit row valid kina check koro (i.e. 1-9 shob ase kina, repeat chara).
Example: [5,3,4,6,7,8,9,1,2] ➝ valid


def is_valid_sudoku_row(row):
    return sorted(row) == list(range(1, 10))

row = list(map(int, input("Enter 9 numbers (1-9) separated by space: ").split()))

if len(row) != 9:
    print("Invalid input! Must be 9 numbers.")
else:
    print("Valid row" if is_valid_sudoku_row(row) else "Invalid row")
