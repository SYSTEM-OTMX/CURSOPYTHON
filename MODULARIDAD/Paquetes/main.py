import my_paquete.aritmetica as a

def main():
    suma = a.sumar(4,4,5,8,7,9)
    restar = a.restar(10,5)
    potencia = a.potencia(3,3)

    print("suma es:",suma)
    print("resta : ", restar)
    print("potencia : ", potencia)
if __name__ == '__main__':
    main()