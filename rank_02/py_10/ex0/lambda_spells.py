#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    lambda_spells.py                                  :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 04:28:21 by maprunty         #+#    #+#              #
#    Updated: 2026/04/27 20:27:45 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Lambda Spells: A Magical Data Manipulation Exercise."""

from typing import TypedDict, cast


class Mage(TypedDict):
    """Represents a mage with a name, power level, and elemental affinity."""

    name: str
    power: int
    type: str


class Artifact(TypedDict):
    """Represents a magical artifact with a name, power level, and type."""

    name: str
    power: int
    type: str


def artifact_sorter(artifacts: list[Artifact]) -> list[Artifact]:
    """Sort artifacts by their power level in descending order."""
    return sorted(artifacts, key=lambda a: (a["power"]), reverse=True)


def power_filter(mages: list[Mage], min_power: int) -> list[Mage]:
    """Filter mages with greater than or equal to min_power."""
    return list(filter(lambda m: m.get("power", 0) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform spell names by adding asterisks around them."""
    return list(map(lambda s: f"*{s}*", spells))


def mage_stats(mages: list[Mage]) -> dict[str, float | Mage]:
    """Calculate max, min, and average power of mages."""
    return {
        "max_power": max(mages, key=lambda m: m["power"]),
        "min_power": min(mages, key=lambda m: m["power"]),
        "avg_power": round(
            sum(map(lambda m: m["power"], mages)) / len(mages), 2
        ),
    }


if __name__ == "__main__":
    artifacts = cast(
        list[Artifact],
        [
            {"name": "Earth Shield", "power": 68, "type": "weapon"},
            {"name": "Shadow Blade", "power": 115, "type": "relic"},
            {"name": "Storm Crown", "power": 96, "type": "weapon"},
            {"name": "Wind Cloak", "power": 86, "type": "focus"},
        ],
    )
    mages = cast(
        list[Mage],
        [
            {"name": "Casey", "power": 84, "element": "fire"},
            {"name": "Luna", "power": 56, "element": "wind"},
            {"name": "Ash", "power": 65, "element": "water"},
            {"name": "Nova", "power": 96, "element": "light"},
            {"name": "Casey", "power": 84, "element": "earth"},
        ],
    )
    spells = ["lightning", "flash", "meteor", "blizzard"]

    print(artifact_sorter(artifacts))
    print(power_filter(mages, 85))
    print(spell_transformer(spells))
    print(mage_stats(mages))
