# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#Első házi feladat


#Első feladat

kertmondat = input("Adjon meg egy mondatot:")
print(kertmondat)
thisdict = dict()
for x in kertmondat:
    if x not in thisdict:
        thisdict[x] = 1
    else:
        thisdict[x] += 1
print(thisdict)

l = len(kertmondat) + 1
i = 1
a = "Fordítva: "

while i < l:

    a += (kertmondat[-i])
    i += 1

print(a)


print("Listába rendezve szavanként: ", kertmondat.split(" "))








#Második feladat

kertadat = int(input("Adjon meg egy számot és egy mértékegységet( cm/ inch ):"))
kertadat2 = input()
x = 2.54
nev1 = "inch"
nev2 = "cm"

if kertadat2 == "cm":
    print(kertadat * x, " inces")
elif kertadat2 == "inch":
    print(kertadat / x , " cm")
else:
    print("Not correct unit!")



