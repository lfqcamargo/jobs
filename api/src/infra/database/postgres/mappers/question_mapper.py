from src.infra.database.postgres.models.question_model import QuestionModel
from src.domain.jobs.enterprise.entities.question import Question
from src.domain.jobs.application.dto.create_question_dto import CreateQuestionDTO


class QuestionMapper:
    """
    Mapper class for converting between QuestionModel (database model) and Question (domain entity).
    """

    @staticmethod
    def to_domain(raw: QuestionModel) -> Question:
        """
        Converts a QuestionModel instance to a Question domain entity.

        Args:
            raw (QuestionModel): The database model instance representing a question.

        Returns:
            Question: A domain entity representing the question.
        """
        dto = CreateQuestionDTO(
            identifier=raw.id,
            company_id=raw.company_id,
            user_id=raw.user_id,
            date_time=raw.date_time,
            question=raw.question,
            response=raw.response,
            question_type=raw.question_type,
        )
        return Question.create(dto)

    @staticmethod
    def to_sql(question: Question) -> QuestionModel:
        """
        Converts a Question domain entity to a QuestionModel instance for database persistence.

        Args:
            question (Question): The domain entity representing a question.

        Returns:
            QuestionModel: A database model instance representing the question.
        """

        return QuestionModel(
            id=question.get_identifier() if question.get_identifier() != 0 else None,
            company_id=question.get_company_id(),
            user_id=question.get_user_id(),
            date_time=question.get_date_time(),
            question_type=question.get_question_type(),
            question=question.get_question(),
            response=question.get_response(),
        )
