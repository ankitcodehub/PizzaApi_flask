from flask import request
from bson.json_util import dumps
from flask_restplus import Resource
from  App.Database.Databaseoperation import Test
from App.PizzaApi import api

@api.route("/getpizzadetails")
class Pizza(Resource):
    def post(self):
        data=request.json
        pizzadetails=Test()
        getpizzadetails=pizzadetails.getpizzadata(data)
        if getpizzadetails:
            return dumps(getpizzadetails)


