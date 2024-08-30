from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse

# initalize the flask class and the API library

app = Flask(__name__)
api = Api(app)

rms = {
    "restaurant": {"name": "Lauki","phone":"85856545","address":"149, Lauki Lane, Marval"},
    "menu":{
        "wings": {"price": 9.99,"quantity_remaining":19}
    }
}
#  Main resturant class shows details about the restaurant
class Restaurant(Resource):
    def get(self):
        return rms['restaurant']

#  main class shows main menu and allo to add items
class Main(Resource):

    def get(self):
        return rms['menu']


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('item')
        parser.add_argument('price')
        parser.add_argument('quantity_remaining')
        result = parser.parse_args()

        if result['item'] == None or result['price'] == None or result['quantity_remaining'] == None:
            return {'error':'missing filds'}

        rms['menu'][result['item']] = {'price': result['price'], 'quantity_remaining':result['quantity_remaining']}
        return {'message':f"{result['item']} added to the menu!"}




#  menu class is about menu and updating, deleting items
class Menu(Resource):
    def get(self, item):
        try:
            return rms['menu'][item]
        except KeyError:
            return {"message":f"{item} doesn't exist"}


    def put(self, item):
        try:
            rms['menu'][item]
        except KeyError:
            return {"error":"{} does not item exists!".format(item)}
        parser = reqparse.RequestParser()
        parser.add_argument('price')
        parser.add_argument('quantity_remaining')
        result = parser.parse_args()
        if result['price'] == None and result['quantity_remaining'] == None:
            return {'error':"values missing"}
        else:
            if result['price'] != None:
                rms['menu'][item]['price'] = result['price']
            if result['quantity_remaining'] != None:
                rms['menu'][item]['quantity_remaining'] = result['quantity_remaining']
            return {'message': "data updated!"}

    def delete(self, item):
        try:
            rms['menu'][item]
        except KeyError:
            return {'error':'{} does not exists'.format(item)}
        
        del rms['menu'][item]
        return {'message':"{} deleted".format(item)}
        
    

# mapping to endpoints
api.add_resource(Restaurant, "/restaurant")
api.add_resource(Menu, "/menu/<item>")
api.add_resource(Main, "/menu")


if __name__ == "__main__":
    app.run(debug=True)