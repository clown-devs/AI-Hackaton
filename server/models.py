from pydantic import BaseModel
from typing import List
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ai.ai as ai
import parser.parser as parser
class Item(BaseModel):
    episode: int
    start: int
    end: int
    duration: int
    type: str
    
class ItemList(BaseModel):
    items: List[Item]
    duration: int
    word_url: str = None
    dead: bool


# returns converted data and seconds
def get_ai_data(file_path: str) -> List[Item]:
    data, edf = parser.parse_file(file_path)
    res, sec = ai.predict_result(data, "ai/my_model.keras")
    return converter(res, sec)

def converter(data_from_model, sec) -> List[Item]:
    items = []
    for i in range(len(data_from_model)):
        start = data_from_model[i][0]
        end = data_from_model[i][1]
        duration = end - start + 1
        items.append(Item(episode=i, start=start, end=end, duration=duration, type="???"))
    return items, sec