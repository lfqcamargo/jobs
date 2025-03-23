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
        name: str,
        email: str,
        password: Optional[str],
        birthday_date: date,
        identifier: int,
    ) -> None:
        self.identifier = identifier
        self.name = name
        self.email = email
        self.password = password
        self.birthday_date = birthday_date
