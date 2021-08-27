from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.serving import WSGIRequestHandler
import json
import os

UPLOAD_FOLDER = "../data/trip"

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['SECRET_KEY'] = "blabla"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Deneme(Resource):

    def patch(self):
        try:
            if 'recording' not in request.files:
                resp = jsonify({'message' : 'No file part in the request'})
                resp.status_code = 400
                return resp

            file = request.files["recording"]
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            resp = jsonify({'message' : 'File successfully uploaded'})
            resp.status_code = 201
            return resp
        
        except Exception as err:
            resp = jsonify({'error' : f'{err}',
                            'filename' : f'{file.filename}',
                            'message' : 'Failed!' })
            resp.status_code = 400
            return resp
api.add_resource(Deneme, "/file")        
WSGIRequestHandler.protocol_version = "HTTP/1.1"    

class Markers(Resource):
    def get(self):
        df = open("./LoadData/ss.txt","r")
        markers = json.loads(df.read())
        df.close()
        resp = jsonify({
        "markers":markers
    })
        resp.status_code = 201
        return resp  

api.add_resource(Markers, "/markers")        
WSGIRequestHandler.protocol_version = "HTTP/1.1" 



if __name__ == "__main__":
    app.run(host='0.0.0.0')

