import sys
from constants import COMMANDS, FILE_NAME
import utils


def main():
    isExactlyTwoCommands = len(sys.argv) == 2
    if isExactlyTwoCommands:
        command = sys.argv[1]
        data = utils.read_json(FILE_NAME)

        if command == COMMANDS["save"]:
            utils.handle_save(data)
        elif command == COMMANDS["delete"]:
            utils.handle_delete()
        elif command == COMMANDS["load"]:
            utils.handle_load(data)
        elif command == COMMANDS["list"]:
            print("\n", "There are", len(data), "saved items: \n\n", data)
        else:
            print(
                "No such command. Type one of these commands: 'save', 'load', 'delete' or 'list'.")

    else:
        print("Please pass exactly 1 command.")


main()
