from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from src.infra.database.postgres.settings.base import Base
from src.domain.users.enterprise.entities.skill import SkillLevel


class SkillModel(Base):
    """
    Model Skill
    """

    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    description = Column(String(255), nullable=False)
    time_month = Column(Integer(), nullable=False)
    level = Column(Enum(SkillLevel), nullable=False)

    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
