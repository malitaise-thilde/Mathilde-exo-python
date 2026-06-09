# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:30:03 2026

@author: mathi
"""

"""client = {
    "prenom": "Lucas",
    "age": 25,
    "ville": "Lyon",
}

print(client["prenom"])     # Lucas
print(client["age"])        # 25

client = {"prenom": "Lucas"}
client["email"] = "lucas@example.com"   # ajout
client["prenom"] = "Lucas M."           # modification
print(client)

client = {"prenom": "Lucas", "age": 25, "ville": "Lyon"}

for cle, valeur in client.items():
    print(f"{cle} : {valeur}")

mots = ["chat", "chien", "chat", "oiseau", "chat"]
compteur = {}

for mot in mots:
    if mot in compteur:
        compteur[mot] = compteur[mot] + 1
    else:
        compteur[mot] = 1

print(compteur)     # {'chat': 3, 'chien': 1, 'oiseau': 1}"""

contact = {
    "prenom": "Lucas",
    "numero": "01.23.45.67.89",
}

print(contact["prenom"])
print(contact["numero"])

contact = {
    "prenom": "Maurice",
    "numero": "03.25.13.24.87",
}

print(contact["prenom"])
print(contact["numero"])

contact = {
    "prenom": "Lucie",
    "numero": "05.26.48.36.89",
}

print(contact["prenom"])
print(contact["numero"])