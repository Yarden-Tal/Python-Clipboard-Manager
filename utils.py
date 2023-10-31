import json
import clipboard
from constants import FILE_NAME


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


def handle_delete():
    key = input("Enter a key for deletion: ")
    if delete_item(FILE_NAME, key):
        print("Key deleted: ", key)
    else:
        print("Nothing found for deletion: ", key)


def handle_load(data):
    key = input("Enter a key to load: ")
    if key in data:
        clipboard.copy(data[key])
        print("Copied to clipboard.")
    else:
        print("Nothing found to load for: ", key)


def handle_save(data):
    key = input("Enter a key to save: ")
    data[key] = clipboard.paste()
    save_items(FILE_NAME, data)
    print('Item saved: ', data[key])
