from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from user_repository.db_api.database import db
from user_repository.db_api.resources import UserDataResource

app = Flask(__name__)

basedir = Path(__file__).resolve().parent
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{basedir}/data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Migrate(app, db)
api = Api(app)

# Add your resources to the API here
api.add_resource(UserDataResource, '/user_data')

if __name__ == '__main__':
    app.run(debug=True)
