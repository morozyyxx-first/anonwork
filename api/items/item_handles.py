from fastapi import APIRouter

from api.items.item_schema import ItemSchema
from api.db.db_add_item import add_item
from api.db.db_get_items import get_all_items
from api.db.db_delete_item import delete_item

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@router.post("/add")
async def new_item(item: ItemSchema):
    add_item(item)


@router.get("/get")
async def get_items():
    return get_all_items()


@router.delete("/delete")
async def remove_item(item_id: int):
    delete_item(item_id)