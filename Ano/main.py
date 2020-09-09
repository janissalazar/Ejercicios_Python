import datetime
## importacion de la libreria datatime
anio = datetime.datetime.now()

##definicion del metodo saberEdad
def saberEdad(edad, anio):
    respueta = edad + (2070 - anio)
    return respueta

##desarrollo del cuerpo
def main():
    print("Bienvenido al programa de la Edad")
    print("El año actual es:")
    print(anio.year)
    edad = -1
    while edad < 0 or edad > 140:
        edad = int(input("por favor ingrese su edad:  "))

        print("Su edad en el año 2070 sera:")
        print((2070 - anio.year) + edad)


if __name__ == '__main__':
    main()