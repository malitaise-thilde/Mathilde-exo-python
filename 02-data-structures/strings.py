# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:08:03 2026

@author: mathi
"""

mot = "Python"

print(mot[0])       # P
print(mot[-1])      # n
print(mot[0:3])     # Pyt   (slicing : du 0 au 3 exclu)
print(len(mot))     # 6

texte = "  Bonjour le Monde  "

print(texte.strip())         # "Bonjour le Monde"  (enlève les espaces)
print(texte.lower())         # "  bonjour le monde  "
print(texte.replace("o", "0"))

phrase = "Emma,Hugo,Chloé"
prenoms = phrase.split(",")
print(prenoms)              # ['Emma', 'Hugo', 'Chloé']

mot = "banane"
compteur = 0

for lettre in mot:
    if lettre == "a":
        compteur = compteur + 1

print(compteur)             # 3