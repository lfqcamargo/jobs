from abc import ABC, abstractmethod
from src.domain.users.enterprise.entities.skill import Skill


class SkillsRepositoryInterface(ABC):
    """
    Interface for the Skills Repository.

    This class defines the contract that any implementation of a Skills Repository
    must follow. It provides methods to retrieve skill data.
    """

    @abstractmethod
    def create(self, skill: Skill) -> bool:
        """
        Persists a new skill in the database.

        This method takes a domain entity representing a skill and saves it in the database.
        Implementations should handle the persistence logic, ensuring the skill data is stored
        correctly.

        Args:
            skill (Skill): The domain entity representing the skill to be stored.

        Returns:
            bool
        """

    @abstractmethod
    def fetch_all(self) -> list[Skill] | None:
        """
        Retrieves all skills from the database.

        This method queries the database and returns a list of all skill entities stored.
        The implementation should handle the retrieval logic, ensuring that the list of skills
        is accurate and complete.

        Returns:
            list[Skill] | None: A list of Skill objects representing all skills in the database
            or None.
        """
