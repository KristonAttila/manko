from product import Product

class Grower:
    def read_file(self):
        fp = open('products.txt', 'r')
        lines = fp.readlines()
        fp.close()

        self.products = []

        for line in lines[1::]:
            (id, name, price, quantity) = line.split(';')
            product = Product(id, name, price, quantity)
            self.products.append(product)
    
    # legdrágább zöldség
    def larger(self):
        max_prod = self.products[0]
        for produc in self.products:
            if produc.price > max_prod.price:
                max_prod = produc
        print('Legdrágább:', max_prod.price)
    
    # Az összes paprika ára
    def calcPepperPrice(self):
        paprika = Product()
        for product in self.products:
            if product.name == 'paprika':
                paprika = product
        print('Paprika:', int(paprika.price) * int(paprika.weight))

    # Mennyi a vöröshagyma és a karalábé tömege együtt?
    def sumOnionKohlrabiWeight(self):
        onion = Product()
        kohlrabi = Product()
        for product in self.products:
            if product.name == 'vöröshagyma':
                onion = product
            if product.name == 'karalábé':
                kohlrabi = product
        print('Vöröshagyma és karalábé tömege együtt:',
            int(onion.weight) + int(kohlrabi.weight)
        )
    
    # Mi a neve legnagyobb tömegű zöldségnek?
    def showLargerWeight(self):
        max_prod = self.products[0]
        for produc in self.products:
            if produc.weight > max_prod.weight:
                max_prod = produc
        print('Legnagyobb tömegű neve:', max_prod.name)
    
    # Van karalábé?
    def isHaveKohlrabi(self):
        ker = 'karalábé'
        n = len(self.products)
        i = 0
        product = Product()
        product = self.products[0]
        while i<n and self.products[i].name != ker:
            i += 1        
        if i<n:
            print('Van')
        else:
            print('Nincs')

    # Hány zöldség drágább mint 700 Ft.
    def moreThenSevenhundred(self):
        count = 0
        for product in self.products:
            if product.price > 700:
                count += 1
        print('Drágább mint 700:', count)
        

grower = Grower()
grower.read_file()
grower.larger()
grower.calcPepperPrice()
grower.sumOnionKohlrabiWeight()
grower.showLargerWeight()
grower.isHaveKohlrabi()
grower.moreThenSevenhundred()