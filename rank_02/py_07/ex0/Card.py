#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    Card.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/02 16:45:33 by maprunty         #+#    #+#              #
#    Updated: 2026/03/02 19:52:52 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

# Card (Abstract Base Class)
from abc import ABC, abstractmethod


class Card(ABC):
    """Card ."""

    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.type = (self.__doc__).split(" ")[0]

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        pass

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
