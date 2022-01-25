#File: vegetable.py
#Auth: Kriston Attila
#Copyright: 2021, Kriston Attila
#Group: Ifra I/N
#Github: https://github.com/KristonAttila
#Licence: GNU GPL

print("Kriston Attila, Ifra I/N")
print("2022.01.11")

from vegetableModel import VegetableModel
from typing import List

class Vegetable:
    def __init__(self):
        self.file_name = 'zoldseg.txt'
        self.vegetables: List[VegetableModel] = []
        self.lines = []
    
    def read_content(self):
        fp = open(self.file_name, 'r',encoding="utf-8")
        self.lines = fp.readlines()
        fp.close()
    
    def convert_content(self):
        for line in self.lines[1::]:
            (id, name, quantity, price, site) = line.split(';')
            vegetableModel = VegetableModel(
                id, name, int(quantity), int(price), site
            )
            self.vegetables.append(vegetableModel)
    
    def print_all(self):
        for vegetable in self.vegetables:
            print(
                vegetable.name,
                vegetable.site,
                vegetable.quantity
                )
    
    # A Szolnokon található zöldséget össz tömegét
    def szolnok_sum_wight(self):
        sum_weight=0
        for vegetable in self.vegetables:
            if vegetable.site.find("Szolnok") !=-1:
                sum_weight+=vegetable.quantity
        print("Szolnokon található zöldségek összes tömege:",sum_weight)

    # Melyik telephelyen van értékben legtöbb zöldség
    def most_valuable_vegetables(self):
        valuable=self.vegetables[0]
        for vegetable in self.vegetables:
            if vegetable.quantity*vegetable.price > valuable.quantity*valuable.price:
                valuable=vegetable
        print("A legtöbb értékben lévő zöldség telephelye:",valuable.site)

vegetable = Vegetable()
vegetable.read_content()
vegetable.convert_content()
vegetable.print_all()
vegetable.szolnok_sum_wight()
vegetable.most_valuable_vegetables()