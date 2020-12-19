from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class Convert(Resource):
    def get(self):
        base = request.args.get('base')
        temp = float(request.args.get('temp'))
        if base == 'celsius':
            result = temp * 9/5 + 32
        elif base == 'fahrenheit':
            result = (temp - 32) * 5/9
        print(result)
        return result

api.add_resource(Convert, '/convert')

if __name__ == 'main':
    app.run()
