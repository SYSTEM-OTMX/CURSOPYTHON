"""
nombre = 'Eduardo Santos'

"""

#Definicendo funcion {definir nombre}
def saludar():

    #Creando variable local
    nombre = 'Eduardo Santos'
    edad = 25
    #Retornando valor tambien return es el termino de una funcion
    return 'Hola desde la funcion saludar',nombre,edad
    
    
#Llamando a la funcion saludar
saludar()
#llamando funcion mostrando el valor del return
print(saludar())
#llamando datos de la funcion , guardandolos en una variable
valor = saludar()
#Llmando datos de la funcion, guardandolos en variables separadas para imprimirlas
saludo, nombre,edad = saludar()
print(valor)
print(saludo)
print(nombre)
print(edad)
