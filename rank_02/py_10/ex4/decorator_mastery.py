#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    decorator_mastery.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 11:08:41 by maprunty         #+#    #+#              #
#    Updated: 2026/04/29 05:12:28 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Decorator Mastery: A Decorator Exercise."""

import time
from collections.abc import Callable
from functools import wraps
from typing import Any

Spell = Callable[[str, int], str]


def spell_timer(func: Spell) -> Spell:
    """Measure the time taken to cast a spell."""

    @wraps(func)
    def wrapper(target: str, power: int) -> str:
        start_time = time.time()
        result = func(target, power)
        end_time = time.time()
        print(f"Spell cast in {end_time - start_time:.2f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[[Spell], Spell]:
    """Validate that the spell's power meets a minimum requirement."""

    def decorator(func: Spell) -> Spell:
        @wraps(func)
        def wrapper(target: str, power: int) -> Any:
            if power >= min_power:
                return func(target, power)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[[Spell], Spell]:
    """Retry a spell a specified number of times if it fails."""

    def decorator(func: Spell) -> Spell:
        @wraps(func)
        def wrapper(target: str, power: int) -> str:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(target, power)
                except Exception:
                    attempts += 1
                    print(
                        "Spell failed, retrying..."
                        + f"(attempt {attempts}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


"""
MageGuild class - Demonstrate staticmethod:
• validate_mage_name(name) - Static method that checks if name is valid
• Name is valid if it’s at least 3 characters and contains only letters/spaces
• cast_spell(self, spell_name, power) - Instance method
• Should use the power_validator decorator with min_power=10
• When power is valid, return "Successfully cast spell_name with <power> power"
• Otherwise return "Insufficient power for this spell"
"""


class MageGuild:
    """A guild of mages with spell casting capabilities."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check if the mage's name is valid."""
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with the given name and power."""

        @power_validator(10)
        def cast(target: str, power: int) -> str:
            return f"Successfully cast {spell_name} with {power} power"

        return cast(spell_name, power)


if __name__ == "__main__":

    @spell_timer
    def heal(target: str, power: int) -> str:
        """Healing spell."""
        time.sleep(1)
        return f"Heal restores {target} for {power} HP"

    @power_validator(50)
    def fireball(target: str, power: int) -> str:
        """Fireball spell."""
        return f"Fireball hits {target} for {power} damage"

    @retry_spell(3)
    def lightning_bolt(target: str, power: int) -> str:
        """Simulate casting a unstable lightning bolt spell."""
        import random

        if random.random() < 0.7:
            raise Exception("Spell failed!")
        return f"Lightning Bolt cast with power {power}!"

    print(heal("ally", 100))
    print(fireball("Dragon", 30))
    print(fireball("Goblin", 60))
    print(lightning_bolt("Goblin", 40))

    mage_guild = MageGuild()
    print(mage_guild.cast_spell("Fireball", 100))
    print(mage_guild.cast_spell("Ice Shard", 5))
