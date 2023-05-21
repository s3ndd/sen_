from http import HTTPStatus

from flask import Blueprint, jsonify, request

from app.schema import UserSchema
from app.service import UserService

user_route = Blueprint('user_route', __name__)

user_service = UserService()
user_schema = UserSchema()


@user_route.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users), HTTPStatus.OK


@user_route.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user), HTTPStatus.OK
    return jsonify({'message': 'User not found'}), HTTPStatus.NOT_FOUND


@user_route.route('/users', methods=['POST'])
def create_user():
    user = user_service.create_user(request.get_json())
    return jsonify(user), HTTPStatus.CREATED


@user_route.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = user_service.update_user(user_id, request.get_json())
    if user:
        return jsonify(user), HTTPStatus.OK
    return jsonify({'message': 'User not found'}), HTTPStatus.NOT_FOUND


@user_route.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return jsonify(user_service.delete_user_by_id(user_id)), HTTPStatus.NO_CONTENT
