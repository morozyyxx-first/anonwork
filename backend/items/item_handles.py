from fastapi import APIRouter

from .item_schema import ItemSchema
from db.db_add_item import add_item
from db.db_get_items import get_all_items
from db.db_delete_item import delete_item

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@router.post("/add")
async def new_item(item: ItemSchema):
    await add_item(item)


@router.get("/get")
async def get_items():
    return await get_all_items()


@router.delete("/delete")
async def remove_item(item_id: int):
    await delete_item(item_id)