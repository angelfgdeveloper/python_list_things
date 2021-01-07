import os

from flask import Flask

# Paso 2
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    from . import db

    db.init_app(app)

    @app.route('/hola')
    def hola():
        return 'Chanchihto Feliz'

    return app

# Paso 1
# INSTALACIONES
# pip install werkzeug
# pip install mysql-connector-python
# pip install Flask

# Paso 3
# antes de correr utilizar el archivo con el comando
# set FLASK_APP=todo
# set FLASK_ENV=development
# flask run