from src.domain.users.enterprise.entities.skill import Skill
from src.domain.users.application.interfaces.skills_repository_interface import (
    SkillsRepositoryInterface,
)


class InMemorySkillsRepository(SkillsRepositoryInterface):
    """
    In-memory implementation of the SkillRepository for testing purposes.

    This class provides an in-memory storage mechanism for skill entities,
    useful for unit testing without relying on a database.
    """

    def __init__(self) -> None:
        self.items: list[Skill] = []

    def create(self, skill: Skill) -> None:
        self.items.append(skill)

    def find_by_identifier(self, identifier: int) -> Skill | None:
        return next(
            (skill for skill in self.items if skill.get_identifier() == identifier),
            None,
        )

    def fetch_all_by_user(self, user_id: int) -> list[Skill] | None:
        return [skill for skill in self.items if skill.get_user_id() == user_id]

    def save(self, skill: Skill) -> bool:
        for i, existing_skill in enumerate(self.items):
            if existing_skill.get_identifier() == skill.get_identifier():
                self.items[i] = skill
                return True
        return False

    def delete(self, identifier: int) -> bool:
        for i, skill in enumerate(self.items):
            if skill.get_identifier() == identifier:
                del self.items[i]
                return True
        return False
