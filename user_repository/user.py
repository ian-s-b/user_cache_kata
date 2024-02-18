import json
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    first_name: str
    family_name: str
    age: int
    job: str
    address: str
    biography: str

    def to_json(self):
        return json.dumps(self.__dict__)
