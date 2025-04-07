from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from src.domain.jobs.enterprise.enums.question_types import QuestionTypes


@dataclass
class EditQuestionDTO:
    """
    DTO Edit Question
    """

    def __init__(
        self,
        company_id: int,
        user_id: int,
        identifier: Optional[int] = None,
        date_time: Optional[datetime] = None,
        question_type: Optional[QuestionTypes] = None,
        question: Optional[str] = None,
        response: Optional[str] = None,
    ) -> None:
        self.company_id = company_id
        self.user_id = user_id
        self.identifier = identifier
        self.date_time = date_time
        self.question_type = question_type
        self.question = question
        self.response = response
