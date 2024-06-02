from .models import ItemList, Item, get_ai_data
import hashlib
from fastapi import FastAPI, UploadFile

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .word.word import generate_doc
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.mount("/static", StaticFiles(directory="./server/static"), name="static")

# gets file in .edf format and returns list of episodes with their types
@app.post("/")
async def read_rec(file: UploadFile, n: int = 10):
    contents = await file.read()
    
    hex_dig = hashlib.md5(contents).hexdigest()
    with open(f"{hex_dig}.edf", "wb") as f:
        f.write(contents)
    
    ai_data, sec = get_ai_data(f"{hex_dig}.edf")
    generate_doc(sec, ai_data, f"server/static/{hex_dig}.docx")
    resp = ItemList(items=ai_data, word_url=f"static/{hex_dig}.docx", dead=False, duration=sec)
    return resp
    

def generate_random_array(n: int) :
    types = ["апное","гипопноэ", "центральное апноэ", "обструктивное апноэ", "???", "храп"]
    import random
    
    data = ItemList(items=[], word_url="static/example.docx", dead=random.choice([True, False]))
    for i in range(n):
        data.items.append(Item(episode=i, start=random.randint(0, 100), end=random.randint(0, 100), duration=random.randint(0, 100), type=random.choice(types)))
    return data
