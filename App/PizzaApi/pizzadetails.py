from flask import request
from bson.json_util import dumps
from flask_restplus import Resource
from  App.Database.Databaseoperation import Test
from App.PizzaApi import api

@api.route("/pizzadetails")
class Pizza(Resource):
    def post(self):
        data=request.json
        pizzadetails=Test()
        insertpizzadetails=pizzadetails.inserPizzatdata(data)
        if insertpizzadetails:
            return dumps(insertpizzadetails)


