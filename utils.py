import json


def save_items(path, content):
    with open(path, "w") as file:
        json.dump(content, file)


def delete_item(path, item):
    data = read_json(path)
    if item in data:
        del data[item]
        save_items(path, data)
        return True
    else:
        return False


def read_json(path):
    try:
        with open(path, "r") as file:
            data = json.load(file)
            return data
    except:
        return {}
