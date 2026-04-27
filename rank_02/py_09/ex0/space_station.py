#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    space_station.py                                  :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/25 12:22:19 by maprunty         #+#    #+#              #
#    Updated: 2026/04/27 15:47:58 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""A module for modeling and validating space station data using Pydantic."""

import csv
import json
import sys
from datetime import datetime
from typing import Any, cast

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """A model of space station with attributes and validation rules."""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(max_length=200)

    def __str__(self) -> str:
        """Return a human-readable string of the space station."""
        status = "Operational" if self.is_operational else "Non-operational"
        return (
            f"ID: {self.station_id}\n"
            f"Name: {self.name}\n"
            f"Crew: {self.crew_size} people\n"
            f"Power: {self.power_level}%\n"
            f"Oxygen: {self.oxygen_level}%\n"
            f"Status: {status}"
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SpaceStation":
        """Create a SpaceStation instance from a dictionary."""
        try:
            return cls(**data)
        except ValidationError:
            raise


def defaults() -> list[dict[str, object]]:
    """Provide default test data for space stations."""
    valid = {
        "station_id": "KSP001",
        "name": "Mun or Bust",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": datetime(2015, 4, 27, 16, 20),
        "is_operational": True,
        "notes": "To the Mun!",
    }
    invalid = {
        "station_id": "KSP002",
        "name": "Mun Overload",
        "crew_size": 25,
        "power_level": 75.0,
        "oxygen_level": 80.0,
        "last_maintenance": datetime(2024, 2, 24, 6, 30),
        "is_operational": True,
        "notes": "Woah there Jebediah... too many kerbals spoil the broth.",
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
    """Run Space Station Data Validation."""
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
                station = SpaceStation.from_dict(i)
                print("Valid station created:\n" + str(station), end="\n\n")
            except ValidationError as e:
                print(
                    "Expected validation error:\n" + str(e.errors()[0]["msg"]),
                    end="\n\n",
                )
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
