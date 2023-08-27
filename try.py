import json
s = open("quotes.json", encoding="utf8")
print(s)

data = json.load(s)

for i in data["quotes"]:
    print(i)

