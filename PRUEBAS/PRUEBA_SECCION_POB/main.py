
from figuras import Circulo, Rectangulo
ciclo = 1
while(ciclo == 1):
    base = 0
    altura = 0
    op = 0
    print("*"*30)
    print("MENU DE OPERACIONES")
    print("1    RECTANGULO")
    print("2    CIRCULO")
    print("3    SALIR")
    print("*"*30)
    op=int(input("INGRESA UNA OPCION :"))
    if op == 3:
        print("SAIENDO DEL SISTEMA")
        break

   
    if op == 1: 
        base = float(input("INGRESA LA BASE :"))
        altura = float(input("INGRESA LA ALTURA :"))
        rectangulo = Rectangulo(base,altura)
        rectangulo.area()
        rectangulo.perimetro()
        
        ciclo = 1

    if op == 2:
        radio = float(input("INGRESA RADIO :"))
        
        Circulo.area(base,altura)
        Circulo.perimetro(base,altura)
        ciclo = 1

    
