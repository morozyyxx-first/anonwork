from items.item_schema import ItemSchema
from api.db.orms import ItemsORM
from api.db.db_engine import get_session

def add_item(item: ItemSchema):
    with get_session() as session:
        session.add(
            ItemsORM(
                title=item.title,
                name_of_company=item.name_of_company,
                salary=item.salary,
                location=item.location,
                contacts=item.contacts,
                job_time=item.job_time,
                description=item.description,
                skills=item.skills
            )
        )
        session.commit()