import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from src.domain.users.application.interfaces.password_handler_interface import (
    PasswordHandlerInterface,
)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY not found in .env")

cipher = Fernet(SECRET_KEY.encode())


class PasswordHandler(PasswordHandlerInterface):
    """
    A class to handle password encryption and decryption using the Fernet symmetric
    encryption algorithm.

    This class implements the PasswordHandlerInterface and provides methods to encrypt and decrypt
    passwords securely using a secret key stored in an environment variable.

    Attributes:
        cipher (Fernet): The Fernet encryption cipher initialized with the secret key.
    """

    def encrypt_password(self, password: str) -> str:
        """Encrypts the password using Fernet."""
        return cipher.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password: str) -> str:
        """Decrypts the password using Fernet."""
        return cipher.decrypt(encrypted_password.encode()).decode()
