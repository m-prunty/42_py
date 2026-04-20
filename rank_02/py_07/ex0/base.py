#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    base.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 18:36:47 by maprunty         #+#    #+#              #
#    Updated: 2026/04/20 02:23:01 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Module defining the base Creature class and CreatureFactory interface."""

from abc import ABC, abstractmethod


class Creature(ABC):
    """Base class for all creatures."""

    def __init__(self, name: str, type: str):
        """Initialize the creature with a name and type."""
        super().__init__()
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self):
        """Abstract method for attacking."""
        return f"{self.name}"

    def describe(self):
        """Describe the creature."""
        print(f"{self.name} is a {self.type} type Creature")


class CreatureFactory(ABC):
    """Abstract factory for creating creatures."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create a base creature."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create an evolved creature."""
        pass
