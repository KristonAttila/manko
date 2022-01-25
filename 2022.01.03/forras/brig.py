from bridgeModel import BridgeModel #1. feladat

class Brig:
    def read_file(self):
        fp = open('forras/hidak.txt', 'r', encoding="utf-8") #3.feladat
        lines = fp.readlines()
        fp.close()

        self.bridges = []

        for line in lines[1::]:
            (id, name, place, length, year) = line.split(':')
            bridge = BridgeModel(id, name, place, int(length), int(year))
            self.bridges.append(bridge)

    # Leghosszabb híd
    def longest(self):   #9. feladat
        n= len(self.bridges)
        max_bridge=self.bridges[0]
        for bridge in self.bridges[1::]:
            if bridge.length > max_bridge.length:
                max_bridge= bridge
        print(
            max_bridge.name,
            max_bridge.length,
            "méter")

    # A Megyeri híd szerepel a listában?
    def isHaveMegyeri(self):    #10. feladat
        n=len(self.bridges)
        ker="Megyeri"
        i=0
        while i<n and self.bridges[i].name.find(ker) == ker:
            i+=1
        if i<n:
            print("Van ilyen")
        else:
            print("Nincs ilyen")

    
    # A nem budapesti hidak nobp.txt fájlba
    def select_nobp(self):  
        for bridge in self.bridges:
            if bridge.place != 'Budapest': #11. feladat
                self.write_bridge(bridge)
        print("Kiírva") #12. feladat
        

    # Híd kiírása
    def write_bridge(self, bridge):
        fp = open('nobp.txt', 'a', encoding="utf-8") #13. feladat, 14. feladat
        fp.write(bridge.id)
        fp.write(';')
        fp.write(bridge.name)
        fp.write(';')
        fp.write(bridge.place)
        fp.write(';')
        fp.write(str(bridge.length)) #15. feladat
        fp.write('\n')
        fp.close()

brig= Brig()            #4. feladat
brig.read_file()        #5. feladat  Először van a fájl beolvasása
brig.longest()          #6. feladat  Ez csak utánna
brig.isHaveMegyeri()    #7. feladat
brig.select_nobp()      #8. feladat