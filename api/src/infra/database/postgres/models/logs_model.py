from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from src.infra.database.postgres.settings.base import Base
from src.infra.database.postgres.models.user_model import UserModel


class LogsModel(Base):
    """
    Model Logs
    """

    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    description = Column(String(1000), nullable=False)
    type = Column(String(100))
    datetime = Column(DateTime)

    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    company = relationship("CompanyModel", back_populates="logs")

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("UserModel", back_populates="logs")
