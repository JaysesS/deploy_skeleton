from flask import Flask
from flask_cors import CORS
from config import TestConfig, DevConfig
from models import db

from blueprints.bp_test import t_blueprint

def create_app():
    
    app = Flask(__name__)
    CORS(app, resources={r'/*': {"origins": "*"}})

    # Init config
    app.config.from_object(DevConfig())

    db.init_app(app)

    @app.before_first_request
    def create_test_admin():
        db.create_all()

    # Register blueprints
    app.register_blueprint(t_blueprint)

    return app

def create_test_app():

    app = Flask(__name__)
    CORS(app, resources={r'/*': {"origins": "*"}})

    # Init config
    app.config.from_object(TestConfig())

    db.init_app(app)

    @app.before_first_request
    def create_test_admin():
        db.create_all()

    # Register blueprints
    app.register_blueprint(t_blueprint)

    return app