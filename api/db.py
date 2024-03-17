from typing import List
from pydantic import BaseModel
from sqlite3 import connect


# define the database

connection = connect("chip.db")

cursor = connection.cursor()


# structure of the database


# class of table


class ChipEntry(BaseModel):
    chipId: str
    phoneNumbers: list[str]

    @classmethod
    def from_document(cls, doc: dict) -> "ChipEntry":
        return cls(chipId=doc["chipId"], phoneNumbers=doc["phoneNumbers"])
