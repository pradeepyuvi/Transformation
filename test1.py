a = {
    "duncan_long": {
        "id": "drekaner",
        "name": "Duncan Long",
        "favorite_color": "Blue"
    },
    "kelsea_head": {
        "id": "wagshark",
        "name": "Kelsea Head",
        "favorite_color": "Ping"
    },
    "phoenix_knox": {
        "id": "jikininer",
        "name": "Phoenix Knox",
        "favorite_color": "Green"
    },
    "adina_norton": {
        "name": "Adina Norton",
        "favorite_color": "Red"
    }
}

for key, value in a.items():
    value.pop('id', None)

print(a)