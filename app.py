from flask import Flask
from flask.ext.cors import CORS
from flask_restful import Resource, Api
from resources.home import Home
from resources.socket import Socket

app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('config.cfg')

cors = CORS(app, resources={r"/socket/*": {"origins": app.config['CORS_ORIGINS']}})

# Add resources
api.add_resource(Home, '/')
api.add_resource(Socket, '/socket/<string:socketNumber>/<string:socketState>')

if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
