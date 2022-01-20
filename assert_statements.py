def divisor(num):
    lista = [i for i in range(1, num + 1) if num % i == 0]

    return lista


def run():
 
        num = input('Ingrese un numero: ')
        assert num.isnumeric() and int(num) > 0, "Debes ingresar un numero positivo"  
        print(divisor(int(num)))
        print("Termino el programa")
    
        

if __name__ == '__main__':
    run()