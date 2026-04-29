#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    functools_artifacts.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 09:29:24 by maprunty         #+#    #+#              #
#    Updated: 2026/04/29 05:17:32 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Functools Artifacts: An Exercise in functools and functional programming."""

from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers based on the specified operation."""
    if not spells:
        return 0
    if operation == "add":
        return reduce(lambda x, y: x + y, spells)
    elif operation == "multiply":
        return reduce(lambda x, y: x * y, spells)
    elif operation == "max":
        return reduce(lambda x, y: x if x > y else y, spells)
    elif operation == "min":
        return reduce(lambda x, y: x if x < y else y, spells)
    else:
        raise ValueError(f"Unknown operation: {operation}")


Enchantment = Callable[[int, str, str], str]
PartEnchant = Callable[[str], str]


def partial_enchanter(base_enchantment: Enchantment) -> dict[str, PartEnchant]:
    """Create partial applications of a base enchantment function."""
    fire_enchanter = partial(base_enchantment, 50, "fire")
    ice_enchanter = partial(base_enchantment, 50, "ice")
    lightning_enchanter = partial(base_enchantment, 50, "lightning")
    return {
        "fire": fire_enchanter,
        "ice": ice_enchanter,
        "lightning": lightning_enchanter,
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using memoization."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Dispatch spells based on their type using singledispatch."""

    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    spells = [10, 20, 30, 40]
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        """Enchantment function."""
        return (
            f"{target} is now a {element.capitalize()} {target}!!"
            + f" with {power} power"
        )

    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"]("Sword"))
    print(enchanters["ice"]("Shield"))
    print(enchanters["lightning"]("Armor"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    dispatcher = spell_dispatcher()
    print("\nTesting spell dispatcher...")
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher({}))
