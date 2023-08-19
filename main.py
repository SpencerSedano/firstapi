from fastapi import FastAPI
from pydantic import BaseModel

class Quote(BaseModel):
    id: int
    name: str
    quote: str
    date: str | None = None


app = FastAPI()


quotes = []


@app.get("/")
async def root():
    return {"message": "Hello there"}

@app.post("/quotes")
async def post_quotes(quote: Quote):
    quotes.append(quote)
    return {"quotes": "Information was created"}

@app.get("/quotes")
async def get_quotes():
    return {"quotes": quotes}