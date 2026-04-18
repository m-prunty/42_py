#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    strategy.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 21:39:22 by maprunty         #+#    #+#              #
#    Updated: 2026/04/18 22:29:37 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


from abc import ABC, abstractmethod

from ex1 import HealCapability, TransformCapability


class BattleStrategy(ABC):
    def __init__(self, creature):
        self.creature = creature

    @abstractmethod
    def act(self):
        pass

    @abstractmethod
    def is_valid(self):
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self, creature):
        super().__init__(creature)

    def act(self):
        print("Normal strategy: Attack with standard moves.")

    def is_valid(self):
        return True

class AggressiveStrategy(BattleStrategy):
    def __init__(self, creature):
        super().__init__(creature)

    def act(self):
        print("Aggressive strategy: Attack with powerful moves.")

    def is_valid(self):
        return issubclass(type(self.creature), TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def __init__(self, creature):
        super().__init__(creature)

    def act(self):
        print("Defensive strategy: Focus on defense and counterattacks.")

    def is_valid(self):
        return issubclass(type(self.creature), HealCapability)
