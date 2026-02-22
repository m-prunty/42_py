#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_circular_curse.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 18:59:35 by maprunty         #+#    #+#              #
#    Updated: 2026/02/22 19:43:57 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""A."""

from alchemy.grimoire import record_spell, validate_ingredients

"""
Testing ingredient validation:
validate_ingredients("fire air"): fire air - VALID
validate_ingredients("dragon scales"): dragon scales - INVALID
Testing spell recording with validation:
record_spell("Fireball", "fire air"): Spell recorded: Fireball (fire air - VALID)
record_spell("Dark Magic", "shadow"): Spell rejected: Dark Magic (shadow - INVALID)
Testing late import technique:
record_spell("Lightning", "air"): Spell recorded: Lightning (air - VALID)
Circular dependency curse avoided using late imports!
All spells processed safely
"""


def fn_context(fn, val) -> None:
    """Context manager to open package atttributes."""
    try:
        if isinstance(val, str):
            print(f"{fn.__name__}({val}): {fn(val)}")
        elif isinstance(val, tuple):
            print(f"{fn.__name__}{val}: {fn(*val)}")
    except AttributeError:
        print(f"alchemy.{pckg}(): AttributeError - not exposed")


if __name__ == "__main__":
    print("=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    fn_context(validate_ingredients, ("fire air"))
    fn_context(validate_ingredients, ("dragon scales"))
    print("\nTesting spell recording with validation:")
    fn_context(record_spell, ("Fireball", "fire air"))
    fn_context(record_spell, ("Dark Magic", "shadow"))
    print("\nTesting late import technique:")
    fn_context(record_spell, (("Lightning", "air")))
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
