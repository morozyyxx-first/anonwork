from sqlalchemy import select

from .orms import ItemsORM
from .db_engine import get_session

async def get_all_items():
    async with await get_session() as session:
        query = select(ItemsORM)
        items = await session.execute(query)
        return items.scalars().all()