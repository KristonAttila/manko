from product import Product

class Grower:
    def read_file(self):
        fp = open('forras/products.txt', 'r',encoding="utf-8")
        lines = fp.readlines()
        fp.close()

        self.products = []

        for line in lines[1::]:
            (id, name, price, quantity) = line.split(';')
            product = Product(id, name, price, quantity)
            self.products.append(product)
    
    # legdrágább zöldség
    def larger(self):
        max_product=self.products[0]
        for product in self.products:
            if product.price > max_product.price:
                max_product=product
        print("Legdrágább:",max_product.name, max_product.price)

            
    
    # Az összes paprika ára
    def calcPepperPrice(self):
        max_ertek=self.products[0]
        for product in self.products:
            if product.name == "paprika":
                max_ertek=product
        print("Paprika",max_ertek.price*max_ertek.weight)

    # Mennyi a vöröshagyma és a karalábé tömege együtt?
    def sumOnionKohlrabiWeight(self):
        sum=0
        for product in self.products:
            if product.name == "vöröshagyma" or product.name == "karalábé":
                sum+=product.weight
        print("Tömegük:" ,sum)
                
    
    # Mi a neve legnagyobb tömegű zöldségnek?
    def showLargerWeight(self):
        max_product=self.products[0]
        for product in self.products:
            if product.weight > max_product.weight:
                max_product=product
        print("A legnagyobb tömegű zöldség: ",max_product.name)

    
    # Van karalábé?
    def isHaveKohlrabi(self):
        n=len(self.products)
        ker="karalábé"
        i=0
        while i<n and self.products[i].name !=ker:
            i+=1
        if i<n:
            print("Van",ker)
        else:
            print("Nincs",ker)

    # Hány zöldség drágább mint 700 Ft.
    def moreThenSevenhundred(self):
        darab=0
        for product in self.products:
            if product.price > 700:
                darab+=1
        print("Drágább mint 700Ft darabszámban:",darab)
        

grower=Grower()
grower.read_file()
grower.larger()
grower.calcPepperPrice()
grower.sumOnionKohlrabiWeight()
grower.showLargerWeight()
grower.isHaveKohlrabi()
grower.moreThenSevenhundred()