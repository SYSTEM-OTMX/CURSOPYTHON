#definidno datos sin cantidad de datos establecidos(*=arguimentos indeterminados por posicion args=todos los parametros por posicion,**kwargas = 
# arumentos por nombre) args es una tupla y kwargs es un diccionario

def sumar(*args,**kwargs):
    suma = 0


    for n in args:
        suma += n

    return suma,kwargs
        

suma,datos = sumar(1,2,3,4,5,6, nombre='SANTOS',edad=25)

print(suma)
print(datos)




