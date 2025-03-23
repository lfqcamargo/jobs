from pydantic import BaseModel, Field


def delete_user_validator(identifier: int) -> None:
    """
    Validates the user data for deletion by identifier.

    Args:
        identifier (int): The identifier of the user to be deleted.

    Raises:
        ValidationError: If the validation fails for the identifier field.
    """

    class BodyData(BaseModel):
        """
        Validate the schema for the user deletion data.
        """

        identifier: int = Field(..., gt=0)

    try:

        BodyData(identifier=identifier)
    except ValueError as error:
        raise error
