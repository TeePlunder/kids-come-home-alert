from tinydb import TinyDB, Query
from pydantic import BaseModel

db = TinyDB('db.json')


class ChipEntry(BaseModel):
    chipId: str
    phoneNumbers: list[str]


def getAllChips() -> list[ChipEntry]:
    return db.all()


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
