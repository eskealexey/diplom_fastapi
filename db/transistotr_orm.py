from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from db.database import Model


class TransistorOrm(Model):
    __tablename__ = "transistors"

    id = Column(Integer, primary_key=True)
    name =  Column(String)
    markname = Column(String)
    type_ = Column(ForeignKey('type_tr.id'))
    korpus = Column(ForeignKey('korpus_tr.id'))
    descr = Column(String)
    amount = Column(Integer, default=0)
    path_file = Column(String)
    userid = Column(ForeignKey('users.id'))

    type_tr = relationship("TypeTransistorOrm", back_populates="transistor")
    korpus_tr = relationship("KorpusTransistorOrm", back_populates="transistor")
    users = relationship("TaskOrm", back_populates="transistor")


class TypeTransistorOrm(Model):
    __tablename__ = "type_tr"

    id = Column(Integer, primary_key=True)
    type_ = Column(String)

    transistor = relationship("TransistorOrm", back_populates="type_tr")


class KorpusTransistorOrm(Model):
    __tablename__ = "korpus_tr"

    id = Column(Integer, primary_key=True)
    korpus = Column(String)
    transistor = relationship("TransistorOrm", back_populates="korpus_tr")