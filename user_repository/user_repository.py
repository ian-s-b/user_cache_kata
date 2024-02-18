from dataclasses import dataclass


@dataclass
class User:
    firstName: str
    familyName: str
    age: int
    job: str
    address: str
    biography: str


class UserRepository:
    def __init__(self):
        pass

    def get_user(self) -> User:
        pass

    def add_user(self) -> None:
        pass

    def update_user(self) -> None:
        pass
