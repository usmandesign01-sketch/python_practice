'''Problem 6 — Tuple

Create a tuple containing:

your name
your age
your city
your class

Print each item separately using indexing.

Then try to change the age.

For example:

student[1] = 19

Observe the error.

The goal is to understand why the error happens.'''
# ********************************************************************************
info = ("Usman Khan", "20", "Mingora", "Class 12")
print(info[0])
print(info[1])
print(info[2])
print(info[3])
# info[1] = 21 # This will through error because the tuple is immutable