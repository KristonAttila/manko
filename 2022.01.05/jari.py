from help import Cars

class BT:
    def read_file(self):
        fp = open('2022.01.05/jaribt.txt', 'r',encoding="utf-8")
        lines = fp.readlines()
        fp.close()

        self.infok = []

        for line in lines[0::]:
            (rendszam ,name, evjarat, uzemanyag,eladasi_ar, klima,erv_forgalmi) = line.split(':')
            info = Cars(rendszam ,name, evjarat, uzemanyag,eladasi_ar, klima,erv_forgalmi)
            self.infok.append(info)

    def osszesBenzinek(self):
        for info in self.infok:
            if info.uzemanyag == "benzin":
                print("Az összes benzines autó adata:",info.rendszam ,info.name, info.evjarat, info.uzemanyag,info.eladasi_ar, info.klima,info.erv_forgalmi)

    def olcsobb(self):
        for info in self.infok:
            if  int(info.eladasi_ar) < 1000000:
                print("Az 1 milliónál olcsóbb autó adata:",info.rendszam ,info.name, info.evjarat, info.uzemanyag,info.eladasi_ar, info.klima,info.erv_forgalmi)

    def hondak(self):
        for info in self.infok:
           if info.name == "Honda":
               print("A hondák adatai:",info.rendszam , info.evjarat, info.uzemanyag,info.eladasi_ar, info.klima,info.erv_forgalmi)


bt=BT()
bt.read_file()
bt.osszesBenzinek()
print("\n","\n","\n")
bt.olcsobb()
print("\n","\n","\n")
bt.hondak()
print("\n","\n","\n")