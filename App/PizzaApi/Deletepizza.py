from flask import request,jsonify
from bson.json_util import dumps
from flask_restplus import Resource
from  App.Database.Databaseoperation import Test
from App.PizzaApi import api

@api.route("/deletepizzadetails")
class Pizza(Resource):
    def delete(self):
        pizzadetails=Test()
        data=request.json
        deletepizzadetails=pizzadetails.deletepizzadetails(data)
        if deletepizzadetails:
            return jsonify({"msg":"your details has been suceesfully deleted"})


