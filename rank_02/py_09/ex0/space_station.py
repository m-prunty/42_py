#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    space_station.py                                  :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/25 12:22:19 by maprunty         #+#    #+#              #
#    Updated: 2026/04/25 21:33:24 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import csv
import json
import sys
from datetime import datetime
from io import StringIO

from pydantic import BaseModel, Field, ValidationError

"""
crew_size,is_operational,last_maintenance,name,notes,oxygen_level,power_level,station_id
6,True,2023-07-11T00:00:00,Titan Mining Outpost,,95.5,76.4,LGW125
3,False,2023-08-24T00:00:00,Deep Space Observatory,System diagnostics required,88.1,70.8,QCH189
11,True,2023-10-21T00:00:00,Europa Research Station,,91.4,82.0,ISS674
"""


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(max_length=200)

    def __str__(self) -> str:
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
    def from_csv(cls, csv_string: str) -> "SpaceStation":
        print(csv_string)
        f = StringIO(csv_string)
        reader = csv.DictReader(f)
        rows = list(reader)
        print(rows)
        try:
            return cls(**data)
        except (StopIteration, ValidationError):
            raise

    @classmethod
    def from_json(cls, json_string: str) -> "SpaceStation":
        data = json.loads(json_string)
        try:
            return cls(**data)
        except ValidationError:
            raise

    @classmethod
    def from_dict(cls, data: dict) -> "SpaceStation":
        try:
            return cls(**data)
        except ValidationError:
            raise


def defaults() -> list[dict[str, object]]:
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


def validator(s: dict | str) -> SpaceStation:
    print("========================================")
    if isinstance(s, str):
        try:
            if sys.argv[1] == "csv":
                st = SpaceStation.from_csv(s)
            st = SpaceStation.from_json(s)
        except (ValidationError, ValueError):
            raise
    else:
        try:
            st = SpaceStation.from_dict(s)
        except (ValidationError, ValueError):
            raise
    return st


def json_load() -> object:
    try:
        if len(sys.argv) > 2:
            return json.load(sys.argv[2])
        return json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return []


def csv_load() -> StringIO:
    try:
        if len(sys.argv) > 2:
            return StringIO(sys.argv[2])
        return StringIO(sys.stdin.read())
    except Exception as e:
        print(f"CSV load error: {e}")
        return StringIO("")


def main() -> None:
    print("Space Station Data Validation")
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        if mode == "json":
            data = json_load()
        elif mode == "csv":
            data = csv_load()
        print(data)
    else:
        data = defaults()
    for i in data:
        try:
            station = validator(i)
            print("Valid station created:\n" + str(station), end="\n\n")
        except ValidationError as e:
            print(
                "Expected validation error:\n" + str(e.errors()[0]["msg"]),
                end="\n\n",
            )


if __name__ == "__main__":
    main()
