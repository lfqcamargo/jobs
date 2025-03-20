from sqlalchemy import Column, String, Integer, Date
from src.infra.database.postgres.settings.base import Base


class UserModel(Base):
    """
    Model User
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(80), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(300), nullable=False)
    birthday_date = Column(Date, nullable=False)
