#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    battle.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 18:01:39 by maprunty         #+#    #+#              #
#    Updated: 2026/04/22 12:07:11 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Module to test the creature factories and simulate battles."""

from ex0 import AquaFactory, FlameFactory


def TestFactory(factory: AquaFactory | FlameFactory) -> None:
    """Test the creature factory."""
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def battle(
    factory1: AquaFactory | FlameFactory, factory2: AquaFactory | FlameFactory
) -> None:
    """Simulate a battle between two creatures from different factories."""
    print("Testing battle")
    creature1 = factory1.create_evolved()
    creature2 = factory2.create_evolved()
    creature1.describe()
    print(" vs.")
    print(creature2.describe())
    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":
    TestFactory(FlameFactory())
    TestFactory(AquaFactory())
    battle(FlameFactory(), AquaFactory())
