#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    tournament.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 21:39:17 by maprunty         #+#    #+#              #
#    Updated: 2026/04/19 00:51:16 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ex0 import AquaFactory, FlameFactory
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)
from ex2 import AggressiveStrategy, DefensiveStrategy, NormalStrategy


def battle(creatures):
    print("*** Tournament ***")
    print_tournament_info(creatures)

    print("* Battle *")
    print(locals())
    for c1 in creatures:
        strat1 = c1[1](c1[0])
        c1[0].describe()
        for c2 in creatures:
            if c1 != c2:
                print("vs")
                c2[0].describe()
                strat2 = c2[1](c2[0])
                if strat1.is_valid() and strat2.is_valid():
                    strat1.act()
                    strat2.act()
                    print("Battle ends.\n")


def get_var_name(var):
    for name, value in globals().items():
        if value is var:
            return name


def print_tournament_info(creatures):
    fmt = "({}+{})"
    a = [
        f"{get_var_name(c[0])}+{get_var_name(c[1])}".format(c)
        for c in creatures
    ]
    print([b[0] for b in a])


def tournament():
    #    print(
    #        [
    #            f"({c[0].__class__.__name__}+{c[1](c[0]).__class__.__name__[:-8]})"
    #            for c in creatures
    #        ]
    #    )

    t0 = [(flameling, normal), (healing, defensive)]
    battle(t0)


flameling = FlameFactory().create_base()
aquabub = AquaFactory().create_base()
healing = HealingCreatureFactory().create_base()
transform = TransformCreatureFactory().create_base()

normal = NormalStrategy
aggressive = AggressiveStrategy
defensive = DefensiveStrategy

if __name__ == "__main__":
    tournament()
    # tournament([creature1, creature2, creature3, creature4])
