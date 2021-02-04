from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from src.routes.routes import initialize_routes

app = Flask(__name__)

CORS(app)
api = Api(app)


initialize_routes(api)
