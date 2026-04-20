#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    heal.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 19:26:34 by maprunty         #+#    #+#              #
#    Updated: 2026/04/20 02:30:38 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Module for creatures with healing capabilities."""

from ex0 import Creature, CreatureFactory

from .capability import HealCapability


class Sproutling(Creature, HealCapability):
    """A creature that can heal itself and others."""

    def __init__(self):
        """Initialize the Sproutling with its name and type."""
        super().__init__(self.__class__.__name__, "Grass")

    def attack(self):
        """Perform an attack using Vine Whip."""
        print(f"{super().attack()} uses Vine Whip!")

    def heal(self, target):
        """Heal the target creature with a small amount."""
        print(f"{super().heal(target)} small amount")


class Bloomelle(Sproutling):
    """An evolved form of Sproutling with enhanced healing abilities."""

    def __init__(self):
        """Initialize the Bloomelle with its name and type."""
        super().__init__()
        self.name = self.__class__.__name__
        self.type += "/Fairy"

    def attack(self):
        """Perform an attack using Petal Dance."""
        print(f"{Creature.attack(self)} uses Petal Dance!")

    def heal(self, target):
        """Heal the target creature with a large amount."""
        print(f"{HealCapability.heal(self, target)} large amount")


class HealingCreatureFactory(CreatureFactory):
    """Factory for creating healing creatures."""

    def create_base(self):
        """Create a base healing creature."""
        return Sproutling()

    def create_evolved(self):
        """Create an evolved healing creature."""
        return Bloomelle()
