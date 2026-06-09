# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:31:46 2026

@author: mathi
"""

"""notes = [12, 15, 8, 19, 14]

print(notes[0])      # 12  (premier élément, index 0)
print(notes[-1])     # 14  (dernier élément)
print(len(notes))    # 5   (nombre d'éléments)

notes = [12, 15, 8]
notes.append(19)        # ajoute à la fin
notes[0] = 13           # remplace le premier
print(notes)            # [13, 15, 8, 19]

notes = [12, 15, 8, 19, 14]

for note in notes:
    print(note)

notes = [12, 15, 8, 19, 14]
total = 0

for note in notes:
    total = total + note

moyenne = total / len(notes)
print(moyenne)          # 13.6"""

liste = [12, 15, 8, 19, 14]
nb_max = liste[0]

for nombre in liste:
    if nombre > nb_max:
        nb_max = nombre

print(nb_max)