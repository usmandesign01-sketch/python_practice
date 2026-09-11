'''Problem 4 — Marks

Create:

marks = [75, 46, 25, 63, 80]

Find:

Total
Average
Highest mark
Lowest mark

You can use Python's built-in:

sum()
max()
min()
len()'''

marks = [75, 46, 25, 63, 80]

print(f"Total Marks: {sum(marks)}")
print(f"Avg Marks: {sum(marks)/len(marks)}")
print(f"Highest Marks: {max(marks)}")
print(f"Smallest Marks: {min(marks)}")