#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    higher_magic.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 07:05:38 by maprunty         #+#    #+#              #
#    Updated: 2026/04/29 05:16:09 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Higher Magic: A Functional Programming Exercise."""

from collections.abc import Callable

Spell = Callable[[str, int], str]


def spell_combiner(spell1: Spell, spell2: Spell) -> Spell:
    """Combine two spells into one that casts both."""
    return (
        lambda target,
        power: f"{spell1(target, power)} {spell2(target, power)}"
    )


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    """Amplify the power of a spell by a given multiplier."""
    return (
        lambda target, power: f"Mega {base_spell(target, power * multiplier)}"
    )


def conditional_caster(
    condition: Callable[[str], bool], spell: Spell
) -> Spell:
    """Cast a spell only if a certain condition is met."""
    return (
        lambda target, power: spell(target, power)
        if condition(target)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    """Create a spell that casts a sequence of spells in order."""
    return lambda target, power: [spell(target, power) for spell in spells]


def heal(target: str, power: int) -> str:
    """Healing spell."""
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    """Fireball spell."""
    return f"Fireball hits {target} for {power} damage"


if __name__ == "__main__":
    combined_spell = spell_combiner(heal, fireball)
    mega_fireball = power_amplifier(fireball, 3)
    conditional_heal = conditional_caster(
        lambda target: target == "Ally", heal
    )
    spell_routine = spell_sequence([heal, fireball, mega_fireball])
    print(combined_spell("Dragon", 50))
    print(mega_fireball("Goblin", 30))
    print(conditional_heal("Ally", 40))
    print(conditional_heal("Goblin", 40))
    print(spell_routine("Ally", 20))
