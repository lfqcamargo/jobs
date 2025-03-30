from datetime import datetime
from dataclasses import dataclass


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
        question: str,
        response: str,
        identifier: int = 0,
    ) -> None:
        self.company_id = company_id
        self.user_id = user_id
        self.date_time = date_time
        self.question = question
        self.response = response
        self.identifier = identifier
