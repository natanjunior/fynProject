from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_assets import Environment, Bundle
from flaskext.sass import sass
import os

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://natanjunior/fyndb'
app.config.from_object('config')

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

assets = Environment(app)
sass(app, input_dir='assets/scss', output_dir='static/css')
scss = Bundle('assets/perfil.scss', 'assets/estilo.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)

from app.controllers import perfil
from app.models import tables