# pylint: skip-file
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.infra.drivers.password_handler import PasswordHandler


password_handler = PasswordHandler()
password_hashed = password_handler.encrypt_password("123")
print(password_hashed)

password = password_handler.decrypt_password(password_hashed)
print(password)
