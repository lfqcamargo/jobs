from dataclasses import dataclass


@dataclass
class CreateSkillDTO:
    """
    DTO Create Skill
    """

    def __init__(
        self,
        description: str,
        time_month: int,
        level: str,
        user_id: int,
        identifier: int = 0,
    ) -> None:
        self.identifier = identifier
        self.description = description
        self.time_month = time_month
        self.level = level
        self.user_id = user_id
