import os
from dataclasses import asdict, dataclass

from tinydb import TinyDB

# Register dataclass use to manipulate the data for the database


@dataclass
class Register:
    register: list

    def asDict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return Register(**data)

    @classmethod
    def from_list(cls, data):
        for item in data:
            return dict(item)


# The database JSON file's path

DB_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database',
                                       'jsondatabase.json'))

# Database

db = TinyDB(DB_FILE, indent=4, encoding='utf8', ensure_ascii=False)


# Register the data in the database JSON file


def dbRegister(index1: int, newRegister, dayRegister, check=False):
    dbReturn = db.get(doc_id=index1)
    if dbReturn is not None:
        valor = Register.from_dict(dbReturn)
        dict_valor = Register.asDict(valor)
        qtde = len(dict_valor["register"])
        if check is True:
            dict_valor["register"].pop(-1)
            if qtde >= 30:
                dict_valor["register"].pop(0)
            qtde = len(dict_valor["register"])
            dayRegister.register.clear()
            db.truncate()
            i = 0
            while i < qtde:
                for j in dict_valor["register"]:
                    dayRegister.register.append(j)
                    i += 1
            dayRegister.register.append(newRegister)
            index1 = db.insert(dayRegister.asDict())
            return index1
        else:
            dayRegister.register.clear()
            db.truncate()
            i = 0
            while i < qtde:
                for j in dict_valor["register"]:
                    dayRegister.register.append(j)
                    i += 1
            dayRegister.register.append(newRegister)
            index1 = db.insert(dayRegister.asDict())
            return index1
    else:
        index1 = db.insert(dayRegister.asDict())
        return index1


# Get the data from de database JSON file


def getValorFromDb(index1: int):
    db_return = db.get(doc_id=index1)

    if db_return is not None:
        valor = Register.from_dict(db_return)
        dict_valor = Register.asDict(valor)
        qtde = len(dict_valor["register"])
        i = 0
        lista = []
        while i < qtde:
            for j in dict_valor["register"]:
                i += 1
                lista.append(j)
            return lista
