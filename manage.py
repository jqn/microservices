from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import os

DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOSTNAME = os.environ['DB_HOSTNAME']
DB_NAME = os.environ['DB_NAME']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DB_USERNAME}:{DB_PASSWORD}{DB_HOSTNAME}/{DB_NAME}'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))


if __name__ == '__main__':
    manager.run()
