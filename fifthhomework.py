def szorzotabla():
        tabla = "{0:>5}{1:>1}{2:>6}{3:>6}{4:>6}{5:>6}{6:>6}{7:>6}{8:>6}{9:>6}{10:>6}{11:>6}{12:>6}{13:>6}"

        print(tabla.format("", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
        print("     :------------------------------------------------------------------------")

        szorzatok=[]
        for i in range(0, 12):
            for j in range(1, 13):
                szorzatok.append(j*(i+1))

            print(tabla.format(str(i+1), ":", szorzatok[0], szorzatok[1], szorzatok[2], szorzatok[3], szorzatok[4], szorzatok[5],
                               szorzatok[6], szorzatok[7], szorzatok[8], szorzatok[9], szorzatok[10], szorzatok[11]))
            szorzatok = []




if __name__ == "__main__":

    szorzotabla()