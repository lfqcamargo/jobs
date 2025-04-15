from datetime import date
from dataclasses import dataclass
from typing import Optional


@dataclass
class EditUserDTO:
    """
    DTO Edit User
    """

    def __init__(
        self,
        identifier: int,
        name: str = None,
        email: str = None,
        password: Optional[str] = None,
        birthday_date: date = None,
        curriculum: bytes = None,
        country_code: str = None,
        phone_number: str = None,
    ) -> None:
        self.identifier = identifier
        self.name = name
        self.email = email
        self.password = password
        self.birthday_date = birthday_date
        self.curriculum = curriculum
        self.country_code = country_code
        self.phone_number = phone_number
