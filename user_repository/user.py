from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    first_name: str
    family_name: str
    age: int
    job: str
    address: str
    biography: str
