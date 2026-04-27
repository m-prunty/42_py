#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    higher_magic.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 07:05:38 by maprunty         #+#    #+#              #
#    Updated: 2026/04/27 07:42:34 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Higher Magic: A Functional Programming Exercise."""

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return (
        lambda target, power: spell(target, power)
        if condition(target)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [spell(target, power) for spell in spells]


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


combined_spell = spell_combiner(heal, fireball)
mega_fireball = power_amplifier(fireball, 3)
conditional_heal = conditional_caster(lambda target: target == "Ally", heal)
spell_routine = spell_sequence([heal, fireball, mega_fireball])

if __name__ == "__main__":
    print(combined_spell("Ally", 50))
    print(mega_fireball("Enemy", 30))
    print(conditional_heal("Ally", 40))
    print(conditional_heal("Enemy", 40))
    print(spell_routine("Ally", 20))
