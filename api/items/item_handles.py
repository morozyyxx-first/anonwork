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
def new_item(item: ItemSchema):
    add_item(item)


@router.get("/get")
def get_items():
    return get_all_items()


@router.delete("/delete")
def remove_item(item_id: int):
    delete_item(item_id)