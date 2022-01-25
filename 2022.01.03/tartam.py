def elettartamVizsgalat(elettartam):
        if elettartam >= 50:
            return "Állandó"
        else:
            return "Rövid"

elettartam=-1

while elettartam !=0:
    elettartam=int(input("Adja meg a híd élettartamát: "))
    if elettartam !=0:
        print(elettartamVizsgalat(elettartam))
 