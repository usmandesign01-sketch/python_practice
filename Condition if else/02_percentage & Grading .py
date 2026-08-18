
# percentage and grading system for students marks

total_marks = 1200

marks_obtained = int(input("Enter the marks obtained by the student: "))

percentage = (marks_obtained / total_marks) * 100 

if marks_obtained < 0 or marks_obtained > total_marks:
    print("\n")
    print("Invalid marks entered. Please enter marks between 0 and", total_marks)
else:
    print("Your percentage is :", percentage)

   
if percentage > 100:
    print("Invalid percentage calculated. Please check the marks entered.")

elif percentage >= 90:
    print("Grade: A+")

elif percentage >= 80:
    print("Grade: A")

elif percentage >= 70:
    print("Grade: B")

elif percentage >= 60:
    print("Grade: C")

elif percentage >= 50:
    print("Grade: D")

else:
    print("Grade: F")