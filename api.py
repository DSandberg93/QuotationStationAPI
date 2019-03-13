from flask import Flask
from flask_restful import Resource, Api
import json
from random import choice
from quotes import quotes

app = Flask(__name__)
api = Api(app)

class Quote(Resource):
    def get(self, supercat=False, category=False, param=False):
        quote = quotes
        if supercat:
            quote = quote.get(supercat)
            if category:
                quote = quote.get(category)
                if param:
                    quote = quote.get(param)
        while type(quote) == dict:
            quote = quote.get(choice(list(quote.keys())))
        return {'quote': choice(quote)}

api.add_resource(Quote,
    '/api',
    '/api/',
    '/api/<string:supercat>',
    '/api/<string:supercat>/',
    '/api/<string:supercat>/<string:category>',
    '/api/<string:supercat>/<string:category>/',
    '/api/<string:supercat>/<string:category>/<string:param>',
    '/api/<string:supercat>/<string:category>/<string:param>/'
    )

app.run(port=5000)
