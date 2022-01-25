class Star:
    def __init__(self):
        self.file_name = 'proker.txt'
        self.lines = []
        self.stars: List[StarModel] = []
    
    def read_content(self):
        fp = open(self.file_name, 'r')
        self.lines = fp.readlines()
        
    
    def convert_content(self):
        for line in self.lines[]:
            (name, constellation, 
            distance, mass, temperature, age) = line.split(':')
            
            starModel = StarModel(
                name, constellation, 
                int(distance), 
                float(mass.replace(',', '.')), 
                int(temperature), 
                float(age.replace(',', '.')))

            self.stars.append(starModel)
    
    def print_out(self):
        for star in self.stars:
            print(star.name)
    
    # Van-e csillag a Göncöl csillagképben
    def star_in_goncol(self):
        pass

    # Legtávolabbi csillag neve, távolsága
    def farthest_star(self):
        pass

    # Legalacsonyabb hőmérsékletű csillag
    def lowest_temperature_star(self):
        pass

    # A Csillagok átlagéletkor
    def average_age_of_stars(self):
        pass

    # a Kepler-18 hány kiloggram tömegű
    def weight_of_kepler18(self):
        pass
            
    # 150 fényévnél közelbbi bolygók neve és távolsága
    def close_stars(self):
        pass

    # A Szextánok csillagképben található csillagok adatai
    def szextan_datas(self):
        pass

    # A 2 M-nél kisebb tömegű csillagok neve és tömege
    def less_than_two_mass_stars(self):
        pass

