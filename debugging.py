def divisor(num):
    lista = [i for i in range(1, num + 1) if num % i == 0]

    return lista


def run():
    try:
        num = int(input('Ingrese un numero: '))
        if num < 0:
            raise ValueError
        print(divisor(num))
        print("Termino el programa")

    except ValueError:
        print("Debes ingresar un numero"," ", "Debes ingresar un numero positivo")

    
        

if __name__ == '__main__':
    run()