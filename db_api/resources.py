import json

from flask import request
from flask_restful import Resource

from db_api.database import db
from db_api.models import UserData
from user_repository.user import User
from user_repository.user_cache import DictUserCache, UserCache


class UserDataResource(Resource):
    """Get and post methods to be used on the database for user data."""
    def __init__(self, cache: UserCache = DictUserCache()):
        self._cache = cache

    def get(self):
        """Get one user data method."""
        first_name = request.args.get('first_name')
        family_name = request.args.get('family_name')

        cached_user: User = self._cache.get_user((first_name, family_name))

        if cached_user is not None:
            cached_user_dict = json.loads(cached_user.to_json())
            return {"data": cached_user_dict, "cached": True}, 200

        if first_name and family_name:
            user_data = UserData.query.filter_by(first_name=first_name, family_name=family_name).first()
            if user_data:
                user_data_json = user_data.json()
                user_obj = User(**user_data_json)
                self._cache.add_user(user_obj)
                return {"data": user_data_json, "cached": False}, 200
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
            self._cache.add_user(User(**json_data))

            return user_data.json(), 201
        else:
            return {'message': 'Invalid data format.'}, 400
        
    def delete(self):
        """Delete one user data method."""
        first_name = request.args.get('first_name')
        family_name = request.args.get('family_name')

        user_data = UserData.query.filter_by(first_name=first_name, family_name=family_name).first()
        if user_data:
            db.session.delete(user_data)
            db.session.commit()
            self._cache.delete_user((first_name, family_name))
            return {'message': 'User data deleted successfully'}, 200
        else:
            return {'message': 'User not found'}, 404
        
    def put(self):
        """Update one user data method."""
        first_name = request.args.get('first_name')
        family_name = request.args.get('family_name')
        json_data = request.get_json()

        user_data = UserData.query.filter_by(first_name=first_name, family_name=family_name).first()
        
        if not user_data:
            return {'message': 'User not found'}, 404

        if json_data:
            user_data.update(json_data)

            db.session.commit()
            self._cache.update_user(User(**json_data), (first_name, family_name))
            return {'message': 'User data updated successfully'}, 200
        else:
            return {'message': 'Invalid data format.'}, 400
            