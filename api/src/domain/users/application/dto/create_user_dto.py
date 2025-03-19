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
        identifier: int = 0,
    ) -> None:
        self.identifier = identifier
        self.name = name
        self.email = email
        self.password = password
        self.birthday_date = birthday_date
