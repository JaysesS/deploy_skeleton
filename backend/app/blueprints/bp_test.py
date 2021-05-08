from flask import Blueprint
from flask import current_app, jsonify
from random import randint

from models import User

t_blueprint = Blueprint('t_blueprint', __name__)

@t_blueprint.route('/')
def index():
    return f"<h2><p>Test blueprint</p><p>Test word: {current_app.config.get('TEST_WORD')}</p></h2>"

@t_blueprint.route('/test_db')
def test_db():

    for _ in range(100):
        r1 = randint(1, 100000000000)
        r2 = randint(1, 10000000000)
        r3 = randint(1, 10000000000)
        print("Write", r1, r2, r3)
        user = User(name = r1, password=r2, email=r3)
        user.save_to_db()

    return jsonify(status=True)

@t_blueprint.route('/view_db')
def view_db():

    users = User.query.all()
    result = [
        {
            "name" : user.name,
            "password" : user.password,
            "email" : user.email
        }
        for user in users
    ]
    return jsonify(status=True, result = result)
