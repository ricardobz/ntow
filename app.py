from flask import Flask
from flask_restful import Api, Resource, reqparse
from controller import num_words as nw

app = Flask(__name__)
api = Api(app)


class Nums(Resource):
    def get(self, param):
        
        if param.isdigit():
            return {"extenso" : nw(int(param))}, 200

        elif param[0] == "-" and param[1:].isdigit():            
            return {"extenso" : nw(int(param))}, 200
            
        else:
            return "Informe um numero valido", 400


class Ini(Resource):
    def get(self):
        return "Informe uma chave inteira de -9999 a 9999", 200


api.add_resource(Ini, "/")
api.add_resource(Nums, "/<string:param>")

app.run(debug=True)
