from typing_extensions import List
from pydantic import BaseModel
from fastapi import FastAPI, status

from api.db import ChipEntry
from api.handler import addChip, getAllChips, removeChip

controllerName = "chips"
app = FastAPI()


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: str = "OK"


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    return HealthCheck(status="OK")


@app.get(
    f"/{controllerName}",
    summary="Get all chips in db",
    response_description="Returns a list of chips",
    status_code=status.HTTP_200_OK,
    response_model=list[ChipEntry],
)
def get_chips() -> list[ChipEntry]:
    return getAllChips()


@app.post(
    f"/{controllerName}",
    summary="Add a new chip",
    response_description="Returns the added chip",
    response_model=ChipEntry,
)
def add_chip(newChip: ChipEntry) -> ChipEntry:
    return addChip(newChip)


@app.delete(
    f"/{controllerName}/{{chipId}}",
    summary="Remove a chip",
    response_description="Returns the number of chips removed",
    response_model=List[int],
)
def remove_chip(chipId: str) -> List[int]:
    return removeChip(chipId)
