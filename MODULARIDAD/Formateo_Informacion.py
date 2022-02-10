
from sys import argv #MODULO QUE INTERACTUA CON EL SISTEMA


if len(argv) == 4:

    print(argv)#RETORNAR LISTA

    nombre = argv[1]#GAURDANDO DATOS DE LA ENTRADA DEL SCRIPT
    edad = int(argv[2])
    altura = float(argv[3])

    c = 0
    print(f'Nombre: {nombre} \nEdad: {edad} \nAltura: {altura}')
    print('Nombre: {} \nEdad: {} \nAltura: {}'.format(nombre,edad,altura))
    print('Nombre: {n} \nEdad: {e} \nAltura: {a}'.format(a = altura,e = edad,n = nombre))
    print('Nombre: %s \nEdad: %i \nAltura: %f'%(nombre, edad, altura))
        
else:
    print("INGRESA LOS ARGUMENTOS CORRECTAMENTE")
    print("Ejemplo: python name_file.py 'Nombre' edad altura")




#PARA EJECUTAR EN CONSOLA ES python entrada_script.py DATOS