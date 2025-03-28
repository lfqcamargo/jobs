from abc import ABC, abstractmethod
from src.domain.users.enterprise.entities.skill import Skill


class SkillsRepositoryInterface(ABC):
    """
    Interface for the Skills Repository.

    Defines the contract that any implementation of a Skills Repository must follow.
    It provides methods to manage skill data.
    """

    @abstractmethod
    def create(self, skill: Skill) -> bool:
        """
        Persist a new skill in the database.

        Args:
            skill (Skill): The skill entity to be stored.

        Returns:
            bool: True if the skill was successfully created, False otherwise.
        """

    @abstractmethod
    def find_by_identifier(self, identifier: int) -> Skill | None:
        """
        Retrieve a skill by its identifier.

        Args:
            identifier (int): The unique ID of the skill.

        Returns:
            Skill | None: The skill instance if found, otherwise None.
        """

    @abstractmethod
    def fetch_all_by_user(self, user_id: int) -> list[Skill]:
        """
        Retrieve all skills belonging to a specific user.

        Args:
            user_id (int): The user ID.

        Returns:
            list[Skill]: A list of Skill objects associated with the user.
                         Returns an empty list if no skills are found.
        """

    @abstractmethod
    def save(self, skill: Skill) -> bool:
        """
        Update an existing skill in the database.

        Args:
            skill (Skill): The skill entity with updated information.

        Returns:
            bool: True if the skill was successfully updated, False otherwise.
        """

    @abstractmethod
    def delete(self, identifier: int) -> bool:
        """
        Delete a skill by its identifier.

        Args:
            identifier (int): The unique ID of the skill.

        Returns:
            bool: True if the skill was successfully deleted, False otherwise.
        """
