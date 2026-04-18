#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    heal.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 19:26:34 by maprunty         #+#    #+#              #
#    Updated: 2026/04/18 20:55:28 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ex0 import Creature, CreatureFactory

from .capability import HealCapability


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__(self.__class__.__name__, "Grass")

    def attack(self):
        print(f"{super().attack()} uses Vine Whip!")

    def heal(self, target):
        print(f"{super().heal(target)} small amount")


class Bloomelle(Sproutling):
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.type += "/Fairy"

    def attack(self):
        print(f"{Creature.attack(self)} uses Petal Dance!")

    def heal(self, target):
        print(f"{HealCapability.heal(self, target)} large amount")


class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()
