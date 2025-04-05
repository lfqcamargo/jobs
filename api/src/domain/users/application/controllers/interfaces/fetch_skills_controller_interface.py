from abc import ABC, abstractmethod
from typing import Union
from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.domain.users.enterprise.entities.skill import Skill


class FetchSkillsControllerInterface(ABC):
    """
    Interface for skill fetching controllers.

    This defines the contract that any implementation of a skill-fetching controller must follow.
    """

    @abstractmethod
    def handle(self, user_id: int) -> Union[list[Skill], ResourceNotFoundError]:
        """
        Handles the logic to fetch all skills associated with a user.

        Args:
            user_id (int): The identifier of the user.

        Returns:
            list[Skill]: A list of Skill entities.
            ResourceNotFoundError: If no skills are found for the user.
        """
