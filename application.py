from flask import Flask, request
from flask_restplus import Api, Resource


app = Flask(__name__)
api = Api(app)

a_language = api.model('Language', {'language': fields.String('The Language.')})

languages = []
python = {'language':'Python'}
language.append(python)

@app.route('/language')
Class Language(Resource):
    def get(self):
        #return {'hey':'there'}
	    return languages

    @api.expect(a_language)
    def post(self):
	    languages.append(api.payload)
		return {'result' : 'Language added'}, 201
		
if __name__ == '__main__':
    app.run(debug=True)