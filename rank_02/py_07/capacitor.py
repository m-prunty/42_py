#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    capacitor.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 19:19:17 by maprunty         #+#    #+#              #
#    Updated: 2026/04/23 22:13:06 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Testing creature factories for healing and transformation capabilities."""

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_heal_factory() -> None:
    """Testing Creature with healing capability."""
    if test_heal_factory.__doc__ is not None:
        print(test_heal_factory.__doc__[:-1])
    factory = HealingCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal("itself"))

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal("itself and others"))
    print()


def test_transform_factory() -> None:
    """Testing Creature with transform capability."""
    if test_transform_factory.__doc__ is not None:
        print(test_transform_factory.__doc__[:-1])
    factory = TransformCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())
    print()


if __name__ == "__main__":
    test_heal_factory()
    test_transform_factory()
