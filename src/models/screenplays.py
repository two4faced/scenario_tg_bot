from datetime import datetime

from sqlalchemy import String, BIGINT, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.database.database import Base


class ScreenplayORM(Base):
    __tablename__ = "screenplays"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    author_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("users.id"))
    title: Mapped[int] = mapped_column(String(75))
    logline: Mapped[str] = mapped_column(String(40), nullable=True)
    redacted_at: Mapped[datetime]

    __table_args__ = (UniqueConstraint("author_id", "title", name="author_title_uq"),)
