from api.db import ChipEntry
from api.db import cursor


def getAllChips() -> list[ChipEntry]:
    return [ChipEntry.from_document(doc) for doc in db.all()]


def addChip(newChip: ChipEntry) -> ChipEntry:
    db.insert({"chipId": newChip.chipId, "phoneNumbers": newChip.phoneNumbers})
    return newChip


def removeChip(chipId: str) -> List[int]:
    Chip = Query()
    return db.remove(Chip.chipId == chipId)
