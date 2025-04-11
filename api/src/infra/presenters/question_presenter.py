from src.domain.jobs.enterprise.entities.question import Question


class QuestionPresenter:
    """
    Presenter responsible for transforming a Question entity into an HTTP-friendly format.

    This class provides a method to convert a Question object into a dictionary
    that can be easily serialized into JSON responses.
    """

    @staticmethod
    def to_http(question: Question) -> dict:
        """
        Converts a Question entity into a dictionary representation.

        Args:
            question (Question): The Question entity to be transformed.

        Returns:
            dict: A dictionary containing the question's identifier, company ID, user ID,
            timestamp, question content, response content, and question type.
        """
        return {
            "id": question.get_identifier(),
            "company_id": question.get_company_id(),
            "user_id": question.get_user_id(),
            "date_time": question.get_date_time().isoformat(),
            "question": question.get_question(),
            "response": question.get_response(),
            "question_type": question.get_question_type().value,
        }
