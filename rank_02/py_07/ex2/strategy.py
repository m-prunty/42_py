#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    strategy.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 21:39:22 by maprunty         #+#    #+#              #
#    Updated: 2026/04/22 12:16:55 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Battle strategies for creatures in the tournament simulation."""

from abc import ABC, abstractmethod

from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class BattleStrategy(ABC):
    """Abstract base class for battle strategies."""

    def __init__(self, creature: Creature) -> None:
        """Initialize the strategy with a creature."""
        self.creature = creature

    @abstractmethod
    def act(self) -> None:
        """Perform the action associated with the strategy."""
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        """Check if the strategy is valid for the creature."""
        pass


class NormalStrategy(BattleStrategy):
    """Normal strategy: simply attack."""

    def __init__(self, creature: Creature) -> None:
        """Initialize the normal strategy with a creature."""
        super().__init__(creature)

    def act(self) -> None:
        """Perform the normal attack action."""
        print(self.creature.attack())

    def is_valid(self) -> bool:
        """Strategy is valid for any creature."""
        return True


class AggressiveStrategy(BattleStrategy):
    """Aggressive strategy: transform, attack, then revert."""

    def __init__(self, creature: Creature) -> None:
        """Initialize the aggressive strategy with a creature."""
        super().__init__(creature)

    def act(self) -> None:
        """Perform the aggressive action: transform, attack, then revert."""
        if hasattr(self.creature, "transform"):
            print(self.creature.transform())
        print(self.creature.attack())
        if hasattr(self.creature, "revert"):
            print(self.creature.revert())

    def is_valid(self) -> bool:
        """Check if the aggressive strategy is valid for the creature."""
        if not isinstance(self.creature, TransformCapability):
            raise StratError(self.creature, self)
        return True


class DefensiveStrategy(BattleStrategy):
    """Defensive strategy: attack, then heal itself."""

    def __init__(self, creature: Creature) -> None:
        """Initialize the defensive strategy with a creature."""
        super().__init__(creature)

    def act(self) -> None:
        """Perform the defensive action: attack, then heal itself."""
        print(self.creature.attack())
        if hasattr(self.creature, "heal"):
            print(self.creature.heal("itself"))

    def is_valid(self) -> bool:
        """Check if the defensive strategy is valid for the creature."""
        if not isinstance(self.creature, HealCapability):
            raise StratError(self.creature, self)
        return True


class StratError(TypeError):
    """Custom exception for invalid strategy usage."""

    def __init__(self, creature: Creature, strat: BattleStrategy) -> None:
        """Display creature and strategy that caused the error."""
        msg = (
            f"Invalid Creature '{type(creature).__name__}' "
            f"for this {strat.__class__.__name__[:-8].lower()} strategy"
        )
        super().__init__(msg)
