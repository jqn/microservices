# app/__init__.py

# third-party imports
from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import os

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
#  Login manager initialization
login_manager = LoginManager()


def create_app(config_name):
    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI="mysql://{username}:{password}@{hostname}/{databasename}".format(
                username=os.environ['DB_USERNAME'],
                password=os.environ['DB_PASSWORD'],
                hostname=os.environ['DB_HOSTNAME'],
                databasename=os.environ['DB_NAME'],
            )
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    from app import models

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .ratings import ratings as ratings_blueprint
    app.register_blueprint(ratings_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    # Test round for 500 error
    @app.route('/500')
    def error():
        abort(500)

    return app
