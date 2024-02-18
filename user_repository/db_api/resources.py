from flask import request
from flask_restful import Resource

from user_repository.db_api.database import db
from user_repository.db_api.models import UserData


class UserDataResource(Resource):
    """Get and post methods to be used on the database for user data."""

    def get(self):
        """Get one user data method."""
        first_name = request.args.get('first_name')
        family_name = request.args.get('family_name')

        if first_name and family_name:
            user_data = UserData.query.filter_by(first_name=first_name, family_name=family_name).first()
            if user_data:
                return user_data.json(), 200
            else:
                return {'message': 'User not found'}, 404
        else:
            return {'message': 'Missing first_name or family_name parameter.'}, 400

    def post(self):
        """Post one user data method."""
        json_data = request.get_json()
        if json_data:
            user_data = UserData(json_data)
            db.session.add(user_data)
            db.session.commit()

            return user_data.json(), 201
        else:
            return {'message': 'Invalid data format.'}, 400
