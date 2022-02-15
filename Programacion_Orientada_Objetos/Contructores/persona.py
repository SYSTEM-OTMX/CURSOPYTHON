class Persona:#se pone class y nombre_clase primera letra en mayusucula
   

    def __init__(self,nombre,edad): #creando constructor con __init__, recibiendo los atributos
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):    #cuando def esta dentro de una clase se convierte a llamar meotodo "self significa que el metodo pertenese a la clase"
        print('Nombre :',self.nombre)
        print('Edad :',self.edad)

    def __str__(self):  #mostrar estado delobjeto, 
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'


