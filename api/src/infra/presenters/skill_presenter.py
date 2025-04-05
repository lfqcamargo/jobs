from src.domain.users.enterprise.entities.skill import Skill


class SkillPresenter:
    """
    Presenter responsible for transforming a Skill entity into an HTTP-friendly format.

    This class provides a method to convert a Skill object into a dictionary
    that can be easily serialized into JSON responses.
    """

    @staticmethod
    def to_http(skill: Skill) -> dict:
        """
        Converts a Skill entity into a dictionary representation.

        Args:
            skill (Skill): The Skill entity to be transformed.

        Returns:
            dict: A dictionary containing the skill's identifier, description, level,
            time in months, and associated user ID.
        """
        return {
            "id": skill.get_identifier(),
            "user_id": skill.get_user_id(),
            "description": skill.get_description(),
            "level": skill.get_level().value,
            "time_month": skill.get_time_month(),
        }
