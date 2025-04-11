from typing import Optional
from src.domain.jobs.application.interfaces.questions_repository_interface import (
    QuestionsRepositoryInterface,
)
from src.infra.database.interfaces.db_connection_handler_interface import (
    DBConnectionHandlerInterface,
)
from src.infra.database.postgres.models.question_model import QuestionModel
from src.domain.jobs.enterprise.entities.question import Question
from src.infra.database.postgres.mappers.question_mapper import QuestionMapper


class QuestionsRepository(QuestionsRepositoryInterface):
    """
    Repository class for managing Question data in a PostgreSQL database.

    This class implements the QuestionsRepositoryInterface and provides methods
    to interact with question records in the database.
    """

    def __init__(self, db_connection: DBConnectionHandlerInterface) -> None:
        self.__db_connection = db_connection

    def create(self, question: Question) -> bool:
        with self.__db_connection as database:
            try:
                print(question.get_question_type())
                question_model = QuestionMapper.to_sql(question)
                print("AAAAAAA")
                database.session.add(question_model)
                database.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    def find_by_identifier(self, identifier: int) -> Question | None:
        with self.__db_connection as database:
            question_model = (
                database.session.query(QuestionModel).filter_by(id=identifier).first()
            )
            return QuestionMapper.to_domain(question_model) if question_model else None

    def fetch_all_by_user(
        self, user_id: int, company: Optional[int] = None
    ) -> list[Question]:
        with self.__db_connection as database:
            query = database.session.query(QuestionModel).filter_by(user_id=user_id)

            if company is not None:
                query = query.filter_by(company_id=company)

            questions_model = query.all()
            return [QuestionMapper.to_domain(question) for question in questions_model]

    def save(self, question: Question) -> bool:
        with self.__db_connection as database:
            try:
                question_model: QuestionModel = (
                    database.session.query(QuestionModel)
                    .filter_by(id=question.get_identifier())
                    .first()
                )
                if not question_model:
                    return False

                question_model.date_time = question.get_date_time()
                question_model.question_type = question.get_question_type()
                question_model.question = question.get_question()
                question_model.response = question.get_response()
                database.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    def delete(self, identifier: int) -> bool:
        with self.__db_connection as database:
            try:
                question_model = (
                    database.session.query(QuestionModel)
                    .filter_by(id=identifier)
                    .first()
                )
                if not question_model:
                    return False
                database.session.delete(question_model)
                database.session.commit()
                return True
            except Exception as e:
                print(e)
                return False
