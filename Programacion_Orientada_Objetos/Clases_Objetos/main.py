from persona import Persona #importando del modulo persona a la clase llamada Persona
from persona import Pc

persona1 = Persona()    #la variable persona1 se convierte en un objeto

persona1.nombre = 'Alex'
persona1.edad = '25'


persona1.mostrar_datos()

persona2 = Persona()    #la variable persona1 se convierte en un objeto

persona2.nombre = 'Santos'
persona2.edad = '25'


persona2.mostrar_datos()

pc = Pc()

pc.tipo = 'TORRE'
pc.costo = '300'


pc.mostrar_datos()