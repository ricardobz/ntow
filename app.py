from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


class Nums(Resource):
    def get(self, param):
            return param, 200

      
api.add_resource(Nums, "/<string:param>")

app.run(debug=True)
