#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    alien_contact.py                                  :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/25 21:34:35 by maprunty         #+#    #+#              #
#    Updated: 2026/04/27 16:46:48 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""A module for modeling and validating alien contact data using Pydantic."""

import csv
import json
import sys
from datetime import datetime
from enum import Enum
from typing import Any, cast

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(Enum):
    """Types of alien contact."""

    VISUAL = "visual"
    RADIO = "radio"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """A model of an alien contact with attributes and validation rules."""

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500)
    is_verified: bool = Field(default=False)

    def __str__(self) -> str:
        """Return a human-readable string of the alien contact."""
        return (
            f"ID: {self.contact_id}\n"
            f"Location: {self.location}\n"
            f"Type: {self.contact_type.value}\n"
            f"Signal: {self.signal_strength}/10\n"
            f"Duration: {self.duration_minutes} minutes\n"
            f"Witnesses: {self.witness_count}\n"
            f"Message: {self.message_received or 'None'}"
        )

    @model_validator(mode="after")
    def validate_message(self) -> "AlienContact":
        """Validate rules for the alien contact."""
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contacts must be verified")
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contacts must have at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must have a message received")
        if not self.is_verified:
            self.is_verified = True
        return self

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "AlienContact":
        """Create an AlienContact instance from a dictionary."""
        return cls(**data)


def defaults() -> list[dict[str, object]]:
    """Provide default test data for alien contacts."""
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


def json_load() -> list[dict[str, Any]]:
    """Load JSON data from a file or stdin and return list of dicts."""
    try:
        with (
            open(sys.argv[2], encoding="utf-8")
            if len(sys.argv) > 2
            else sys.stdin as f
        ):
            return cast(list[dict[str, Any]], json.load(f))
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return []


def csv_load() -> list[dict[str, Any]]:
    """Load CSV data from a file or stdin and return list of dicts."""
    try:
        with (
            open(sys.argv[2], encoding="utf-8")
            if len(sys.argv) > 2
            else sys.stdin as f
        ):
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception as e:
        print(f"CSV load error: {e}")
        return []


def main() -> None:
    """Run Alien Contact Log Validation."""
    print(f"{(main.__doc__[4:-1] if main.__doc__ else ' ')}")
    try:
        if len(sys.argv) > 1:
            mode = sys.argv[1].lower()
            if mode == "json":
                data = json_load()
            elif mode == "csv":
                data = csv_load()
        else:
            data = defaults()
        for i in data:
            print("========================================")
            try:
                contact = AlienContact.from_dict(i)
                print("Valid station created:\n" + str(contact), end="\n\n")
            except ValidationError as e:
                print(
                    "Expected validation error:\n" + str(e.errors()[0]["msg"]),
                    end="\n\n",
                )
    except Exception as e:
        print(f"Error creating AlienContact: {e}")


if __name__ == "__main__":
    main()
