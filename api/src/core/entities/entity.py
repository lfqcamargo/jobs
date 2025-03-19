from abc import ABC


class Entity(ABC):
    """
    Represents a base entity with a unique identifier.
    """

    def __init__(self, identifier: int) -> None:
        self.__identifier = identifier

    def get_identifier(self) -> int:
        """
        Retrieves the unique identifier of the entity.

        :return: The entity's unique identifier.
        """
        return self.__identifier

    def __str__(self) -> str:
        pass
