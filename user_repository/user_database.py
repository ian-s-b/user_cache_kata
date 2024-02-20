from abc import ABC, abstractmethod
from typing import Optional, Dict, Tuple, Any

from user_repository.user import User


class UserDatabase(ABC):
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


class MockUserDatabase(UserDatabase):
    def __init__(self):
        self._mock_db: Dict[Tuple[str, str], User] = {}

    @property
    def get_mock_db(self) -> Dict[Tuple[str,str], User]:
        return self._mock_db

    def _is_user_in_db(self, user_id: Tuple[str, str]):
        if user_id in self._mock_db:
            return True
        return False

    def get_user(self, user_id) -> Optional[User]:
        if self._is_user_in_db(user_id):
            return self._mock_db[user_id]
        return None

    def add_user(self, user: User) -> None:
        user_id = (user.first_name, user.family_name)
        if not self._is_user_in_db(user_id):
            self._mock_db[user_id] = user

    def update_user(self, user: User, user_id: Optional[Tuple[str, str]] = None) -> None:
        new_user_id = (user.first_name, user.family_name)
        if user_id is None:
            self._mock_db[new_user_id] = user
        elif self._is_user_in_db(user_id):
            if user_id == new_user_id or not self._is_user_in_db(new_user_id):
                self._mock_db[new_user_id] = user

    def delete_user(self, user_id) -> None:
        if self._is_user_in_db(user_id):
            del self._mock_db[user_id]
