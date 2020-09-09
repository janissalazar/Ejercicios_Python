

def saberAño(d):
    return d

def main():

   print("Bienvenido al año 2019")
   c=0
   a = float(input("por favor la poblacion inicial de A:  "))
   b=float(input("por favor la poblacion inicial de B:  "))
   while a>b:
    a=a+(a*0.02)
    b=b+(b*0.03)
    c+=1
    d=2019+c
   print("La poblacion del pais B supera a la del pais A en el año "+str(d))

   saberAño(d)
if __name__ == '__main__':
    main()
