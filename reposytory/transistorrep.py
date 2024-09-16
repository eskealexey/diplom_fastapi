from sqlalchemy import select

from db.database import new_session
from db.transistotr_orm import TransistorOrm, TypeTransistorOrm
from schemas.transisnors import STransistorAdd, STypeTransistorAdd


class TransistorRepository:
    @classmethod
    async def add_one(cls, data: STransistorAdd) -> int:
        async with new_session() as session:
            transistor_dict = data.model_dump()
            transistor = TransistorOrm(**transistor_dict)
            session.add(transistor)
            await session.flush()
            await session.commit()
            return transistor.id


    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TransistorOrm)
            result = await session.execute(query)
            transistor_models = result.scalars().all()
            return transistor_models

    @classmethod
    async def add_type_one(cls, data: STypeTransistorAdd) -> int:
        async with new_session() as session:
            transistor_dict = data.model_dump()
            transistor = TypeTransistorOrm(**transistor_dict)
            session.add(transistor)
            await session.flush()
            await session.commit()
            return transistor.id


    @classmethod
    async def find_type_all(cls):
        async with new_session as session:
            query = select(TypeTransistorOrm)
            result = await session.execute(query)
            type_models = result.scalars().all()
            return type_models
