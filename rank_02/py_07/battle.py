#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    battle.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 18:01:39 by maprunty         #+#    #+#              #
#    Updated: 2026/04/18 18:31:36 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Module to test the creature factories and simulate battles."""

from ex0 import AquaFactory, FlameFactory


def TestFactory(factory):
    """Test the creature factory."""
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    base.describe()
    base.attack()
    evolved.describe()
    evolved.attack()
    print()


def battle(factory1, factory2):
    """Simulate a battle between two creatures from different factories."""
    print("Testing battle")
    creature1 = factory1.create_evolved()
    creature2 = factory2.create_evolved()
    creature1.describe()
    print(" vs.")
    creature2.describe()
    print(" fight!")
    creature1.attack()
    creature2.attack()


if __name__ == "__main__":
    TestFactory(FlameFactory())
    TestFactory(AquaFactory())
    battle(FlameFactory(), AquaFactory())
