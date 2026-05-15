from pydantic import BaseModel
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import Base


class BaseRepository:
    model: type[Base]
    schema: type[BaseModel]
    session: AsyncSession

    def __init__(self, session):
        self.session = session

    async def get_one_or_none(self, **kwargs):
        query = select(self.model).filter_by(**kwargs)
        executed_query = await self.session.execute(query)
        result = executed_query.scalars().one_or_none()

        if result is None:
            return None

        return self.schema.model_validate(result, from_attributes=True)

    async def get_one(self, **kwargs):
        query = select(self.model).filter_by(**kwargs)
        result = await self.session.execute(query)

        return self.schema.model_validate(result, from_attributes=True)

    async def get_all(self, *args, **kwargs):
        query = select(self.model).filter(*args).filter_by(**kwargs)
        result = await self.session.execute(query)

        return [
            self.schema.model_validate(model, from_attributes=True)
            for model in result.scalars().all()
        ]

    async def create(self, data: BaseModel):
        insert_stmt = insert(self.model).values(**data.model_dump())
        await self.session.execute(insert_stmt)
