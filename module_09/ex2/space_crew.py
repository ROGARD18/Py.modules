from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List, Self
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_safety_rules(self) -> Self:
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        check_rank = False
        for member in self.crew:
            if member.rank == Rank.commander or member.rank == Rank.captain:
                check_rank = True
                break
        if not check_rank:
            raise ValueError("Mission must have at least one Commander or"
                             " Captain")

        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")

        if self.duration_days > 365:
            exp_count = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    exp_count += 1

            if exp_count < len(self.crew) / 2:
                raise ValueError("Long missions need 50% experienced"
                                 " crew (5+ years)")
        return self

    def display_infos(self):
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: ${self.budget_millions}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew members:")
        for member in self.crew:
            print(f"- {member.name} ({member.rank.value}) -"
                  f" {member.specialization}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=============================")
    try:
        my_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-06-01",
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="c01",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20
                    ),
                CrewMember(
                    member_id="c02",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=30,
                    specialization="Navigation",
                    years_experience=8
                    ),
                CrewMember(
                    member_id="c03",
                    name="Alice Johson",
                    rank=Rank.officer,
                    age=30,
                    specialization="Engineering",
                    years_experience=8
                    )
            ]
        )
        print("Valid mission created:")
        my_mission.display_infos()
    except ValidationError as e:
        print(e.errors()[0]['msg'])

    print("\n=========================================")
    print("Expected validation error:")
    try:
        my_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-06-01",
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="c01",
                    name="Sarah Connor",
                    rank=Rank.cadet,
                    age=45,
                    specialization="Command",
                    years_experience=20
                    ),
                CrewMember(
                    member_id="c02",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=30,
                    specialization="Navigation",
                    years_experience=8
                    ),
                CrewMember(
                    member_id="c03",
                    name="Alice Johson",
                    rank=Rank.officer,
                    age=30,
                    specialization="Navigation",
                    years_experience=8
                    )
            ]
        )
        print("Valid mission created:")
        my_mission.display_infos()
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
