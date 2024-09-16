from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Model


class TaskOrm(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]
    password: Mapped[Optional[str]]
    status: Mapped[int] = 0

    transistor = relationship("TransistorOrm", back_populates="users")