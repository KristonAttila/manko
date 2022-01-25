# File: star.py
# Author: Kriston Attila
# Copyright: 2021, Kriston Attila
# Group: Infra I/N
# Date: 2022-01-17
# Github: https://github.com/kristonattila
# Licenc: GNU GPL

from starModel import StarModel
from typing import List

class Star:
    def __init__(self):
        self.file_name = 'Megoldas/stars.txt'
        self.lines = []
        self.stars: List[StarModel] = []
    
    def read_content(self):
        fp = open(self.file_name, 'r',encoding="utf-8")
        self.lines = fp.readlines()
        fp.close() #6. feladat
        
    
    def convert_content(self):
        for line in self.lines[1:]:
            (name, constellation, distance, mass, temperature, age) = line.split(':')
            
            starModel = StarModel(
                name, constellation, 
                float(distance.replace(",",".")), 
                float(mass.replace(',', '.')), 
                int(temperature), 
                float(age.replace(',', '.')))

            self.stars.append(starModel)
    
    def print_out(self):
        for star in self.stars:
            print(star.name,star.constellation,"\n")

    
    # Van-e csillag a Göncöl csillagképben
    def star_in_goncol(self):
        i=0
        n=len(self.stars)
        while i<n and self.stars[i].constellation.find("Göncöl") ==-1:
            i+=1
        if i<n:
            print("van")
        else:
            print("nincs")

    # Legtávolabbi csillag neve, távolsága
    def farthest_star(self):
        max_star=self.stars[0]
        for star in self.stars:
            if star.distance > max_star.distance:
                max_star=star
        print("Legtávolabbi:",max_star.name,max_star.distance, "ly")

    # Legalacsonyabb hőmérsékletű csillag
    def lowest_temperature_star(self):
        min_stars=self.stars[0]
        for star in self.stars:
            if star.temperature < min_stars.temperature:
                min_stars = star
        print("Legalacsonyabb hőmérséklet:",min_stars.temperature, "K")

    # A Csillagok átlagéletkor
    def average_age_of_stars(self):
        osszeg=0
        darab= len(self.stars)
        for star in self.stars:
            osszeg+=star.age
        atlag=osszeg/darab
        print("Átlag: %.2f Ga" % atlag)

    # a Kepler-18 hány kiloggram tömegű
    def weight_of_kepler18(self):
        for star in self.stars:
            if star.name == "Kepler-18":
                print("A csillag tömege:",star.mass)
            
    # 150 fényévnél közelbbi bolygók neve és távolsága
    def close_stars(self):
        pass

    # A Szextánok csillagképben található csillagok adatai
    def szextan_datas(self):
        pass

    # A 2 M-nél kisebb tömegű csillagok neve és tömege
    def less_than_two_mass_stars(self):
        pass

star= Star()
star.read_content()
star.convert_content()
star.print_out()
star.star_in_goncol()
star.farthest_star()
star.lowest_temperature_star()
star.average_age_of_stars()
star.weight_of_kepler18()
star.close_stars()
star.szextan_datas()
star.less_than_two_mass_stars()