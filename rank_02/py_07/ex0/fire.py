#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    fire.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 18:37:30 by maprunty         #+#    #+#              #
#    Updated: 2026/04/18 20:54:31 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Module defining fire-type creatures and their factory."""

from .base import Creature, CreatureFactory


class Flameling(Creature):
    """A basic fire-type creature."""

    def __init__(self):
        """Initialize the Flameling with its name and type."""
        super().__init__(self.__class__.__name__, "Fire")

    def attack(self):
        """Attack with Ember."""
        print(f"{super().attack()} uses Ember!")


class Pyrodon(Flameling):
    """An evolved fire-type creature."""

    def __init__(self):
        """Initialize the Pyrodon with its name and type."""
        super().__init__()
        self.name = self.__class__.__name__
        self.type += "/Flying"

    def attack(self):
        """Attack with Flamethrower."""
        print(f"{Creature.attack(self)} uses Flamethrower!")


class FlameFactory(CreatureFactory):
    """Factory for creating fire-type creatures."""

    def create_base(self) -> Creature:
        """Create a Flameling."""
        return Flameling()

    def create_evolved(self) -> Creature:
        """Create a Pyrodon."""
        return Pyrodon()
