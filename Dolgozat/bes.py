#File: bes.py
#Auth: Kriston Attila
#Copyright: 2021, Kriston Attila
#Group: Ifra I/N
#Date: 2021-12-07
#Github: https://github.com/KristonAttila
#Licence: GNU GPL

print("Kriston Attila, Ifra I/N")
print("2021.12.07")
print("Feladat 1055")
print("A program a bekér egy karaktersorozatot és kiírja a 'b' betűk számát.\n")

ksor=input("Adja meg a karaktersorozatot: ")

bkeres=["b"]
bszam=0

for kar in ksor:
    if kar in bkeres:
        bszam+=1

print("A 'b' betűk száma: %d db " % bszam)