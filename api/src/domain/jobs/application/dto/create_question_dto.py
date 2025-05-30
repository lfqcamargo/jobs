from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from src.domain.jobs.enterprise.enums.question_types import QuestionTypes


@dataclass
class CreateQuestionDTO:
    """
    DTO Create Question
    """

    def __init__(
        self,
        company_id: int,
        user_id: int,
        date_time: datetime,
        question_type: QuestionTypes,
        question: str,
        response: Optional[str] = None,
        identifier: int = 0,
    ) -> None:
        self.company_id = company_id
        self.user_id = user_id
        self.date_time = date_time
        self.question_type = question_type
        self.question = question
        self.response = response
        self.identifier = identifier
