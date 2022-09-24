# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def sentence(kertmondat):

    thisdict = dict()
    for x in kertmondat:
        if x not in thisdict:
            thisdict[x] = 1
        else:
            thisdict[x] += 1
    print("Betűk gyakorisága: ",thisdict)

def sentence_backwards_and_pieces(kertmondat):
    l = len(kertmondat) + 1
    i = 1

    a = ("Fordítva: ")
    while i < l:

        a += kertmondat[-i]
        i += 1
    print(a)

def sentence_listpiece(kertmondat):
    print("Listába rendezve szavanként: ", kertmondat.split(" "))

def cmvalto(kertmondat,kertmondat2):

    x = 2.54
    nev1 = "inch"
    nev2 = "cm"

    if kertadat2 == "cm":
        print(kertadat * x, " inces")
    elif kertadat2 == "inch":
        print(kertadat / x, " cm")
    else:
        print("Not correct unit!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

#Első feladat

    wordpieces = input("Adjon meg egy mondatot: ")
    sentence(wordpieces)
    sentence_backwards_and_pieces(wordpieces)
    sentence_listpiece(wordpieces)

#Második feladat

    kertadat = int(input("Adjon meg egy számot és egy mértékegységet( cm/ inch ):"))
    kertadat2 = input()
    cmvalto(kertadat,kertadat2)



















