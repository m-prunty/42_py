#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ArtifactCard.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/02 18:40:23 by maprunty         #+#    #+#              #
#    Updated: 2026/03/02 19:30:29 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


# ArtifactCard (Concrete Implementation)
class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ):
        super().__init__(name, cost, rarity)
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        pass

    def activate_ability(self) -> dict:
        pass
