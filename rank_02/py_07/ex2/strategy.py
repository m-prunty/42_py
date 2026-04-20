#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    strategy.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 21:39:22 by maprunty         #+#    #+#              #
#    Updated: 2026/04/20 02:38:21 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Battle strategies for creatures in the tournament simulation."""

from abc import ABC, abstractmethod

from ex1 import HealCapability, TransformCapability


class BattleStrategy(ABC):
    """Abstract base class for battle strategies."""

    def __init__(self, creature):
        """Initialize the strategy with a creature."""
        self.creature = creature

    @abstractmethod
    def act(self):
        """Perform the action associated with the strategy."""
        pass

    @abstractmethod
    def is_valid(self):
        """Check if the strategy is valid for the creature."""
        pass


class NormalStrategy(BattleStrategy):
    """Normal strategy: simply attack."""

    def __init__(self, creature):
        """Initialize the normal strategy with a creature."""
        super().__init__(creature)

    def act(self):
        """Perform the normal attack action."""
        self.creature.attack()

    def is_valid(self):
        """Strategy is valid for any creature."""
        return True


class AggressiveStrategy(BattleStrategy):
    """Aggressive strategy: transform, attack, then revert."""

    def __init__(self, creature):
        """Initialize the aggressive strategy with a creature."""
        super().__init__(creature)

    def act(self):
        """Perform the aggressive action: transform, attack, then revert."""
        self.creature.transform()
        self.creature.attack()
        self.creature.revert()

    def is_valid(self):
        """Check if the aggressive strategy is valid for the creature."""
        if not isinstance(self.creature, TransformCapability):
            raise StratError(self.creature, self.__class__)
        return True


class DefensiveStrategy(BattleStrategy):
    """Defensive strategy: attack, then heal itself."""

    def __init__(self, creature):
        """Initialize the defensive strategy with a creature."""
        super().__init__(creature)

    def act(self):
        """Perform the defensive action: attack, then heal itself."""
        self.creature.attack()
        self.creature.heal("itself")

    def is_valid(self):
        """Check if the defensive strategy is valid for the creature."""
        if not isinstance(self.creature, HealCapability):
            raise StratError(self.creature, self.__class__)
        return True


class StratError(TypeError):
    """Custom exception for invalid strategy usage."""

    def __init__(self, creature, strat):
        """Display creature and strategy that caused the error."""
        msg = (
            f"Invalid Creature '{type(creature).__name__}' "
            f"for this {strat.__name__[:-8].lower()} strategy"
        )
        super().__init__(msg)
