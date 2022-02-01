#ENTRADA DE DATOS(CONSUMO)
from cgi import print_directory


print("INGRESE CANTIDAD DE CONSUMO")
consumo = float(input())

#PROCESO DE DESCUENTO
if consumo > 0:
    
    if consumo <= 100:
        #Descuento del 10 %
        dato_descuento = '10%'
        descuento = consumo * 0.10

    elif consumo > 100 and consumo <=200:
        #Descuento de 20%
        dato_descuento = '20%'
        descuento = consumo * 0.20


    elif consumo > 200:
        #Descuento de 30
        dato_descuento = '30%'
        descuento = consumo * 0.30



    #Monto del descuento
    monto_descuento = consumo - descuento

    #IGV impuesto

    igv = monto_descuento * 0.19

    #Total a pagar
    total_pagar = monto_descuento + igv

    #Imprecion de datos

    print("="*30)
    print('----------FACTURA DE DATOS--------------')
    print("Descuebto :",dato_descuento)
    print('='*30)
    print('Consumo:',consumo)
    print('Desciento:',descuento)
    print('Monto de descuento:',monto_descuento)
    print('IGV:',igv)
    print('Total a pagar:',total_pagar)
    print("="*30)


else:
    print("ERROR INGRESAR VALOR MAYOR A CERO")