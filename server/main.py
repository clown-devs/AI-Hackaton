from typing import Union, List
import hashlib
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    episode: int
    start: int
    end: int
    duration: int
    type: str

# gets file in .edf format and returns list of episodes with their types
@app.post("/")
async def read_rec(file: UploadFile, n: int = 10):
    contents = await file.read()
    hash_data = hashlib.md5(contents).hexdigest()
    hex_dig = hashlib.md5(contents).hexdigest()
    with open(f"{hex_dig}.edf", "wb") as f:
        f.write(contents)
    
    return generate_random_array(n)
    

def generate_random_array(n: int) -> List[Item]:
    import random
    arr = []
    for i in range(n):
        arr.append(Item(episode=i, start=random.randint(0, 100), end=random.randint(0, 100), duration=random.randint(0, 100), type="random"))
    return arr
