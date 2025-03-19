from dataclasses import dataclass


@dataclass
class CreateCompanyDTO:
    """
    DTO Create Company
    """

    def __init__(self, name: str, link: str, identifier: int = 0) -> None:
        self.identifier = identifier
        self.name = name
        self.link = link
