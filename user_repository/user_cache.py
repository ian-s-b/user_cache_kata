from abc import ABC, abstractmethod
from typing import Optional, Any, Tuple

from user_repository.user import User


class UserCache(ABC):
    @abstractmethod
    def get_user(self, user_id: Any):
        pass

    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def update_user(self, user: User, user_id: Any):
        pass

    @abstractmethod
    def delete_user(self, user_id: Any):
        pass

    @abstractmethod
    def clean_cache(self):
        pass


class DictUserCache(UserCache):
    def __init__(self, cache_limit: int = 10):
        self._cache = {}
        self._cache_limit = cache_limit

    def _is_user_in_cache(self, user_id: Tuple[str, str]):
        if user_id in self._cache:
            return True
        return False

    def get_user(self, user_id) -> Optional[User]:
        if self._is_user_in_cache(user_id):
            return self._cache[user_id]
        return None

    def add_user(self, user: User) -> None:
        user_id = (user.first_name, user.family_name)
        if not self._is_user_in_cache(user_id):
            while len(self._cache) >= self._cache_limit:
                first_key = next(iter(self._cache))
                self._cache.pop(first_key)
            self._cache[user_id] = user

    def update_user(self, user: User, user_id=None) -> None:
        new_user_id = (user.first_name, user.family_name)
        if user_id is None:
            self._cache[new_user_id] = user
        elif self._is_user_in_cache(user_id):
            if user_id == new_user_id or not self._is_user_in_cache(new_user_id):
                self._cache[new_user_id] = user

    def delete_user(self, user_id) -> None:
        if self._is_user_in_cache(user_id):
            del self._cache[user_id]

    def clean_cache(self):
        self._cache = {}
