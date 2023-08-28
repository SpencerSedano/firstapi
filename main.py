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

#file = open("quotes.json", encoding="utf8")

#data = json.load(file)

with open("quotes.json", encoding="utf8") as file:
    data = json.load(file)
    quotes = data["quotes"]


#quotes = []


#Get Info
@app.get("/")
async def root():
    return {"message": "Hello there"}

#Get all quotes
@app.get("/quotes")
async def get_quotes():
    return quotes

#Get one quote
@app.get("/quotes/{quote_id}")
async def get_quote(quote_id: int):
    #return data["id"]
    for quote in quotes:
        if quote["id"] == quote_id:
            return quote
    return {"message": "Quote was not found"}

#Create Info
@app.post("/quotes")
async def post_quotes(quote: Quote):
    data.append(quote)
    return {"quotes": "Information was created"}