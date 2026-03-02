#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    SpellCard.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/02 18:27:05 by maprunty         #+#    #+#              #
#    Updated: 2026/03/02 19:33:12 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

# SpellCard (Concrete Implementation)
class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        pass

    def resolve_effect(self, targets: list) -> dict:
        pass
