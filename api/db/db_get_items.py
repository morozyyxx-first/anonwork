from sqlalchemy import select

from .orms import ItemsORM
from .db_engine import get_session

def get_all_items():
    with get_session() as session:
        query = select(ItemsORM)
        items = session.execute(query)
        return items.scalars().all()