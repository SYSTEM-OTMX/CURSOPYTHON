#POLIMORFISMO PODER MODIFICAR O REESCRIBIR METODOS DE LA CLASE PADRE

#OBJECT CREA UNA CLASE NORMAL
class Persona(object):
    def __init__(self, nombre) :
        self.nombre = nombre

    def moverse(self):
        print('ANDO CAMINANDO')

class Atleta(Persona):
    #se reescribe el metodo moverse para atleta
    def moverse(self):
        print('ANDO CORRIENDO')

class Ciclista(Persona):
    #se reescribe el metodo moverse para ciclista
    def moverse(self):
        print('ANDO PEDALEANDO')

