# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:25:11 2026

@author: mathi
"""

"""print(10 > 5)     # True
print(3 == 3)     # True
print(4 != 4)     # False
print(7 <= 2)     # False

age = 20

if age >= 18:
    print("Tu es majeur.")
    
age = 15

if age >= 18:
    print("Majeur")
else:
    print("Mineur")

note = 13

if note >= 16:
    print("Très bien")
elif note >= 12:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")

age = 25
a_le_permis = True

if age >= 18 and a_le_permis:
    print("Peut conduire")"""

nombre = int(input("Quel est ton nombre ? "))

if nombre % 2 == 0:
    print("Pair")
else:
    print("Impair")
    
age = int(input("Quel est ton âge ? "))

if age <= 12:
    print("Enfant")
elif age >= 12 and age <= 17:
    print("Adolescent")
elif age >= 18 and age <= 64:
    print("Adulte")
else:
    print("Senior")