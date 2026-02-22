from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)

    def display_infos(self) -> None:
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level}%")
        print(f"Oxygen: {self.oxygen_level}%")
        status = "Operational" if self.is_operational else "Not operational"
        print(f"Status: {status}")


def main() -> None:
    print("Space Station Data Validation")
    print("===========================================")
    try:
        my_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-02-21"
        )
        print("Valid station created:")
        my_station.display_infos()
    except ValidationError as e:
        print("Unexpected error :", e)

    print("\n===========================================")
    try:
        my_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-02-21"
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
