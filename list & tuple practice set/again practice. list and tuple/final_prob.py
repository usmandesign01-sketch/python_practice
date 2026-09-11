'''🔥 Day 2 Final Challenge

Create a program for 5 students' marks.

Example:

marks = [78, 65, 91, 54, 88]

Your program should print:

All marks: [...]
Total: ...
Average: ...
Highest: ...
Lowest: ...
Number of students: ...

Then add one more student's marks and print the updated list and new average.'''

marks = [78, 65, 91, 54, 88]
print(f"Total Marks: {sum(marks)}")
print(f"Avg Marks: {sum(marks)/len(marks)}")
print(f"Highest Marks: {max(marks)}")
print(f"Smallest Marks: {min(marks)}")
print(f"Total student: {len(marks)}")
# adding one more student
marks.append(100)
print(f"Updated list {marks}")
print(f"Updated avg {sum(marks)/len(marks)}")