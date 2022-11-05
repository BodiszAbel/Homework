def palindrom(kertmondat):
    a = "".join(reversed(kertmondat))

    b = kertmondat



    listrossz = ["yn","yl","yg","yt","szd","zd"]
    listjo = ["ny","ly","gy","ty","dzs","dz"]

    for i in listrossz:
        if i in a:
           ujmondat = a.replace(i, listjo[listrossz.index(i)])

    if a == kertmondat:
        print("A megadott szó egy palindróm")
    if ujmondat == kertmondat:
        print("A megadott szó egy palindróm")
    else:
        print("A megadott szó nem egy palindróm")

if __name__ == "__main__":

    bekeres = input("Kérem adjon megy egy szót/mondatot: ")
    palindrom(bekeres)

