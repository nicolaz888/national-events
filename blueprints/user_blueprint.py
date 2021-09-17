from flask import Blueprint

from models.user import User

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/usersapi')


@user_blueprint.route('/users')
def get_users():
    try:
        users = User.query.all()
        return {'users': [user.to_json() for user in users]}, 200
    except Exception as e:
        print(f'error en get_users(): {e}')
        return {'message': 'sorry, we are learning'}, 500
