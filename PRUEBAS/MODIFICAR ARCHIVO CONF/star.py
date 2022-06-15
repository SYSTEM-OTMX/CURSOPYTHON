import json


conf_file = "PRUEBAS\MODIFICAR ARCHIVO CONF\conf.conf"



data = open(conf_file,'r')

config = data.read()

data.close()

DCONFIG = json.loads(config)
print(type(DCONFIG),DCONFIG['directorio'][0])
pedat = dict(DCONFIG["directorio"][0])
print(type(pedat),pedat['idCel'][0])
gnss = dict(DCONFIG["dirGNSS"][0])
print(type(gnss),gnss["alias"])
#print(type(DCONFIG),DCONFIG)

pedat["id"] = "001"

print(pedat)


DCONFIG["directorio"] = pedat

form_dir = json.dumps(DCONFIG, indent=4)
    
data = open('PRUEBAS\MODIFICAR ARCHIVO CONF\conf.conf','w')
data.write(form_dir)
data.close()

