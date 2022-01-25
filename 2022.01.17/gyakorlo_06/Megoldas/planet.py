# File: planet.py
# Author: Kriston Attila
# Copyright: 2021, Kriston Attila
# Group: Infra I/N
# Date: 2022-01-17
# Github: https://github.com/kristonattila
# Licenc: GNU GPL


def chek_planet(bolygo):
    torpek=["Ceres", "Pluto", "Haumea", "Makemake", "Eris"]
    bolygok=["Merkúr", "Vénusz", "Mars", "Jupiter", "Szaturnusz", "Uránusz","Neptunusz"]
    if bolygo in torpek:
        return "törpebolygó"
    elif bolygo in bolygok:
        return "bolygó"
    else:
        return "Ismeretlen"

bolygo=""

while bolygo !="vege":
    bolygo = input("Bolygó neve: ")

    if bolygo!="vege":
        uzenet = chek_planet(bolygo)
        print(uzenet)

