#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    decorator_mastery.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 11:08:41 by maprunty         #+#    #+#              #
#    Updated: 2026/04/27 11:38:56 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable) -> Callable:
    import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell cast in {end_time - start_time:.2f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int, *args: Any, **kwargs: Any) -> Any:
            if power >= min_power:
                return func(power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[[Callable], Callable]:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempts += 1
                    print(
                        "Spell failed, retrying..."
                        + f"(attempt {attempts}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def cast(power: int) -> str:
            return f"Successfully cast {spell_name} with {power} power"

        return cast(power)


if __name__ == "__main__":

    @spell_timer
    def fireball(power: int) -> str:
        import time

        time.sleep(1)
        return f"Fireball cast with power {power}!"

    @power_validator(50)
    def lightning_bolt(power: int) -> str:
        return f"Lightning Bolt cast with power {power}!"

    @retry_spell(3)
    def unstable_spell() -> str:
        import random

        if random.random() < 0.7:
            raise Exception("Spell failed!")
        return "Unstable Spell cast successfully!"

    print(fireball(100))
    print(lightning_bolt(30))
    print(lightning_bolt(60))
    print(unstable_spell())

    mage_guild = MageGuild()
    print(mage_guild.cast_spell("Fireball", 100))
    print(mage_guild.cast_spell("Ice Shard", 5))
