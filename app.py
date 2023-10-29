import sys
import clipboard
import json

FILE_NAME = "clipboard.json"


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


def handle_load():
    key = input("Enter a key to load: ")
    if key in data:
        clipboard.copy(data[key])
        print("Copied to clipboard.")
    else:
        print("Nothing found to load for: ", key)


def handle_save():
    key = input("Enter a key to save: ")
    data[key] = clipboard.paste()
    save_items(FILE_NAME, data)
    print('Item saved: ', data[key])


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = read_json(FILE_NAME)

    if command == "save":
        handle_save()
    elif command == "delete":
        handle_delete()
    elif command == "load":
        handle_load()
    elif command == "list":
        print("\n", "There are", len(data), "saved items: \n\n", data)
    else:
        print("No such command. Type one of these commands: 'save', 'load', 'delete' or 'list'.")

else:
    print("Please pass exactly 1 command.")
