class Persona:#se pone class y nombre_clase primera letra en mayusucula
    nombre = None   #atributo
    edad = None #atributo

    


    def mostrar_datos(self):    #cuando def esta dentro de una clase se convierte a llamar meotodo "self significa que el metodo pertenese a la clase"
        print('Nombre :',self.nombre)
        print('Edad :',self.edad)

        
class Pc:
    tipo = None
    costo = None 

    def mostrar_datos(self):
        print('TIPO',self.tipo)
        print('COSTP',self.costo)