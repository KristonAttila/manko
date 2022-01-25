#File: palya.py
#Auth: Kriston Attila
#Copyright: 2021, Kriston Attila
#Group: Ifra I/N
#Github: https://github.com/KristonAttila
#Licence: GNU GPL

print("Kriston Attila, Ifra I/N")
print("2021.12.15")
print("Feladat 2")
print("A program megkérdezi, hogy melyik területhez tartozik a megadott vasúti pálya és figyelmezteti a felhasználót a pálya állapotáról.\n")

palya=input("Adja meg melyik területhez tartozika vasúti pálya: ")

teruletek=["Budapest","Miskolc","Pécs","Zalaegerszeg"]

if palya in teruletek:
    orid=int(input("Adja meg a területhez tartozó pályák öregedési idejét években: "))
    if 2<orid and orid<6:
        print("felülvizsgálatot igényel")
    elif 5<orid:
        print("Sürgős karbantartás")
    else:
        print("Normál")
else:
    quit()