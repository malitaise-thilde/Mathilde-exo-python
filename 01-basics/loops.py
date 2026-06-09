# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:57:21 2026

@author: mathi
"""

"""for i in range(5):
    print(i)        # affiche 0, 1, 2, 3, 4

for prenom in ["Emma", "Hugo", "Chloé"]:
    print(f"Bonjour {prenom}")
    
total = 0

for i in range(1, 11):
    total = total + i

print(total)        # 55

compteur = 3

while compteur > 0:
    print(compteur)
    compteur = compteur - 1

print("Décollage !")"""

nombre = int(input("Quel est ton nombre ? "))

total = 0

for i in range(1, nombre):
    total = total + i

print(total)