from faker import Faker
from src.domain.users.enterprise.entities.skill import Skill
from src.domain.users.application.dto.create_skill_dto import CreateSkillDTO
from src.domain.users.enterprise.enums.skill_level import SkillLevel

faker = Faker()


class MakeSkill:
    """
    Creates a Skill object with default values, allowing overrides for specific attributes.

    Args:
        description (Optional[str]): The description of the skill
        (e.g., "Python programming").
        time_month (Optional[int]): The duration (in months) the user has spent learning
        or practicing
        the skill.
        level (Optional[SkillLevel]): The proficiency level of the skill
        (e.g., Beginner, Intermediate, Advanced).
        user_id (Optional[int]): The unique identifier of the user associated with this skill.
        identifier (Optional[int]): The unique identifier for the skill.

    Returns:
        Skill: The created Skill instance with the provided or default properties.
    """

    def __init__(
        self,
        description: str = None,
        time_month: int = None,
        level: SkillLevel = None,
        user_id: int = None,
        identifier: int = None,
    ) -> None:
        self.description = description or faker.word()
        self.time_month = time_month or faker.random_int(min=1, max=120)
        self.level = level or SkillLevel.JUNIOR
        self.user_id = user_id or faker.random_int(min=1, max=100)
        self.identifier = identifier or faker.random_int(min=1, max=1000)

    def make_skill_dto(self) -> CreateSkillDTO:
        """Creates a CreateSkillDTO with generated or provided data."""
        return CreateSkillDTO(
            description=self.description,
            time_month=self.time_month,
            level=self.level,
            user_id=self.user_id,
            identifier=self.identifier,
        )

    def make_skill(self) -> Skill:
        """Creates a Skill entity from a DTO."""
        return Skill.create(self.make_skill_dto())
