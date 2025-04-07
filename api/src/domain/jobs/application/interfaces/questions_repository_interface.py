from typing import Optional
from abc import ABC, abstractmethod
from src.domain.jobs.enterprise.entities.question import Question


class QuestionsRepositoryInterface(ABC):
    """
    Interface for the Questions Repository.

    Defines the contract that any implementation of a Questions Repository must follow.
    It provides methods to manage question data.
    """

    @abstractmethod
    def create(self, question: Question) -> bool:
        """
        Persist a new question in the database.

        Args:
            question (Question): The question entity to be stored.

        Returns:
            bool: True if the question was successfully created, False otherwise.
        """

    @abstractmethod
    def find_by_identifier(self, identifier: int) -> Question | None:
        """
        Retrieve a question by its identifier.

        Args:
            identifier (int): The unique ID of the question.

        Returns:
            Question | None: The question instance if found, otherwise None.
        """

    @abstractmethod
    def fetch_all_by_user(
        self, user_id: int, company: Optional[int] = None
    ) -> list[Question]:
        """
        Retrieve all questions belonging to a specific user.

        Args:
            user_id (int): The user ID.
            company (Optional[int], optional): The company ID to further filter the questions.
                                                Defaults to None.

        Returns:
            list[Question]: A list of Question objects associated with the user.
                            Returns an empty list if no questions are found.
        """

    @abstractmethod
    def save(self, question: Question) -> bool:
        """
        Update an existing question in the database.

        Args:
            question (Question): The question entity with updated information.

        Returns:
            bool: True if the question was successfully updated, False otherwise.
        """

    @abstractmethod
    def delete(self, identifier: int) -> bool:
        """
        Delete a question by its identifier.

        Args:
            identifier (int): The unique ID of the question.

        Returns:
            bool: True if the question was successfully deleted, False otherwise.
        """
