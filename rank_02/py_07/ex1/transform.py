#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    transform.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 20:07:05 by maprunty         #+#    #+#              #
#    Updated: 2026/04/20 02:28:14 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Module for creatures with transformation capabilities."""

from ex0 import Creature, CreatureFactory

from .capability import TransformCapability


class Shiftling(Creature, TransformCapability):
    """A creature that can transform to boost its abilities."""

    def __init__(self):
        """Initialize the Shiftling with its name and type."""
        super().__init__(self.__class__.__name__, "Normal")

    def attack(self):
        """Perform an attack, with a boost if transformed."""
        if self.transformed:
            print(f"{super().attack()} performs a boosted strike!")
        else:
            print(f"{super().attack()} attacks normally.")

    def transform(self):
        """Transform the Shiftling into a sharper form."""
        print(f"{super().transform()} shifts into a sharper form!")

    def revert(self):
        """Revert the Shiftling back to its normal form."""
        print(f"{super().revert()} returns to normal.")


class Morphagon(Shiftling):
    """An evolved form of Shiftling."""

    def __init__(self):
        """Initialize the Morphagon with its name and type."""
        super().__init__()
        self.name = self.__class__.__name__
        self.type += "/Dragon"

    def attack(self):
        """Perform an attack, with a powerful boost if transformed."""
        if self.transformed:
            print(f"{Creature.attack(self)} unleashes a powerful attack!")
        else:
            print(f"{Creature.attack(self)} attacks normally.")

    def transform(self):
        """Transform the Morphagon into its dragonic battle form."""
        print(
            f"{TransformCapability.transform(self)}"
            + " morphs into dragonic battle form!"
        )

    def revert(self):
        """Revert the Morphagon back to its normal form."""
        print(f"{TransformCapability.revert(self)} stabilises its form.")


class TransformCreatureFactory(CreatureFactory):
    """Factory for creating Shiftling and Morphagon creatures."""

    def create_base(self):
        """Create a base creature, which is a Shiftling."""
        return Shiftling()

    def create_evolved(self):
        """Create an evolved creature, which is a Morphagon."""
        return Morphagon()
