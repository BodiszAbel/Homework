import string

imvaltozo = string.punctuation + "aáeéiíoóöőuúüű"


with open("hazi.txt", "r", encoding="UTF-8") as f, open("hazi_rombolt.txt", "w", encoding="UTF-8") as r:

    tartalom = f.readlines()
    f_tartalom = tartalom[0::3]


    for line in f_tartalom:
        if line.strip():
            line = line.replace(" ", "")
            newline = ""
            for char in line:
                if (char not in imvaltozo) and (char not in imvaltozo.upper()):
                    newline += char
            r.write(newline)
