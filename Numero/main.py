##definicion del metodo saberTipo
def saberTipo(numero):
    respueta = numero % 2
    return respueta

##desarrollo del programa
def main():
    print("Bienvenido al programa de los numeros")
    numero = float(input("por favor ingrese un numero :"))

    if numero % 2 == 0:
        print(bool(numero))
    else:
        if numero % 2 != 0:
            print(bool())

    saberTipo(numero)


if __name__ == '__main__':
    main()