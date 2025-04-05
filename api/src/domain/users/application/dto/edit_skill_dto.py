from dataclasses import dataclass


@dataclass
class EditSkillDTO:
    """
    DTO Edit Skill
    """

    def __init__(
        self,
        identifier: int,
        description: str = None,
        time_month: int = None,
        level: str = None,
    ) -> None:
        self.identifier = identifier
        self.description = description
        self.time_month = time_month
        self.level = level
