from typing import Optional, Any

from user_repository.user import User
from user_repository.user_cache import UserCache, DictUserCache
from user_repository.user_database import UserDatabase, MockUserDatabase


class UserRepository:
    def __init__(self, cache: UserCache = DictUserCache(), database: UserDatabase = MockUserDatabase()):
        self._cache = cache
        self._database = database

    def get_cache(self) -> UserCache:
        return self._cache

    def get_database(self) -> UserDatabase:
        return self._database

    def get_user(self, user_id: Any) -> Optional[User]:
        cached_user = self._cache.get_user(user_id)
        if cached_user is not None:
            return cached_user
        database_user = self._database.get_user(user_id)
        if database_user:
            self._cache.add_user(database_user)
        return database_user

    def add_user(self, user: User) -> None:
        self._database.add_user(user)
        self._cache.add_user(user)

    def update_user(self, user: User, user_id: Any) -> None:
        self._database.update_user(user, user_id)
        self._cache.update_user(user, user_id)
