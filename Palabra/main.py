##definicion del metodo saberPalabra
def saberPalabra(palabra):
   longitud=len(palabra)
   letra1=palabra[0]
   letra2=palabra[-1]
   respuesta=letra1+letra2
   return respuesta

##desarrollo del programa
def main():
    print("Bienvenido al programa de la palabra")
    palabra=str(input("por favor la palabra que desee:  "))
    print("La primera letra es:"+palabra[0])
    print("La ultima letra es:"+palabra[-1])


if __name__ == '__main__':
    main()