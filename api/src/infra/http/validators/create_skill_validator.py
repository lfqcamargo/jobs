from pydantic import BaseModel, ValidationError, Field
from src.domain.users.enterprise.enums.skill_level import SkillLevel
from src.infra.http.views.http_types.http_request import HttpRequest


def create_skill_validator(http_request: HttpRequest) -> None:
    """
    Validates the skill data in the given HTTP request for a skill.

    Args:
        http_request (HttpRequest): The HTTP request containing the skill data.

    Raises:
        ValidationError: If validation fails for any of the fields in the request body.
        ValueError: If the skill ID is missing from the request parameters.
    """

    class BodyData(BaseModel):
        """
        Schema for validating the skill creation body payload.
        """

        description: str = Field(
            ..., min_length=3, max_length=50, description="Skill description"
        )
        time_month: int = Field(
            ..., description="Time in months of experience with the skill"
        )
        level: SkillLevel = Field(
            ..., description="Skill level (e.g., beginner, intermediate, advanced)"
        )

    try:
        BodyData(**http_request.body)
    except ValidationError as error:
        raise error

    if "user_id" not in http_request.params:
        raise ValueError("user ID is required to create a skill.")
