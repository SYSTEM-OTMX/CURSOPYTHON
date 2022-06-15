from persona import Persona #importando del modulo persona a la clase llamada Persona


persona1 = Persona('Eduardo',21)    #la variable persona1 se convierte en un objeto

persona1.mostrar_datos() #ejecuta el metodo de mostrar datos

persona1.nombre = 'Santos' #establece valor nuevo al objeto

persona1.mostrar_datos() #vuelve a ejecutra el metodo para ver el ccambio de valor
 
print(persona1)  #ver el estado del objeto