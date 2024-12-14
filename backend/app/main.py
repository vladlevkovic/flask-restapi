from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from db_connection import get_quote, create, update, quote_delete

app = Flask(__name__)
api = Api(app)
CORS(app)

def row_json(quote):
    print(type(quote))
    data = {'id': quote['id'], 'author': quote['author'], 'quote': quote['quote']}
    json_data = jsonify(data)
    json_data.status_code = 200
    return json_data

class Quote(Resource):
    def get(self, quote_id):
        quote = get_quote(quote_id)
        if quote:
            quote_json = row_json(quote)
            print(quote_json)
            return quote_json
        return {'message': 'Quote not found', 'status': 404}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('author')
        parser.add_argument('quote')
        params = parser.parse_args()
        answer = create(params['author'], params['quote'])
        json_data = jsonify(f'Records create with id {answer}')
        json_data.status_code = 201
        return json_data

    def put(self, quote_id):
        parser = reqparse.RequestParser()
        parser.add_argument('author')
        parser.add_argument('quote')
        params = parser.parse_args()
        update(params['author'], params['quote'], quote_id)
        json_data = jsonify(f'Зміни записано для id {quote_id}')
        json_data.status_code = 200
        return json_data

    def delete(self, quote_id):
        quote_delete(quote_id)
        json_data = jsonify(f'Цитату видалено з id {quote_id}')
        json_data.status_code = 200
        return json_data

api.add_resource(Quote, '/api/v1/quotes/<int:quote_id>', '/api/v1/quotes')

if __name__ == '__main__':
    app.run(debug=True)
