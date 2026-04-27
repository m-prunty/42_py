#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    space_crew.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/25 23:05:36 by maprunty         #+#    #+#              #
#    Updated: 2026/04/27 20:10:39 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Modeling and validating space mission crew data using Pydantic."""

import csv
import json
import sys
from datetime import datetime
from enum import Enum
from typing import Any, cast

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(Enum):
    """Ranks of space crew members."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """A model of a space crew member with attributes and validation rules."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=8, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)

    def __str__(self) -> str:
        """Return a human-readable string of the crew member."""
        active_status = "Active" if self.is_active else "Inactive"
        return (
            f"Member ID: {self.member_id}\n"
            f"Name: {self.name}\n"
            f"Rank: {self.rank.value}\n"
            f"Age: {self.age}\n"
            f"Specialization: {self.specialization}\n"
            f"Experience: {self.years_experience} years\n"
            f"Status: {active_status}"
        )

    def describe(self) -> str:
        """Return a brief description of the crew member."""
        return f"{self.name} ({self.rank.value}) - {self.specialization}"


class SpaceMission(BaseModel):
    """A model of a space mission with attributes and validation rules."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=3, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    def __str__(self) -> str:
        """Return a human-readable string of the space mission."""
        crew_desc = "\n- ".join(member.describe() for member in self.crew)
        return (
            f"Mission: {self.mission_name}\n"
            f"ID: {self.mission_id}\n"
            f"Destination: {self.destination}\n"
            f"Duration: {self.duration_days} days\n"
            f"Budget: ${self.budget_millions}M\n"
            f"Crew size: {len(self.crew)}\n"
            f"Crew members:\n- {crew_desc}\n"
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SpaceMission":
        """Create a SpaceMission instance from a dictionary."""
        return cls.model_validate(data)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        """Validate rules for the space mission."""
        if self.mission_id and not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not [
            m for m in self.crew if m.rank in (Rank.COMMANDER, Rank.CAPTAIN)
        ]:
            raise ValueError(
                "Mission must have at least one commander or captain"
            )
        if self.duration_days > 365 and not (
            len([m.years_experience >= 5 for m in self.crew])
            >= len(self.crew) / 2
        ):
            raise ValueError(
                "Missions >365days need >= half the crew to have 5+ years exp"
            )
        if any(not m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")
        return self


def default_crew() -> list[dict[str, object]]:
    """Provide default test data for space crew members."""
    crew = [
        {
            "member_id": "C001",
            "name": "Sarah Connor",
            "rank": Rank.COMMANDER,
            "age": 35,
            "specialization": "Mission Command",
            "years_experience": 12,
            "is_active": True,
        },
        {
            "member_id": "C002",
            "name": "John Smith",
            "rank": Rank.LIEUTENANT,
            "age": 28,
            "specialization": "Navigation",
            "years_experience": 5,
            "is_active": True,
        },
        {
            "member_id": "C003",
            "name": "Alice Johnson",
            "rank": Rank.OFFICER,
            "age": 30,
            "specialization": "Engineering",
            "years_experience": 7,
            "is_active": True,
        },
    ]
    return crew


def invalid_crew() -> list[dict[str, object]]:
    """Provide invalid test data for space crew members."""
    crew = [
        {
            "member_id": "C004",
            "name": "Bob Brown",
            "rank": Rank.CADET,
            "age": 22,
            "specialization": "Science",
            "years_experience": 1,
            "is_active": True,
        },
        {
            "member_id": "C005",
            "name": "Eve Davis",
            "rank": Rank.OFFICER,
            "age": 27,
            "specialization": "Medical",
            "years_experience": 3,
            "is_active": True,
        },
        {
            "member_id": "C003",
            "name": "Alice Johnson",
            "rank": Rank.OFFICER,
            "age": 30,
            "specialization": "Engineering",
            "years_experience": 7,
            "is_active": True,
        },
    ]
    return crew


def defaults() -> list[dict[str, object]]:
    """Provide default test data for space missions."""
    mission = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": datetime(2025, 7, 20),
        "duration_days": 900,
        "crew": default_crew(),
        "mission_status": "planned",
        "budget_millions": 2500.0,
    }
    invalid_mission = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": datetime(2025, 7, 20),
        "duration_days": 900,
        "crew": invalid_crew(),
        "mission_status": "planned",
        "budget_millions": 2500.0,
    }
    return [mission, invalid_mission]


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
    """Run Space Mission Crew Validation."""
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
                mission = SpaceMission.from_dict(i)
                print("Valid station created:\n" + str(mission))
            except ValidationError as e:
                print(
                    "Error creating SpaceMission:\n"
                    + str(e.errors()[0]["msg"]),
                    end="\n\n",
                )
    except Exception as e:
        print(f"Error creating SpaceMission: {e}")


if __name__ == "__main__":
    main()
