import sys
import clipboard
import utils

FILE_NAME = "clipboard.json"
COMMANDS = {
    "save": "save",
    "delete": "delete",
    "load": "load",
    "list": "list",
}


def handle_delete():
    key = input("Enter a key for deletion: ")
    if utils.delete_item(FILE_NAME, key):
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
    utils.save_items(FILE_NAME, data)
    print('Item saved: ', data[key])


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = utils.read_json(FILE_NAME)

    if command == COMMANDS["save"]:
        handle_save()
    elif command == COMMANDS["delete"]:
        handle_delete()
    elif command == COMMANDS["load"]:
        handle_load()
    elif command == COMMANDS["list"]:
        print("\n", "There are", len(data), "saved items: \n\n", data)
    else:
        print("No such command. Type one of these commands: 'save', 'load', 'delete' or 'list'.")

else:
    print("Please pass exactly 1 command.")
