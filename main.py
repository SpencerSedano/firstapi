from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import json

DATABASE_URL = "dbname=quotes_db user=postgres password=230110 host=localhost"

#Creating the BaseModel using pydantic
#This is the structure of my API
class Quote(BaseModel):
    id: int
    name: str
    quote: str
    date: str | None = None

app = FastAPI()

with open("quotes.json", encoding="utf8") as file:
    data = json.load(file)
    quotes_to_insert = data["quotes"]

def insert_quotes():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    for quote in quotes_to_insert:
        # Check if the quote with the same ID exists in the database
        existing_quote_query = f"SELECT id FROM quotes WHERE id = {quote['id']}"
        cursor.execute(existing_quote_query)
        
        if cursor.fetchone():
            # Update the existing row
            update_query = f"UPDATE quotes SET name = '{quote['name']}', quote = '{quote['quote']}', date = '{quote['date']}' WHERE id = {quote['id']}"
            cursor.execute(update_query)
        else:
            # Insert a new row
            insert_query = f"INSERT INTO quotes (id, name, quote, date) VALUES ({quote['id']}, '{quote['name']}', '{quote['quote']}', '{quote['date']}')"
            cursor.execute(insert_query)

    conn.commit()
    cursor.close()
    conn.close()

# Call the function to insert quotes
insert_quotes()

# Get Info
@app.get("/")
async def root():
    return {"message": "Hello there, Welcome to this Couple API"}

# Get all quotes
@app.get("/quotes")
async def get_quotes():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    query = "SELECT * FROM quotes"
    cursor.execute(query)
    quotes = cursor.fetchall()
    cursor.close()
    conn.close()

    #Convert the list of tuples into a list of dictionaries
    quotes_list = []
    for quote in quotes:
        quote_dict = {
            "id": quote[0],
            "name": quote[1],
            "quote": quote[2],
            "date": quote[3]
        }
        quotes_list.append(quote_dict)
    return quotes_list

# Get one quote
@app.get("/quotes/{quote_id}")
async def get_quote(quote_id: int):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    query = f"SELECT * FROM quotes WHERE id = {quote_id}"
    cursor.execute(query)
    quote = cursor.fetchone()
    cursor.close()
    conn.close()

    def convert(lst):
        res_dict = {}
        for i in range(0,len(lst),2):
            res_dict[lst[i]] = lst[i+1]
        return res_dict
    if quote:
        return convert(quote)
    return {"message": "Quote was not found"}

# Create Info
@app.post("/quotes")
async def post_quotes(quote: Quote):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    query = f"INSERT INTO quotes (id, name, quote, date) VALUES ({quote.id}, '{quote.name}', '{quote.quote}', '{quote.date}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Information was created"}
