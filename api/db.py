from tinydb import TinyDB, Query
from pydantic import BaseModel

db = TinyDB('db.json')


class ChipEntry(BaseModel):
    chipId: str
    phoneNumbers: list[str]

    @classmethod
    def from_document(cls, doc: dict) -> "ChipEntry":
        return cls(chipId=doc["chipId"], phoneNumbers=doc["phoneNumbers"])


def getAllChips() -> list[ChipEntry]:
    return [ChipEntry.from_document(doc) for doc in db.all()]


def addChip(newChip: ChipEntry) -> ChipEntry:
    db.insert({'chipId': newChip.chipId, 'phoneNumbers': newChip.phoneNumbers})
    return newChip


def updateChip(chipId: str, newChipEntry: list[str]) -> ChipEntry:
    Chip = Query()
    updatedChip = {'chipId': newChipEntry.chipId,
                   'phoneNumbers': newChipEntry.phoneNumbers}
    db.update(updateChip, Chip.chipId == chipId)
    return updatedChip


def removeChip(chipId: str) -> int:
    Chip = Query()
    return db.remove(Chip.chipId == chipId)
