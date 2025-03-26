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
            description=raw.description,
            time_month=raw.time_month,
            level=raw.level,
            user_id=raw.user_id,
        )
        return Skill.create(dto)
