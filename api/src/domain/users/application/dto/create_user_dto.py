from datetime import date
from dataclasses import dataclass


@dataclass
class CreateUserDTO:
    """
    DTO Create User
    """

    def __init__(
        self,
        name: str,
        email: str,
        password: str,
        birthday_date: date,
        curriculum: bytes,
        country_code: str,
        phone_number: str,
        identifier: int = 0,
    ) -> None:
        self.identifier = identifier
        self.name = name
        self.email = email
        self.password = password
        self.birthday_date = birthday_date
        self.curriculum = curriculum
        self.country_code = country_code
        self.phone_number = phone_number
