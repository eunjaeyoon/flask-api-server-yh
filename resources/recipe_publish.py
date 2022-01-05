from flask import request
from flask.json import jsonify
from flask_restful import Resource
from http import HTTPStatus

from mysql_connection import get_connection
from mysql.connector.errors import Error

class RecipepublishResource(Resource) :
    def put(self, recipe_id) :


        return {'result' :'이 레시피는 공개로 설정 되었습니다. '},HTTPStatus































    def delete(self, recipe_id) :
        #1. DB에 연결
        connection = get_connection()

        #2. 쿼리문 만들고