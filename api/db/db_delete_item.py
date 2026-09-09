from sqlalchemy import delete
from .orms import ItemsORM
from .db_engine import get_session

def delete_item(item_id: int):
    with get_session() as session:
        query = delete(ItemsORM).filter_by(id=item_id)
        session.execute(query)
        session.commit()
