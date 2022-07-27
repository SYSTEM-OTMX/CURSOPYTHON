from ast import Return
from pymongo import MongoClient
import certifi
MONGO_URL = 'mongodb+srv://SYSTEM-OTMX:Cop07234MON@cluster0.qustf.mongodb.net/?retryWrites=true&w=majority'

ca = certifi.where()

def dbConection():
    try:
        client = MongoClient.connect(MONGO_URL, tlsCAFile=ca)
        db = client["dbb_products_app"]
    
    except ConnectionError:
        print('ERRO DE CONEXION CON LA BD')
    
    return db
