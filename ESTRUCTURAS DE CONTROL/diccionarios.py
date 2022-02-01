

Diccionario = {"EDUARDO":"21","YEAR":2000}

print(Diccionario["EDUARDO"])

print(Diccionario["YEAR"])

Diccionario['GENERRO'] = "HOMBRE"#AGREGAR DATOS A DICCIONARIO

print(Diccionario)

#metodos

a = Diccionario.get('EDUARD','no exsite')#buscar por clave, y no pos valor, 

print(a)

a = Diccionario.keys()#muestra todas las claves del diccionario

print(a)

a = Diccionario.values()#muestra todos los valores del diccionario

print(a)

a = Diccionario.items()#Regresa todos los datos en lista

print(a)

Diccionario.pop('YEAR','NNO SE ENCONTRO')#eliminarr elemento espcifico

print(a)
"""
Diccionario.clear()#elimnar todo

print(a)

"""

for numero in Diccionario:#iterar datos
    print(numero)

for numero in Diccionario.values():#iterar valores
    print(numero)


for numero,valor in Diccionario.items():#iterar llave y vaalor
    print(numero,valor)
