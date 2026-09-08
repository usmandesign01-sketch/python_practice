class Employe:
    salary = 12300
    language = "Py"

usman = Employe()
print(f"language is {usman.language}\nsalary is {usman.salary}")

print("\n")

kamran = Employe()
kamran.language = "JavaScript"
print(f"language is {kamran.language}\nsalary is {kamran.salary}")