import json

with open("quotes.json", encoding="utf8") as s:
    data = json.load(s)
    quotes = data["quotes"]

for quote in quotes:
    id_number = quote["id"]
    print("ID:", id_number)
