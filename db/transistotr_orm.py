from typing import Optional

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, MappedColumn, relationship
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from db.database import Model


class TransistorOrm(Model):
    __tablename__ = "transistors"

    id = Column(Integer, primary_key=True)
    name =  Column(String)
    markname = Column(String)
    type_ = Column(ForeignKey('type_tr.id'))
    korpus = Column(String)
    descr = Column(String)
    amount = Column(Integer, default=0)
    path_file = Column(String)
    userid = Column(Integer)

    type_tr = relationship("TypeTransistorOrm", back_populates="transistor")

# class TransistorOrm(Model):
#     __tablename__ = "transistors"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     markname: Mapped[str]
#     # type_: MappedColumn[int, ForeignKey('TypeTransistorOrm')]
#     korpus: Mapped[Optional[str]]
#     descr: Mapped[Optional[str]]
#     amount: Mapped[Optional[str]]
#     path_file: Mapped[Optional[str]]
#     userid: Mapped[Optional[str]]

    # type_tr = relationship("TypeTransistorOrm", back_populates="transistors")



class TypeTransistorOrm(Model):
    __tablename__ = "type_tr"

    id = Column(Integer, primary_key=True)
    type_ = Column(String)

    transistor = relationship("TransistorOrm", back_populates="type_tr")



class KorpusTransistorOrm(Model):
    __tablename__ = "korpus_tr"

    id = Column(Integer, primary_key=True)
    korpus = Column(String)
