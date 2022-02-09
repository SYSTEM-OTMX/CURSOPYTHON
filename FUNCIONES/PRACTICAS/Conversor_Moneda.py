
def tipo_moneda(tipo):

    if tipo == 1:
        nom_moneda = "MXN"
        valor_dolar = 20.58
        return nom_moneda,valor_dolar

    elif tipo == 2:
        nom_moneda = "BOB"
        valor_dolar = 4.48
        return nom_moneda,valor_dolar
    
    elif tipo == 3:
        nom_moneda = "COP"
        valor_dolar = 3941.63
        return nom_moneda,valor_dolar

def convertir(cant, valor_dolar):

    cantidad = cant / valor_dolar

    return cantidad

def main():
    op = True

    while op == True:
        print("*"*30)
        print(" "*30)
        print("LISTA DE MONEDAS PARA CONVERTIR")
        print("*"*30)
        print(" "*30)
        print(" 1-----MXN(PESOS MEXICANOS)")
        print(" 2-----BOB(VOLIVAR)")
        print(" 3-----COP(PESO COLOMBIANO)")
        print(" "*30)
        print("*"*30)
        print(" "*30)
        print("SELECCIONE MONEDA A CONVERTIR")
        tipo = int(input())
        print(" "*30)
        print("*"*30)
        print(" "*30)
        print("INGRESE CANTIDAD DE DINERO A CONVERTIR")
        cant = float(input())
        
        if tipo > 0 and tipo < 4:
            nom_moneda,valor_dolar = tipo_moneda(tipo)
            monedas = convertir(cant,valor_dolar)
            print("*"*30)
            print(" "*30)
            print(f"LA CANTIDAD DE {cant} {nom_moneda}: EQUIVALE A {monedas} DOLARES")
            print(" "*30)
            print("*"*30)
            print(" "*30)
            print("DESEA REALIZAR OTRA OPCION? S/N")
            opcion = str(input().upper())
            if opcion == "S":
                op = True
            elif opcion == "N":
                op = False

        else:
            print("INGRESE UNA OPCION VALIDA")
    print("SALIENDO DEL PROGRAMA")

if __name__ == "__main__":
    main()