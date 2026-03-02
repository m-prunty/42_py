#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    Deck.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/02 19:36:53 by maprunty         #+#    #+#              #
#    Updated: 2026/03/02 21:07:19 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

# Deck (Management Class)
class Deck:
    def __init__(self):
        self.deck: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        try:
            self.deck.remove(card_name)
            return True
        except Exception:
            print(f"Card: {card_name} not in deck")
            return False

    def shuffle(self) -> None:
        shuf(self.deck)

    def draw_card(self) -> Card:
        self.deck.pop()

    def get_deck_stats(self) -> dict:
        return
