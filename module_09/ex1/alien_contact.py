from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional, Self
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_rules(self) -> Self:

        if not (self.contact_id.startswith("AC")):
            raise ValueError("Contact ID must start with 'AC'")

        if ((self.contact_type == ContactType.physical)
                and not self.is_verified):
            raise ValueError("Physical contact reports must be verified")

        if ((self.contact_type == ContactType.telepathic)
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires at least 3"
                             " witnesses")

        if (self.signal_strength > 7.0) and not self.message_received:
            raise ValueError("Strong signals (>7.0) should received a message")

        return (self)

    def display_infos(self) -> None:
        print(f"ID: {self.contact_id}")
        print(f"Type: {self.contact_type.value}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}/10")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witness: {self.witness_count}")
        if (self.message_received):
            print(f"{self.message_received}")


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        my_alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-02-23",
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        my_alien.display_infos()
    except ValidationError as e:
        print(e)

    print("\n======================================")
    try:
        my_alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-02-23",
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        my_alien.display_infos()
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
