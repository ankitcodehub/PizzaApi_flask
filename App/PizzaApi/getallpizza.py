from flask import request
from bson.json_util import dumps
from flask_restplus import Resource
from  App.Database.Databaseoperation import Test
from App.PizzaApi import api

@api.route("/getallpizzadetails")
class Pizza(Resource):
    def get(self):
        pizzadetails=Test()
        getpizzadetails=pizzadetails.getallpizzadetails()
        if getpizzadetails:
            return dumps(getpizzadetails)


