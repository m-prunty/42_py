#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    capacitor.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 19:19:17 by maprunty         #+#    #+#              #
#    Updated: 2026/04/20 02:41:54 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Testing creature factories for healing and transformation capabilities."""

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_heal_factory():
    """Testing Creature with healing capability."""
    print(test_heal_factory.__doc__[:-1])
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
    """Testing Creature with transform capability."""
    print(test_transform_factory.__doc__[:-1])
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
