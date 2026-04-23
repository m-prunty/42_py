#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    heal.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 19:26:34 by maprunty         #+#    #+#              #
#    Updated: 2026/04/23 00:55:51 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Module for creatures with healing capabilities."""

from ex0 import Creature, CreatureFactory

from .capability import HealCapability


class Sproutling(Creature, HealCapability):
    """A creature that can heal itself and others."""

    def __init__(self) -> None:
        """Initialize the Sproutling with its name and type."""
        super().__init__(self.__class__.__name__, "Grass")

    def attack(self) -> str:
        """Perform an attack using Vine Whip."""
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: str) -> str:
        """Heal the target creature with a small amount."""
        return f"{self.name} heals {target} for a small amount"


class Bloomelle(Sproutling):
    """An evolved form of Sproutling with enhanced healing abilities."""

    def __init__(self) -> None:
        """Initialize the Bloomelle with its name and type."""
        super().__init__()
        self.name = self.__class__.__name__
        self.type += "/Fairy"

    def attack(self) -> str:
        """Perform an attack using Petal Dance."""
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: str) -> str:
        """Heal the target creature with a large amount."""
        return f"{self.name} heals {target} large amount"


class HealingCreatureFactory(CreatureFactory):
    """Factory for creating healing creatures."""

    def create_base(self) -> Sproutling:
        """Create a base healing creature."""
        return Sproutling()

    def create_evolved(self) -> Sproutling:
        """Create an evolved healing creature."""
        return Bloomelle()
