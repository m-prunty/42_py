#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    space_crew.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/25 23:05:36 by maprunty         #+#    #+#              #
#    Updated: 2026/04/26 00:55:28 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=8, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)

    def __str__(self) -> str:
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
        return f"{self.name} ({self.rank.value}) - {self.specialization}"


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=3, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    def __str__(self) -> str:
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
    def from_dict(cls, data: dict) -> "SpaceMission":
        crew_data = data.pop("crew", [])
        crew_members = [CrewMember(**member) for member in crew_data]
        return cls(crew=crew_members, **data)

    def add_crew_member(self, member: CrewMember) -> None:
        if len(self.crew) >= 12:
            raise ValueError("Crew cannot exceed 12 members")
        self.crew.append(member)


def default_crew() -> list[dict[str, object]]:
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


def default_mission() -> dict[str, object]:
    mission = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": datetime(2025, 7, 20),
        "duration_days": 300,
        "crew": [],
        "mission_status": "planned",
        "budget_millions": 2500.0,
    }
    return mission


def main() -> None:
    try:
        crew_data = default_crew()
        mission_data = default_mission()
        mission_data["crew"] = crew_data
        mission = SpaceMission.from_dict(mission_data)
        print(mission)
    except Exception as e:
        print(f"Error creating SpaceMission: {e}")


if __name__ == "__main__":
    main()
