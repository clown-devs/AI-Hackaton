from pydantic import BaseModel
from typing import List
class Item(BaseModel):
    episode: int
    start: int
    end: int
    duration: int
    type: str

class ItemList(BaseModel):
    items: List[Item]
    word_url: str = None