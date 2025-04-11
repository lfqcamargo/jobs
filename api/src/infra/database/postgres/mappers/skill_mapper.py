from src.infra.database.postgres.models.skill_model import SkillModel
from src.domain.users.enterprise.entities.skill import Skill
from src.domain.users.application.dto.create_skill_dto import CreateSkillDTO


class SkillMapper:
    """
    Mapper class for converting between SkillModel (database model) and Skill (domain entity).
    """

    @staticmethod
    def to_domain(raw: SkillModel) -> Skill:
        """
        Converts a SkillModel instance to a Skill domain entity.

        Args:
            raw (SkillModel): The database model instance representing a skill.

        Returns:
            Skill: A domain entity representing the skill.
        """
        dto = CreateSkillDTO(
            identifier=raw.id,
            user_id=raw.user_id,
            description=raw.description,
            time_month=raw.time_month,
            level=raw.level,
        )
        return Skill.create(dto)

    @staticmethod
    def to_sql(skill: Skill) -> SkillModel:
        """
        Converts a Skill domain entity to a SkillModel instance for database persistence.

        Args:
            skill (Skill): The domain entity representing a skill.

        Returns:
            SkillModel: A database model instance representing the skill.
        """
        return SkillModel(
            id=skill.get_identifier() if skill.get_identifier() != 0 else None,
            user_id=skill.get_user_id(),
            description=skill.get_description(),
            time_month=skill.get_time_month(),
            level=skill.get_level(),
        )
