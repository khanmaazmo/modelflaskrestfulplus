from flask import Flask, request
from flask_restplus import Api, Resource


app = Flask(__name__)
api = Api(app)  #api = App(app, doc = False)

app.config['SWAGGER_UI_JSONEDITOR'] = True

a_language = api.model('Language', {'language': fields.String('The Language.')}) #, 'id' : fields.Integer('ID')

languages = []
python = {'language' : 'Python', 'id' : 1}
language.append(python)

@app.route('/language')
Class Language(Resource):

    @api.marshal_with(a_language, envelope = 'data') 
    def get(self):
        #return {'hey':'there'}
	    return languages

    @api.expect(a_language)
    def post(self):
	    new_language = api.payload
		new_language[id] = len(languages) + 1
	    languages.append(new_language)
		return {'result' : 'Language added'}, 201
		
if __name__ == '__main__':
    app.run(debug=True)