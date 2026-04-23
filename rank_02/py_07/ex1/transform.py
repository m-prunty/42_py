#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    transform.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 20:07:05 by maprunty         #+#    #+#              #
#    Updated: 2026/04/22 20:45:30 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Module for creatures with transformation capabilities."""

from ex0 import Creature, CreatureFactory

from .capability import TransformCapability


class Shiftling(Creature, TransformCapability):
    """A creature that can transform to boost its abilities."""

    def __init__(self) -> None:
        """Initialize the Shiftling with its name and type."""
        super().__init__(self.__class__.__name__, "Normal")

    def attack(self) -> str:
        """Perform an attack, with a boost if transformed."""
        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} attacks normally."

    def transform(self) -> str:
        """Transform the Shiftling into a sharper form."""
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        """Revert the Shiftling back to its normal form."""
        return f"{self.name} returns to normal."


class Morphagon(Shiftling):
    """An evolved form of Shiftling."""

    def __init__(self) -> None:
        """Initialize the Morphagon with its name and type."""
        super().__init__()
        self.name = self.__class__.__name__
        self.type += "/Dragon"

    def attack(self) -> str:
        """Perform an attack, with a powerful boost if transformed."""
        if self.transformed:
            return f"{self.name} unleashes a powerful attack!"
        else:
            return f"{self.name} attacks normally."

    def transform(self) -> str:
        """Transform the Morphagon into its dragonic battle form."""
        return f"{self.name} morphs into dragonic battle form!"

    def revert(self) -> str:
        """Revert the Morphagon back to its normal form."""
        return f"{self.name} stabilises its form."


class TransformCreatureFactory(CreatureFactory):
    """Factory for creating Shiftling and Morphagon creatures."""

    def create_base(self) -> Shiftling:
        """Create a base creature, which is a Shiftling."""
        return Shiftling()

    def create_evolved(self) -> Shiftling:
        """Create an evolved creature, which is a Morphagon."""
        return Morphagon()
