'''🔥 Problem 2 — Student Marks

Create:

marks = [78, 45, 91, 33, 67, 88, 52]

Using a loop:

Print each mark
Print "Pass" if mark >= 50
Print "Fail" if mark < 50
Count total passed students
Count total failed students'''


marks = [78, 45, 91, 33, 67, 88, 52]
passed_std = 0
failed_std = 0

for num in marks:

    if num >= 50:
        passed_std = passed_std + 1
        print(f"Pass: {num}")
    else:
        failed_std = failed_std + 1
        print(f"Fail: {num}")

print(f"Total passed students: {passed_std}")
print(f"Total failed students: {failed_std}")