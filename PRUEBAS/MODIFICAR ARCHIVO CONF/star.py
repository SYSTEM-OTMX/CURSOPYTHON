import json




hola = []
establecimiento = {}
nombre = "eduardo"

establecimiento['name'] = nombre
latitud = 19.507943
establecimiento['lat'] = latitud
longitud = -99.049428
establecimiento['lng'] = longitud
direccion = "MEXICO DF"
establecimiento['address'] = direccion
telefono = "6647826273"
establecimiento['phone'] = telefono


hola.append(establecimiento)
form_dir = json.dumps(hola, indent=4)
    
data = open('data.json','w')
data.write(form_dir)
data.close()


