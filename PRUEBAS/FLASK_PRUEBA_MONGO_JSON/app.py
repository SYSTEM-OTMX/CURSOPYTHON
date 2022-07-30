
import re
from flask import Flask, redirect, render_template, render_template, request,Response, jsonify, url_for
import database as dbase
from products import Product
import json
app = Flask(__name__)
archivojs = 'E:\PC\DOCUMENTOS\Repositorios-GIT\AMADEUS-PROYECT\FLASK\static\JS\data.json'
db = dbase.dbConection()


#rutas de la apliacion 
@app.route('/')
def home():
    
     products = db['locations']
     productsReceived = products.find()
     datajson = products.find()
     datos = []
     for dato in datajson:
          objeto = {}
          objeto['name'] = dato['name']
          objeto['lat'] = float(dato['lat'])
          objeto['lng'] = float(dato['lng'])
          objeto['address'] = dato['address']
          objeto['phone'] = dato['phone']
          datos.append(objeto)
          form_dir = json.dumps(datos, indent=4)
          data = open(archivojs,'w')
          data.write(form_dir)
          data.close()
          
          print(type(dato),dato)
     return render_template('index.html', products = productsReceived)
     
#Method Post
@app.route('/products',methods = ['POST'])
def appProduct():
     products = db['locations']
     name = request.form['name']
     lat = request.form['lat']
     lng = request.form['lng']
     address = request.form['address']
     phone = request.form['phone']
     

     if name and lat and lng and address and phone:

          product = Product(name,lat, lng, address, phone)
          products.insert_one(product.toDBCollection())
          response = jsonify({
               'name' : name,
               'lat': lat,
               'lng': lng,
               'address':address,
               'phone': phone
          })
          return redirect(url_for('home'))
     else:
          return notFound()

#Method Delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
     products = db['locations']
     products.delete_one({'name': product_name})
     datos = []
     form_dir = json.dumps(datos, indent=4)
     data = open(archivojs,'w')
     data.write(form_dir)
     data.close()
     return redirect(url_for('home'))

#Method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
     products = db['locations']
     name = request.form['name']
     lat = request.form['lat']
     lng = request.form['lng']
     address = request.form['address']
     phone = request.form['phone']
     datos = []
     

     if name and lat and lng and address and phone:
          products.update_one({'name': product_name},{'$set' : {'name' : name, 'lat': lat, 'lng' : lng,'address':address, 'phone':phone}})
          response = jsonify({'message': 'Producto ' + product_name + 'actualizado correctamente'})
          objeto = {}


          return redirect(url_for('home'))
     else:
          return notFound()


@app.errorhandler(404)
def notFound(error=None):
     message ={
          'message':'No encontrado ' + request.url,
          'status': '404 no found'
     }   
     response = jsonify(message)
     response.status_code = 404 
     return response
          
if __name__ == '__main__':
    app.run(debug=True, port=4000)