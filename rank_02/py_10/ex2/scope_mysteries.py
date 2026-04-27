#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    scope_mysteries.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 07:52:02 by maprunty         #+#    #+#              #
#    Updated: 2026/04/27 09:26:33 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    def accumulate(add: int) -> int:
        nonlocal initial_power
        initial_power += add
        return initial_power

    return accumulate


def enchantment_factory(
    enchantment_type: str,
) -> Callable[[str], Callable[[], str]]:
    def enchant(item: str) -> Callable[[], str]:
        return lambda: f"{enchantment_type} {item}"

    return enchant


def memory_vault() -> dict[str, Any]:
    vault: dict[str, Callable[[Any], Any]] = {}

    def store(key: str, value: Callable[[Any | None], Any]) -> None:
        vault[key] = value

    def retrieve(key: str) -> Callable[[Any], Any] | str:
        return vault.get(key, "Memory not found")

    return {"store": store, "retrieve": retrieve}


if __name__ == "__main__":
    counter = mage_counter()
    print(counter())  # Should print 1
    print(counter())  # Should print 2

    counter2 = mage_counter()
    print(counter2())  # Should print 1 (counter2 is independent of counter)
    print(counter())  # Should print 3 (counter continues from its own state)

    accumulator = spell_accumulator(10)
    print(accumulator(20))  # Should print 30
    print(accumulator(12))  # Should print 42

    fire_enchant = enchantment_factory("Flaming")
    ice_enchant = enchantment_factory("Icy")
    print(fire_enchant("Sword")())  # Should print "Flaming Sword"
    print(ice_enchant("Shield")())  # Should print "Icy Shield"

    vault = memory_vault()
    vault["store"]("secret_spell", lambda: "Invisibility")
    print(vault["retrieve"]("secret_spell")())  # Should print "Invisibility"
    print(vault["retrieve"]("unknown_spell"))  # Should print "Memory not found
