from datetime import datetime
from src.core.entities.entity import Entity
from src.domain.jobs.enterprise.enums.question_types import QuestionTypes
from src.domain.jobs.application.dto.create_question_dto import CreateQuestionDTO


class Question(Entity):
    """
    Represents a question entity.

    This class extends the base Entity class and includes specific attributes
    and methods related to a question.
    """

    def __init__(
        self,
        company_id: int,
        user_id: int,
        date_time: datetime,
        question: str,
        response: str,
        question_type: QuestionTypes,
        identifier: int = 0,
    ) -> None:
        """
        Initializes a Question instance.

        Args:
            company_id (int): The ID of the company associated with the question.
            user_id (int): The ID of the user who asked the question.
            date_time (datetime): The timestamp when the question was asked.
            question_type (QuestionTypes): The type of the question input (e.g., text,
            number, date).
            question (str): The content of the question.
            response (str): The answer to the question.
            identifier (int, optional): The unique identifier of the question. Defaults to 0.
        """
        super().__init__(identifier)
        self.__company_id = company_id
        self.__user_id = user_id
        self.__date_time = date_time
        self.__question_type = question_type
        self.__question = question
        self.__response = response

    def get_company_id(self) -> int:
        """
        Retrieve the company ID associated with the question.

        Returns:
            int: The company ID of the question.
        """
        return self.__company_id

    def get_user_id(self) -> int:
        """
        Retrieve the user ID associated with the question.

        Returns:
            int: The user ID of the question.
        """
        return self.__user_id

    def get_date_time(self) -> datetime:
        """
        Retrieve the timestamp when the question was asked.

        Returns:
            datetime: The date and time when the question was asked.
        """
        return self.__date_time

    def get_question_type(self) -> QuestionTypes:
        """
        Retrieve the type of the question input.

        Returns:
            QuestionTypes: The type of input associated with the question (e.g., text,
            number, date).
        """
        return QuestionTypes(self.__question_type)

    def get_question(self) -> str:
        """
        Retrieve the content of the question.

        Returns:
            str: The question itself.
        """
        return self.__question

    def get_response(self) -> str | None:
        """
        Retrieve the response to the question.

        Returns:
            str: The response to the question.
        """
        return self.__response

    def set_date_time(self, date_time: datetime) -> None:
        """
        Set the timestamp when the question was asked.

        Args:
            date_time (datetime): The new date and time to set.
        """
        self.__date_time = date_time

    def set_question_type(self, question_type: QuestionTypes) -> None:
        """
        Set the type of the question input.

        Args:
            question_type (QuestionTypes): The new type of input associated with the question.
        """
        self.__question_type = question_type

    def set_question(self, question: str) -> None:
        """
        Set the content of the question.

        Args:
            question (str): The new question content.
        """
        self.__question = question

    def set_response(self, response: str) -> None:
        """
        Set the response to the question.

        Args:
            response (str): The new response content.
        """
        self.__response = response

    @staticmethod
    def create(props: CreateQuestionDTO) -> "Question":
        """
        Factory method to create a new Question instance from a DTO.

        Args:
            props (CreateQuestionDTO): A Data Transfer Object containing the
            details of the question.

        Returns:
            Question: A new instance of Question with the given properties.
        """
        return Question(
            company_id=props.company_id,
            user_id=props.user_id,
            date_time=props.date_time,
            question_type=props.question_type,
            question=props.question,
            response=props.response,
            identifier=props.identifier,
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the question.

        Returns:
            str: A formatted string containing the question's details (ID, question, and response).
        """
        return f"ID: {self.__identifier}, Question: {self.__question}, Response: {self.__response}"
