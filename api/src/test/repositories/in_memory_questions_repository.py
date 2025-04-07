from typing import Optional
from src.domain.jobs.enterprise.entities.question import Question
from src.domain.jobs.application.interfaces.questions_repository_interface import (
    QuestionsRepositoryInterface,
)


class InMemoryQuestionsRepository(QuestionsRepositoryInterface):
    """
    In-memory implementation of the QuestionsRepository for testing purposes.

    This class provides an in-memory storage mechanism for question entities,
    useful for unit testing without relying on a database.
    """

    def __init__(self) -> None:
        self.items: list[Question] = []

    def create(self, question: Question) -> None:
        self.items.append(question)

    def find_by_identifier(self, identifier: int) -> Question | None:
        return next(
            (
                question
                for question in self.items
                if question.get_identifier() == identifier
            ),
            None,
        )

    def fetch_all_by_user(
        self, user_id: int, company: Optional[int] = None
    ) -> list[Question]:
        if company is not None:
            return [
                question
                for question in self.items
                if question.get_user_id() == user_id
                and question.get_company_id() == company
            ]
        return [
            question for question in self.items if question.get_user_id() == user_id
        ]

    def save(self, question: Question) -> bool:
        for i, existing_question in enumerate(self.items):
            if existing_question.get_identifier() == question.get_identifier():
                self.items[i] = question
                return True
        return False

    def delete(self, identifier: int) -> bool:
        for i, question in enumerate(self.items):
            if question.get_identifier() == identifier:
                del self.items[i]
                return True
        return False
