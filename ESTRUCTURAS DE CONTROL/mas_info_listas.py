from calendar import day_abbr
from distutils.command.clean import clean
from turtle import clear


datos = ['EDAURDO',18,'MEXICO']

datos.append('SANTOS') #append agrega datos al final de laa lista

print('aappend',datos)

datos.extend(datos)# extiende la lista

print('extend',datos)

datos.insert(0,'PRIMER')# inseta datos en una posicion especifica

print('insert',datos)

datos = ['EDAURDO',18,'MEXICO']

datos.remove(18) #elimina un dato especifio de la lsita

print("remove",datos)

datos = ['EDAURDO',18,'MEXICO']

datos.pop()#elimina el ultimo dato de la lista o tambie se puede elgir que casilla eliminar

print("pop",datos)

datos.clear()#elimina todos los elementos de la lista

print("clear",datos)

datos = ['EDAURDO',18,'MEXICO']

a = datos.index(18)

print("index",a)#muestra el indice del elemento de la lista

datos = ['EDAURDO',18,18,'MEXICO']

a = datos.count(18)#muestra el nuemrod de veces que se repite un datos en la lista

print("count",a)

datos = ['c','b','h','a']

datos.sort()#ordena los datos de una lista, tener en cuanta que debe ser el mismo tipo de dato

print("sort",datos)

datos.reverse()#invertir listaa de datos

print("reverse",datos)