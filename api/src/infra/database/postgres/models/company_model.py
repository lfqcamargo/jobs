from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
from src.infra.database.postgres.settings.base import Base
from src.infra.database.postgres.models.logs_model import LogsModel


class CompanyModel(Base):
    """
    Model Company
    """

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(80), nullable=False)
    link = Column(String(100), nullable=False)

    logs = relationship(
        "LogsModel", back_populates="company", cascade="all, delete-orphan"
    )
