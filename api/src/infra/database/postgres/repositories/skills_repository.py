from src.domain.users.application.interfaces.skills_repository_interface import (
    SkillsRepositoryInterface,
)
from src.infra.database.interfaces.db_connection_handler_interface import (
    DBConnectionHandlerInterface,
)
from src.infra.database.postgres.models.skill_model import SkillModel
from src.domain.users.enterprise.entities.skill import Skill
from src.infra.database.postgres.mappers.skill_mapper import SkillMapper


class SkillsRepository(SkillsRepositoryInterface):
    """
    Repository class for managing Skill data in a PostgreSQL database.

    This class implements the SkillsRepositoryInterface and provides methods
    to retrieve skill records from the database.
    """

    def __init__(self, db_connection: DBConnectionHandlerInterface) -> None:
        self.__db_connection = db_connection

    def fetch_all(self) -> list[Skill] | None:
        with self.__db_connection as database:
            skills_model = database.session.query(SkillModel).all()
            if skills_model:
                skills = []
                for skill in skills_model:
                    skills.append(SkillMapper.to_domain(skill))

                return skills
            return None
