def read ():
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        lista = [int(lines) for lines in f ]

    print (lista)


def write ():
    names = ["Juan", "Pedro", "Maria", "Carlos"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")




def run():
    write ()

if __name__ == '__main__':
    run()