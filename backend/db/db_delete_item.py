from sqlalchemy import delete
from .orms import ItemsORM
from .db_engine import get_session

async def delete_item(item_id: int):
    async with await get_session() as session:
        query = delete(ItemsORM).filter_by(id=item_id)
        await session.execute(query)
        await session.commit()
