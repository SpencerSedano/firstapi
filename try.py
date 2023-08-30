import json

with open("quotes.json", encoding="utf8") as s:
    data = json.load(s)
    quotes = data["quotes"]

for quote in quotes:
    id_number = quote["id"]
    print("ID:", id_number)


#Convert a list to dictionary
def convert(lst):
    res_dict = {}
    for i in range(0,len(lst),2):
        res_dict[lst[i]] = lst[i+1]
    return res_dict

quotes_list = ["id", 1, "name", "Spencer"]
print(convert(quotes_list))

alist = []
var = "Spencer"
for i in var:
    alist = i

quote_dict = {}


print(quote_dict)
