import os
from flask import Flask, request, Blueprint, url_for
from flask_restplus import Resource, Api, Namespace, fields

def create_app():
    app = Flask(__name__)
    api = Api(app, version="1.0", title="API title", description="A simple API")

    app.config.SWAGGER_UI_DOC_EXPANSION = "full"
    database = {}

    class MyApi(Api):
        @property
        def specs_url(self):
            scheme = os.environ.get('SCHEME')
            return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)
        
    api_bp = Blueprint('api', __name__)
    swagger_doc = os.environ.get('SWAGGER_DOC', '/doc')
    my_api = MyApi(api_bp,
                doc=swagger_doc,
                static_url_path='/swaggerurl',
                title='API Test',
                version='1.0.0')

    user_api_ns = Namespace('user', description="User")
    my_api.add_namespace(user_api_ns)

    user_res = my_api.model(
        'user_res', {
            'user_id': fields.String(required=True, description='User ID')
        }
    )

    @api.route('/hello')
    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}
        
    @api.route('/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    class IdSimple(Resource):
        def get(self, id):
            print(request.args.to_dict())
            if database.get(id):
                return {"id": id, "name": database[id]}
            else:
                return {"id": id, "name": "none"}

        
        def post(self, id):
            data = request.get_json(force=True)
            print("req : ", data)
            database[id] = data['name']
            return {"id": id, "name": database[id]}
            

        def put(self, id):
            data = request.get_json(force=True)
            print("req : ", data)
            if database.get(id):
                database[id] = data['name']
                return {"id": id, "name": database[id]}
            else:
                return {f"{id} not in database"}
    return app
        

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
