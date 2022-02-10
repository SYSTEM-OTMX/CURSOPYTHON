from cgi import print_directory
import sys #MODULO QUE INTERACTUA CON EL SISTEMA


if len(sys.argv) == 3:

    print(sys.argv)#RETORNAR LISTA
    texto = sys.argv[1]#GAURDANDO DATOS DE LA ENTRADA DEL SCRIPT
    cantidad = int(sys.argv[2])

    c = 0
    while c < cantidad:
        print(texto)
        c += 1 
else:
    print("INGRESA LOS ARGUMENTOS CORRECTAMENTE")
    print("Ejemplo: python name_file.py 'texto' 5")




#PARA EJECUTAR EN CONSOLA ES python entrada_script.py DATOS