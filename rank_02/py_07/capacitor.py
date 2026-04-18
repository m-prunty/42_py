#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    capacitor.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 19:19:17 by maprunty         #+#    #+#              #
#    Updated: 2026/04/18 20:33:13 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_heal_factory():
    print("Testing Creature with healing capability:")
    factory = HealingCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(" base:")
    base.describe()
    base.attack()
    base.heal("itself")

    print(" evolved:")
    evolved.describe()
    evolved.attack()
    evolved.heal("itself and others")
    print()


def test_transform_factory():
    print("Testing Creature with transformation capability")
    factory = TransformCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(" base:")
    base.describe()
    base.attack()
    base.transform()
    base.attack()
    base.revert()

    print(" evolved:")
    evolved.describe()
    evolved.attack()
    evolved.transform()
    evolved.attack()
    evolved.revert()
    print()


if __name__ == "__main__":
    test_heal_factory()
    test_transform_factory()
