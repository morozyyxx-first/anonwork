from sqlalchemy import select

from api.db.orms import ItemsORM
from api.db.db_engine import get_session

def get_all_items():
    with get_session() as session:
        query = select(ItemsORM)
        items = session.execute(query)
        return items.scalars().all()