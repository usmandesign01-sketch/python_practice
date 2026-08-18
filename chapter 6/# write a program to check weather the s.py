# write a program to check weather the students are paassed or fail. minimum requirement is 33%
total_marks = 600

english = 100
pysics  = 100
urdu    = 100
math    = 100
islamyat = 100
m_quran = 50
pak_study = 50


english = int(input("English sujbect marks : "))
pysics = int(input("pysics sujbect marks : "))
urdu = int(input("Urdu sujbect marks : "))
math = int(input("Math sujbect marks : "))
islamyat = int(input("Islamyat sujbect marks : "))
pak_study = int(input("Pak_Study sujbect marks : "))
m_quran = int(input("m_quran sujbect marks : "))

obtain_marks = ("Total Marks: ",english + pysics + urdu + math + islamyat + pak_study + m_quran)
print(obtain_marks)

percentage = (total_marks\obtain_marks) * 100

if percentage < 33:
    print("You FAIL ")
else:
    print("You PASS")
