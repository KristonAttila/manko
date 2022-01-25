#File: betombv.py
#Auth: Kriston Attila
#Copyright: 2021, Kriston Attila
#Group: Ifra I/N
#Date: 2021-12-07
#Github: https://github.com/KristonAttila
#Licence: GNU GPL

print("Kriston Attila, Ifra I/N")
print("2021.12.07")
print("Feladat 1906")
print("A program  feltölt egy 20 elemű tömböt számokkal, majd visszaadja a tömböt.\n")

import random

def feltolt(tomb):
    for i in range (0,20):
        szam=random.randrange(1,20)
        tomb.append(szam)

szamtomb=[]
feltolt(szamtomb)
print("A tömb tartalma:",szamtomb)