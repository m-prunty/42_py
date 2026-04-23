#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    water.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 18:38:41 by maprunty         #+#    #+#              #
#    Updated: 2026/04/22 11:57:57 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Module defining water-type creatures and their factory."""

from .base import Creature, CreatureFactory


class Aquabub(Creature):
    """A basic water-type creature."""

    def __init__(self) -> None:
        """Initialize the Aquabub with its name and type."""
        super().__init__(self.__class__.__name__, "Water")

    def attack(self) -> str:
        """Attack with Water Gun."""
        return f"{self.name} uses Water Gun!"


class Torragon(Aquabub):
    """An evolved water-type creature."""

    def __init__(self) -> None:
        """Initialize the Torragon with its name and type."""
        super().__init__()
        self.name = self.__class__.__name__

    def attack(self) -> str:
        """Attack with Hydro Pump."""
        return f"{self.name} uses Hydro Pump!"


class AquaFactory(CreatureFactory):
    """Factory for creating water-type creatures."""

    def create_base(self) -> Creature:
        """Create an Aquabub."""
        return Aquabub()

    def create_evolved(self) -> Creature:
        """Create a Torragon."""
        return Torragon()
