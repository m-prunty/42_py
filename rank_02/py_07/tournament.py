#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    tournament.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 21:39:17 by maprunty         #+#    #+#              #
#    Updated: 2026/04/20 02:39:46 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Tournament simulation for creatures with different battle strategies."""

from ex0 import AquaFactory, FlameFactory
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)
from ex2 import AggressiveStrategy, DefensiveStrategy, NormalStrategy


def battle(creatures):
    """Simulate battles between creatures with their respective strategies."""
    for i in range(len(creatures)):
        c1 = creatures[i][0]
        s1 = creatures[i][1](c1)
        for j in range(i + 1, len(creatures)):
            c2 = creatures[j][0]
            s2 = creatures[j][1](c2)
            try:
                print("* Battle *")
                c1.describe()
                print(" vs.")
                c2.describe()
                print(" now fight!")
                s1.is_valid()
                s2.is_valid()
                s1.act()
                s2.act()
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
            print()


def get_var_name(var):
    """Get the variable name of a creature."""
    for name, value in globals().items():
        if value is var:
            return name


def print_tournament_info(creatures):
    """Print information about the tournament and the creatures involved."""
    items = [
        f"({get_var_name(c[0]).capitalize()}"
        + f"+{c[1](c[0]).__class__.__name__[:-8]})"
        for c in creatures
    ]
    print(f"[ {', '.join(items)} ]")
    print("*** Tournament ***")
    print(f"{len(creatures)} opponents involved")
    print()


def tournament():
    """Run the tournament with different creatures and strategies."""
    print("Tournament 0 (basic)")
    t0 = [(flameling, normal), (healing, defensive)]
    print_tournament_info(t0)
    battle(t0)

    print("Tournament 1 (error)")
    t1 = [(flameling, aggressive), (healing, defensive)]
    print_tournament_info(t1)
    battle(t1)

    print("Tournament 2 (multiple)")
    t2 = [(aquabub, normal), (healing, defensive), (transform, aggressive)]
    print_tournament_info(t2)
    battle(t2)


flameling = FlameFactory().create_base()
aquabub = AquaFactory().create_base()
healing = HealingCreatureFactory().create_base()
transform = TransformCreatureFactory().create_base()

normal = NormalStrategy
aggressive = AggressiveStrategy
defensive = DefensiveStrategy

if __name__ == "__main__":
    tournament()
