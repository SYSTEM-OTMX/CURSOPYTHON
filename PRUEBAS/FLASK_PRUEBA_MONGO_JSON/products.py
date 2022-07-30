class Product:
    def __init__(self, name, lat,lng,address,phone):
        self.name = name
        self.lat = lat
        self.lng = lng
        self.address = address
        self.phone = phone

    def toDBCollection(self):
        return{
            'name':self.name,
            'lat':self.lat,
            'lng':self.lng,
            'address':self.address,
            'phone':self.phone
        }