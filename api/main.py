from pydantic import BaseModel
from fastapi import FastAPI, status

from api.db import ChipEntry, getAllChips, addChip


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
    """
    ## Perform a Health Check
    Endpoint to perform a healthcheck on. This endpoint can primarily be used Docker
    to ensure a robust container orchestration and management is in place. Other
    services which rely on proper functioning of the API service will not deploy if this
    endpoint returns any other HTTP status code except 200 (OK).
    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
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
    response_model=ChipEntry
)
def add_chip(newChip: ChipEntry) -> ChipEntry:
    return addChip(newChip)
