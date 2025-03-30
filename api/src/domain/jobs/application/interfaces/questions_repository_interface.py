from abc import ABC, abstractmethod
from src.domain.jobs.enterprise.entities.question import Question


class QuestionsRepositoryInterface(ABC):
    """
    Interface for the Questions Repository.

    This class defines the contract that any implementation of a Questions Repository
    must follow. It provides methods to retrieve question data.
    """

    @abstractmethod
    def create(self, question: Question) -> bool:
        """
        Persists a new questionin the database.

        This method takes a domain entity representing a questionand saves it in the database.
        Implementations should handle the persistence logic, ensuring the questiondata is stored
        correctly.

        Args:
            question(Question): The domain entity representing the questionto be stored.

        Returns:
            bool
        """

    @abstractmethod
    def find_by_question(
        self, company_id: int, user_id: int, question: str
    ) -> Question | None:
        """
        Retrieve a question by its question.

        Returns:
            Question | None: The question instance if found, otherwise None.
        """
