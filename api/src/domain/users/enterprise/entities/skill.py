from datetime import date
from src.core.entities.entity import Entity
from ...application.dto.create_skill_dto import CreateSkillDTO
from ..enums.skill_level import SkillLevel


class Skill(Entity):
    """
    Represents a skill entity.

    This class extends the base Entity class and includes specific attributes
    and methods related to a skill.
    """

    def __init__(
        self,
        description: str,
        time_month: int,
        level: SkillLevel,
        user_id: int,
        identifier: int = 0,
    ) -> None:
        """
        Initializes a Skill instance.

        Args:
            description (str): A brief description of the skill (e.g., "Python programming").
            time_month (int): The duration (in months) the user has spent learning or practicing
            the skill.
            level (SkillLevel): The proficiency level of the skill (e.g., Beginner, Intermediate,
            Advanced).
            user_id (int): The unique identifier of the user associated with this skill.
            identifier (int, optional): A unique identifier for the skill instance. Defaults to 0.

        Attributes:
            __description (str): The description of the skill.
            __time_month (int): The time, in months, the user has been practicing the skill.
            __level (SkillLevel): The level of proficiency in the skill.
            __user_id (int): The ID of the user who possesses the skill.
        """
        super().__init__(identifier)
        self.__description = description
        self.__time_month = time_month
        self.__level = level
        self.__user_id = user_id

    def get_description(self) -> str:
        """
        Retrieve the skill's description.

        Returns:
            str: The description of the skill.
        """
        return self.__description

    def set_description(self, description: str) -> None:
        """
        Set the skill's description.

        Args:
            description (str): The description to be set for the skill.
        """
        self.__description = description

    def get_time_month(self) -> str:
        """
        Retrieve the skill's time in month.

        Returns:
            str: The time in month of the skill.
        """
        return self.__time_month

    def set_time_month(self, time_month: str) -> None:
        """
        Set the skill's time_month.

        Args:
            time_month (str): The time in month to be set for the skill.
        """
        self.__time_month = time_month

    def get_level(self) -> SkillLevel:
        """
        Retrieve the skill's level.

        Returns:
            str: The level of the skill.
        """
        return SkillLevel(self.__level)

    def set_level(self, level: str) -> None:
        """
        Set the skill's level.

        Args:
            level (str): The level to be set for the skill.
        """
        self.__level = level

    def get_user_id(self) -> date:
        """
        Retrieve the skill's birthday date.

        Returns:
            date: The birthday date of the skill.
        """
        return self.__user_id

    def set_user_id(self, user_id: date) -> None:
        """
        Set the skill's birthday date.

        Args:
            user_id (date): The birthday date to be set for the skill.
        """
        self.__user_id = user_id

    @staticmethod
    def create(props: CreateSkillDTO) -> "Skill":
        """
        Factory method to create a new Skill instance from a DTO.

        Args:
            props (CreateSkillDTO): Data Transfer Object containing skill details.

        Returns:
            Skill: A new instance of Skill with the given properties.
        """
        skill: Skill = Skill(
            description=props.description,
            time_month=props.time_month,
            level=props.level,
            user_id=props.user_id,
            identifier=props.identifier,
        )

        return skill

    def __str__(self) -> str:
        """
        Returns a string representation of the skill.

        Returns:
            str: A formatted string containing skill details.
        """
        return f"user_id: {self.get_user_id()} ID: {self.get_identifier()}, description: {self.__description}, time_month: {self.__time_month}"
