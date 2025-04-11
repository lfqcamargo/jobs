from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum
from src.infra.database.postgres.settings.base import Base
from src.domain.jobs.enterprise.enums.question_types import QuestionTypes


class QuestionModel(Base):
    """
    Model for Question.
    """

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    date_time = Column(DateTime, nullable=False)
    question_type = Column(Enum(QuestionTypes), nullable=False)
    question = Column(String(255), nullable=False)
    response = Column(String, nullable=True)

    company_id = Column(
        Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
