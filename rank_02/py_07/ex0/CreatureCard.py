#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    CreatureCard.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/02 16:45:47 by maprunty         #+#    #+#              #
#    Updated: 2026/03/02 19:49:45 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

# CreatureCard (Concrete Implementation)

from Card import Card


class CreatureCard(Card):
    """Creature Card."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def __str__(self):
        d = self.__dict__
        d |= {"type": self.type}
        return str(d)

    def play(self, game_state: dict) -> dict:
        pass

    def attack_target(self, target) -> dict:
        pass
