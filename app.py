from flask import Flask, request
from flask.json import jsonify
from http import HTTPStatus

from flask_restful import Api, Resource

from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource
from resources.recipe_publish import RecipepublishResource
from resources.register import UserRegisterResource
from flask_jwt_extended import JWTManager

app = Flask(__name__)
# JWT 토큰 만들기
jwt = JWTManager(app)

api = Api(app)

app.config.from_object(Config)

# 경로와 리소스를 연결한다.
api.add_resource(RecipeListResource, '/recipes')
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipepublishResource,   '/recipes/<int:recipe_id>/publish')
api.add_resource(UserRegisterResource,   '/user/register')
if __name__ == "__main__" :
    app.run()

## export FLASK_APP=app.py
## export FLASK_RUN_PORT=5000