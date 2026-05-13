from sqlalchemy import BIGINT
from sqlalchemy.orm import mapped_column, Mapped

from src.database.database import Base


class UsersORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
