from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

import json

class Quote(BaseModel):
    id: int
    name: str
    quote: str
    date: str | None = None


app = FastAPI()

file = open("quotes.json", encoding="utf8")

data = json.load(file)

#quotes = []


#Get Info
@app.get("/")
async def root():
    return {"message": "Hello there"}

#Get all quotes
@app.get("/quotes")
async def get_quotes():
    return {"blablabla": data}

#Get one quote
@app.get("/quotes/{quote_id}")
async def get_quotes(quote_id: int):
    for quote in data:
        if quote.id == quote_id:
            return {"quote": data}
    return {"message": "Quote was not found"}

#Create Info
@app.post("/quotes")
async def post_quotes(quote: Quote):
    data.append(quote)
    return {"quotes": "Information was created"}