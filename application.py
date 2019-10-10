from flask import Flask
from flask_restplus import Api, Resource


app = Flask(__name__)
api = Api(app)

@app.route('/reviewthis')
Class reviewthis(Resource):
    def get(self):
        return {'hey':'there'}
	
if __name__ == '__main__':
    app.run(debug=True)