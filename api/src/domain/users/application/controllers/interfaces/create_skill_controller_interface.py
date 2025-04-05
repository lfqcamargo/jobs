from abc import ABC, abstractmethod


class CreateSkillControllerInterface(ABC):
    """
    Interface for the skill creation controllers.

    This class defines the contract that any implementation of a skill creation controller
    must follow. It provides a method to handle skill creation requests.

    Methods:
        handle(user_id: str, description: str, time_month: int, level: str) -> None:
            Handles the skill creation logic. This method is implemented in the controller.
    """

    @abstractmethod
    def handle(
        self,
        user_id: str,
        description: str,
        time_month: int,
        level: str,
    ) -> None:
        """
        Handles the skill creation logic.

        This method takes skill details as individual arguments and performs the skill
        creation logic.
        It may raise specific exceptions in case of errors, such as `ResourceNotFoundError`
        if the user is not found, or `DomainError` for any unexpected domain-related errors.

        Args:
            user_id (str): Identifier of the user to whom the skill belongs.
            description (str): Description of the skill.
            time_month (int): Time of experience in months with the skill.
            level (str): Skill level (e.g., beginner, intermediate, advanced).

        Raises:
            ResourceNotFoundError: If the user does not exist in the system.
            DomainError: For any unexpected domain-related errors encountered in the domain layer.

        Returns:
            None: Returns `None` if the skill creation is successful.
        """
