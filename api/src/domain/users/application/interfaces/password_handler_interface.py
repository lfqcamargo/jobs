from abc import ABC, abstractmethod


class PasswordHandlerInterface(ABC):
    """
    Interface for the Users Repository.

    This class defines the contract that any implementation of a Users Repository
    must follow. It provides methods to retrieve user data.
    """

    @abstractmethod
    def encrypt_password(self, password: str) -> str:
        """Encrypts the password using Fernet."""

    @abstractmethod
    def decrypt_password(self, encrypted_password: str) -> str:
        """Decrypts the password using Fernet."""
