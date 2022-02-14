
import json

def item_generator(json_input, lookup_key):
    if type(json_input) is dict and json_input:
        for key in json_input:
            if key == lookup_key:
                return json_input[key]
            item_generator(json_input[key], lookup_key)

    elif type(json_input) is list and json_input:
        for item in json_input:
            item_generator(item, lookup_key)

def find(file, key):

    try:
        with open(file, "r") as f:
            data = json.load(f)

            items = []

            for d in data:
                item = item_generator(d, key)

                if type(item) is str:
                    if item not in items:
                        items.append(item)
                elif type(item) is list:
                    for i in item:
                        if type(i) is str:
                            if i not in items:
                                items.append(i)
            return items

    except Exception as e:
        print(e)


print(find("1.json", "password"))
