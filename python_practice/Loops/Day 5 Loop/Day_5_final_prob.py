'''🔥 DAY 5 FINAL CHALLENGE
Student Marks Analyzer  

----- Marks Analysis -----

Marks: [45, 78, 92, 33, 67, 88, 51, 76]

Total: 530
Average: 66.25
Highest: 92
Lowest: 33
Passed: 6
Failed: 2

'''

marks = [45, 78, 92, 33, 67, 88, 51, 76]
total = 0
for mark in marks:
    total = total + mark

print(f"Total: {total}")
print(f"Average: {total / len(marks)}")
print(f"Highest: {max(marks)}")
print(f"Lowest: {min(marks)}")

passed_students = 0
failed_students = 0
for mark in marks:
    if mark >= 50:
        passed_students = passed_students + 1
    else:
        failed_students = failed_students + 1

print(f"Passed: {passed_students}")
print(f"Failed: {failed_students}")

