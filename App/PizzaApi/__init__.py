from flask import  *
from flask_restplus import Api
from flask_cors import CORS
app = Flask(__name__)


api=Api(app)
CORS(app)
from App.PizzaApi import pizzadetails
from  App.PizzaApi import getpizzadetails
from App.PizzaApi import getallpizza
from App.PizzaApi import Deletepizza