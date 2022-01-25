# File: bolygo.py
# Author: Kriston Attila
# Copyright: 2021, Kriston Attila
# Group: Infra I/N
# Date: 2022-01-17
# Github: https://github.com/kristonattila
# Licenc: GNU GPL

bolygo_nev=input("Adja meg a bolygó nevét: ")

if bolygo_nev=="":
    exit()

lista=["Ceres","Haumea", "Eris", "Makemake"]

if bolygo_nev in lista:
    print("törpebolygó")
else:
    print("Nem besorolt")