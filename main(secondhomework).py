# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def triangle_editable(adat1,adat2,adat3):

  message = "A {},{} és {} oldalú háromszög szerkeszthető. "
  message_if_not = "A {},{} és {} oldalú háromszög NEM szerkeszthető."

  if adat1 + adat2 >= adat3 and adat1 + adat3 >= adat2 and adat2 + adat3 >= adat1:

      print(message.format(haromszagadat1,haromszagadat2,haromszagadat3))

  else :

      print(message_if_not.format(haromszagadat1,haromszagadat2,haromszagadat3))






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm

print("Adja meg a háromszög oldalát cm-ben: ")
haromszagadat1 = input("a oldal (cm): " )
haromszagadat2 = input("b oldal (cm): " )
haromszagadat3 = input("c oldal (cm): " )
triangle_editable(haromszagadat1,haromszagadat2,haromszagadat3)