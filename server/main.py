from typing import Union, List
import hashlib
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
app = FastAPI()


class Item(BaseModel):
    episode: int
    start: int
    end: int
    duration: int
    type: str

# gets file in .edf format and returns list of episodes with their types
@app.post("/")
async def read_rec(file: UploadFile):
    contents = await file.read()
    hash_data = hashlib.md5(contents).hexdigest()
    hex_dig = hashlib.md5(contents).hexdigest()
    with open(f"{hex_dig}.edf", "wb") as f:
        f.write(contents)
    
    return [
        Item(episode=1, start=0, end=10, duration=10, type="Апноэ"),
        Item(episode=2, start=40, end=50, duration=10, type="Гиперопноэ"),
    ]
    


