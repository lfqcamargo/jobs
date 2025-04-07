from datetime import datetime
from faker import Faker
from src.domain.jobs.enterprise.entities.question import Question
from src.domain.jobs.application.dto.create_question_dto import CreateQuestionDTO
from src.domain.jobs.enterprise.enums.question_types import QuestionTypes

faker = Faker()


class MakeQuestion:
    """
    Creates a Question object with default values, allowing overrides for specific attributes.

    Args:
        company_id (Optional[int]): The company ID associated with the question.
        user_id (Optional[int]): The user ID who created the question.
        date_time (Optional[datetime]): The datetime when the question was created.
        question_type (Optional[QuestionTypes]): The type of the question.
        question (Optional[str]): The text/content of the question.
        response (Optional[str]): The response to the question, if any.
        identifier (Optional[int]): Unique identifier of the question.

    Returns:
        Question: The created Question instance.
    """

    def __init__(
        self,
        company_id: int = None,
        user_id: int = None,
        date_time: datetime = None,
        question_type: QuestionTypes = None,
        question: str = None,
        response: str = None,
        identifier: int = None,
    ) -> None:
        self.company_id = company_id or faker.random_int(min=1, max=10)
        self.user_id = user_id or faker.random_int(min=1, max=100)
        self.date_time = date_time or datetime.now()
        self.question_type = question_type or QuestionTypes.NUMBER
        self.question = question or faker.sentence(nb_words=10)
        self.response = response or None
        self.identifier = identifier or faker.random_int(min=1, max=1000)

    def make_question_dto(self) -> CreateQuestionDTO:
        """Creates a CreateQuestionDTO with generated or provided data."""
        return CreateQuestionDTO(
            company_id=self.company_id,
            user_id=self.user_id,
            date_time=self.date_time,
            question_type=self.question_type,
            question=self.question,
            response=self.response,
            identifier=self.identifier,
        )

    def make_question(self) -> Question:
        """Creates a Question entity from a DTO."""
        return Question.create(self.make_question_dto())
