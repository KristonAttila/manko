from country import Country
from typing import List

class Mikronezia:
    def __init__(self):
        self.countries: List[Country] = []
        self.sep = ';'
    def read_content(self):
        file_name = '2022.01.10/gyakorlo_05/forras/countries.txt'
        fp = open(file_name, 'r',encoding="utf-8")
        self.lines = fp.readlines()
        fp.close()

    def convert_content(self):
        for line in self.lines[1::]:            
            (id, name, area, population) = line.split('#')
            country = Country(id, name, int(area), int(population))
            self.countries.append(country)

    # Legnépesebb ország
    def most_populated(self):
        max_country = self.countries[0]
        for country in self.countries:
            if country.population > max_country.population:
                max_country=country
        print("Legnépesebb ország",max_country.name,max_country.population)

    # Legkisebb területű ország
    def smallest_area(self):
        min_country = self.countries[0]
        for country in self.countries:
            if country.area < min_country.area:
                min_country=country
        print("Legkisebb területű ország",min_country.id,min_country.name,min_country.area,min_country.population)

    # 99 ezernél kisebb népesség
    def less_than_ninety_nine_thousand(self):
        min_country = self.countries[0]
        for country in self.countries:
            if country.population < 99000:
                print(country.name,country.population)

    # Hány 500 négyeztkilométernél nagyobb területi ország van?
    def more_than_five_hunderd_area(self):
        darab=0
        for country in self.countries:
            if country.area > 500:
                darab+=1
        print("500 négyeztkilométernél nagyobb területi ország darabszáma:",darab)

    # Hány ország nevében szerepel a "sziget" szó?
    def island_word_in_name(self):
        darab=0
        for country in self.countries:
            if country.name.find ("sziget") !=-1:
                darab+=1
        print("Szigetek darabszáma:", darab)

    # Az országok területe összesen
    def sum_areas(self):
        osszeg=0
        for country in self.countries:
            osszeg+=country.area
        print("Az országok területe összesen:",osszeg)

    # Az országok népességének átlaga
    def population_average(self):
        osszeg=0
        darab=0
        for country in self.countries:
            darab+=1
            osszeg+=country.population
        atlag= osszeg/darab
        print("A népesség átlaga: %.2f" % atlag)
            

    # Állapítsuk meg, hogy egyszavas, vagy nem, a név
    def is_one_word(self, country: Country):
        res=country.name.find("-")
        if res == -1:
            return True
        else:
            return False

    def write_a_country(self, fp, country):
        fp.write(country.id)
        fp.write(self.sep)
        fp.write(country.name)
        fp.write(self.sep)
        fp.write(str(country.area))
        fp.write(self.sep)
        fp.write(str(country.population))
        fp.write('\n')


    def write_one_word(self):
        fp = open('oneword.txt', 'a')
        for country in self.countries:
            if self.is_one_word(country):
                self.write_a_country(fp, country)
        fp.close()


mikro = Mikronezia()
mikro.read_content()
mikro.convert_content()
mikro.most_populated()
mikro.smallest_area()
mikro.less_than_ninety_nine_thousand()
mikro.more_than_five_hunderd_area()
mikro.island_word_in_name()
mikro.write_one_word()
mikro.sum_areas()
mikro.population_average()
res=mikro.is_one_word(mikro.countries[0])
print(res)
