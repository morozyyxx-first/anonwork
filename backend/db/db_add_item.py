from items.item_schema import ItemSchema
from .orms import ItemsORM
from .db_engine import get_session

async def add_item(item: ItemSchema):
    async with await get_session() as session:
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
        await session.commit()