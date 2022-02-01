"""
nombre = 'Eduardo Santos'

"""

#Definicendo funcion {definir nombre} (parametro)
def saludar(nombre):

    #Creando variable local
    
    
    #Retornando valor tambien return es el termino de una funcion
    return f'Hola,{nombre} desde la funcion saludar'

def sumar(a ,b):
    return a + b
    #Definiendo funcion con parametros vacions o por defecto

def restar(a=None,b=None):
    if a == None or b == None:
        print("PARAMETROS VACIOS")
        return
    else:
        return a - b    

#llamando datos de la funcion , guardandolos en una variable con un argumento name_funcion(argumento)
saludo = saludar('Eduardo')
print(saludo)

#llamadno  funcion sumar por argumennto por posicion
suma = sumar(2,2)
print('la suma es:',suma)

#llamando fucnion restar por argumento por nombre
resta = restar(b = 5 , a=15)
print('La resta es:',resta)



