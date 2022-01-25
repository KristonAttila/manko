tipus=input("Adja meg a híd típusát: ")

fajtak=["gerenda","keret","konzolos"]
if tipus == "":
    exit()
elif tipus in fajtak:
    print("Hajlító vagy nyíró igénybevételek alapján tipizált")
else:
    print("Ismeretlen típus")