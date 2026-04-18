#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    transform.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 20:07:05 by maprunty         #+#    #+#              #
#    Updated: 2026/04/18 20:56:11 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


from ex0 import Creature, CreatureFactory

from .capability import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__(self.__class__.__name__, "Normal")

    def attack(self):
        if self.transformed:
            print(f"{super().attack()} performs a boosted strike!")
        else:
            print(f"{super().attack()} attacks normally!")

    def transform(self):
        print(f"{super().transform()} shifts into a sharper form!")

    def revert(self):
        print(f"{super().revert()} returns to normal.")


class Morphagon(Shiftling):
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.type += "/Dragon"

    def attack(self):
        if self.transformed:
            print(f"{Creature.attack(self)} unleashes a powerful attack!")
        else:
            print(f"{Creature.attack(self)} attacks normally!")

    def transform(self):
        print(
            f"{TransformCapability.transform(self)}"
            + " morphs into dragonic battle form!"
        )

    def revert(self):
        print(f"{TransformCapability.revert(self)} stabilises its form.")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()
