from enum import Enum


class SkillLevel(Enum):
    """
    Enumeration representing the possible skill levels.

    Attributes:
        JUNIOR (str): Represents a junior level skill.
        PLENO (str): Represents a mid-level (Pleno) skill.
        SENIOR (str): Represents a senior level skill.
        ESPECIALISTA (str): Represents a specialist level skill.
    """

    JUNIOR = "Junior"
    MID_LEVEL = "Pleno"
    SENIOR = "Senior"
    SPECIALIST = "Especialista"
