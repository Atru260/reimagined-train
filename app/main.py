from fastapi import FastAPI
from pydantic import BaseModel
print("running")
app = FastAPI()

# Dummy
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

#TODO: add more info
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/analyze/{text}")
def analyze(text: str):
    return {"metadata": {},
            "summary" : {},
            "entities": {},
            "temporal_information": {},
            "observations": {},
            "uncertainty": {},
            "raw_text": text
            }


# Toy example from the official tutorial
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}