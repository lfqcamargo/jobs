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

    def create(self, skill: Skill) -> bool:
        with self.__db_connection as database:
            skill_model = SkillMapper.to_sql(skill)
            try:
                database.session.add(skill_model)
                database.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    def find_by_identifier(self, identifier: int) -> Skill | None:
        with self.__db_connection as database:
            skill_model = (
                database.session.query(SkillModel).filter_by(id=identifier).first()
            )
            return SkillMapper.to_domain(skill_model) if skill_model else None

    def fetch_all_by_user(self, user_id: int) -> list[Skill]:
        with self.__db_connection as database:
            skills_model = (
                database.session.query(SkillModel).filter_by(user_id=user_id).all()
            )
            return [SkillMapper.to_domain(skill) for skill in skills_model]

    def save(self, skill: Skill) -> bool:
        with self.__db_connection as database:
            try:
                skill_model = (
                    database.session.query(SkillModel)
                    .filter_by(id=skill.get_identifier())
                    .first()
                )
                if not skill_model:
                    return False

                skill_model.description = skill.get_description()
                skill_model.level = skill.get_level()
                skill_model.time_month = skill.get_time_month()
                database.session.commit()
                return True
            except Exception:
                return False

    def delete(self, identifier: int) -> bool:
        with self.__db_connection as database:
            try:
                skill_model = (
                    database.session.query(SkillModel).filter_by(id=identifier).first()
                )
                if not skill_model:
                    return False
                database.session.delete(skill_model)
                database.session.commit()
                return True
            except Exception:
                return False
