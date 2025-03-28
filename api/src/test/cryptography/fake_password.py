from src.domain.users.application.interfaces.password_handler_interface import (
    PasswordHandlerInterface,
)


class FakerPassword(PasswordHandlerInterface):
    """
    Fake implementation of PasswordHandlerInterface for testing purposes.

    This class simulates password encryption and decryption using simple string manipulations,
    useful for unit testing without relying on actual encryption algorithms.
    """

    def encrypt_password(self, password: str) -> str:
        return f"hashed_{password}"

    def decrypt_password(self, encrypted_password: str) -> str:
        if encrypted_password.startswith("hashed_"):
            return encrypted_password[len("hashed_") :]
        return ""
