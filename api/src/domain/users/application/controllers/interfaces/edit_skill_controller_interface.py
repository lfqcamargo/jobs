from abc import ABC, abstractmethod
from typing import Optional
from src.domain.users.enterprise.enums.skill_level import SkillLevel


class EditSkillControllerInterface(ABC):
    """
    Interface for skill editing controllers.

    This class defines the contract that any implementation of a skill editing controller
    must follow. It provides a method to handle skill update requests.

    Methods:
        handle(identifier: int, description: Optional[str], time_month: Optional[int],
        level: Optional[SkillLevel]) -> None:
            Handles the skill editing logic.
    """

    @abstractmethod
    def handle(
        self,
        identifier: int,
        description: Optional[str],
        time_month: Optional[int],
        level: Optional[SkillLevel],
    ) -> None:
        """
        Handles the skill editing logic.

        Args:
            identifier (int): Identifier of the skill to be edited.
            description (Optional[str]): New description of the skill.
            time_month (Optional[int]): New time in months of experience.
            level (Optional[SkillLevel]): New skill level.

        Raises:
            ResourceNotFoundError: If the skill does not exist in the system.
            DomainError: For any unexpected domain-related errors.

        Returns:
            None: If the edit is successful.
        """
