from abc import ABC, abstractmethod


class DBConnectionHandlerInterface(ABC):
    """
    Abstract base class for database connection handlers.

    This class defines the contract for any class that handles database
    connections. It provides methods for establishing a connection and
    retrieving the database engine.
    """

    @abstractmethod
    def connect_to_db(self) -> None:
        """
        Connect DB
        """

    def get_engine(self) -> any:
        """
        Get Engine
        """

    def __enter__(self) -> any:
        pass

    def __exite__(self) -> None:
        pass
