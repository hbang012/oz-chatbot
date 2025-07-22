from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel


router = APIRouter()


# 타입잡기
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


# 경로, 쿼리 파라미터 받기
@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# put 수정
@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
