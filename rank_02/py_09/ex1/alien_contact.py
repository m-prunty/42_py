#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    alien_contact.py                                  :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/25 21:34:35 by maprunty         #+#    #+#              #
#    Updated: 2026/04/25 23:05:11 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class ContactType(Enum):
    VISUAL = "visual"
    RADIO = "radio"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(le=500)
    is_verified: bool = Field(default=False)

    def __str__(self) -> str:
        verified_status = "Verified" if self.is_verified else "Unverified"
        return (
            f"Contact ID: {self.contact_id}\n"
            f"Timestamp: {self.timestamp.isoformat()}\n"
            f"Location: {self.location}\n"
            f"Type: {self.contact_type.value}\n"
            f"Signal Strength: {self.signal_strength}\n"
            f"Duration: {self.duration_minutes} minutes\n"
            f"Witnesses: {self.witness_count}\n"
            f"Message: {self.message_received or 'None'}\n"
            f"Status: {verified_status}"
        )

    @model_validator(mode="after")
    def validate_message(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must have a message received")
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contacts must have at least 3 witnesses"
            )
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contacts must be verified")
        return self

    @classmethod
    def from_dict(cls, data: dict) -> "AlienContact":
        return cls(**data)


def default() -> list[dict[str, object]]:
    valid = {
        "contact_id": "AC_2024_001",
        "timestamp": datetime.now(),
        "location": "Area 51, Nevada",
        "contact_type": ContactType.RADIO,
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": True,
    }
    invalid = {
        "contact_id": "AC_2026_051",
        "timestamp": datetime.now(),
        "location": "Area 51, Nevada",
        "contact_type": ContactType.TELEPATHIC,
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 2,
        "message_received": "",
        "is_verified": True,
    }
    return [valid, invalid]


def main() -> None:
    try:
        contact = AlienContact.from_dict(contact_data)
        print(contact)
    except Exception as e:
        print(f"Error creating AlienContact: {e}")


if __name__ == "__main__":
    main()
