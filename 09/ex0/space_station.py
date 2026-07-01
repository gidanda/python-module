from datetime import datetime
from pydantic import BaseModel, Field, ValidationError

class SpaceStation(BaseModel):
    station_id: str = Field(..., max_length=10, min_length=3)
    name: str = Field(..., max_length=50, min_length=1)
    crew_size: int = Field(le=20, ge=1)
    power_level: float  = Field(le=100.0, ge=0.0)
    oxygen_level: float = Field(le=100.0, ge=0.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-05-22T10:00:00",
    )

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")

    if station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Not operational")

    print()
    print("========================================")

    try:
        SpaceStation(
            station_id="BAD001",
            name="Invalid Station",
            crew_size=30,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-05-22T10:00:00",
        )
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]["msg"])

if __name__ == "__main__":
    main()
