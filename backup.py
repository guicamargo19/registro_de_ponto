import json
import os

# Absolute path of the backup JSON file (save application state)
JSON_TEMP = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database',
                                         'jsontemp.json'))

# dump the register at the backup JSON file


def dumpJson(object: list[str]):
    with open(JSON_TEMP, 'w', encoding="utf8") as file:
        json.dump(object, file, ensure_ascii=False, indent=2)

# load the registers from the backup JSON file


def loadJson():
    with open(JSON_TEMP, 'r', encoding='utf8') as file:
        lista = json.load(file)
        return lista

# clean the backup JSON file (reset)


def clearJson():
    with open(JSON_TEMP, 'w', encoding="utf8") as file:
        json.dump([], file, ensure_ascii=False, indent=2)
