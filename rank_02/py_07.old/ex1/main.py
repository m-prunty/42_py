#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    main.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/02 17:32:19 by maprunty         #+#    #+#              #
#    Updated: 2026/03/04 14:53:00 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


# from .ArtifactCard import ArtifactCard
# from .SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard

from .Deck import Deck

BCK_DCT = {
    "Creature": {
        "name": "Fire Dragon",
        "cost": 5,
        "rarity": "Legendary",
        "attack": 7,
        "health": 5,
    },
    "Spell": {
        "name": "Lightning Bolt",
        "cost": 3,
        "rarity": "Common",
        "effect_type": "damage",
    },
    "Artifact": {
        "name": "Mana Crystal",
        "cost": 2,
        "rarity": "Common",
        "durability": 5,
        "effect": "Permanent: +1 mana per turn",
    },
}


def build_deck() -> Deck:
    dct = {}
    try:
        from card_generator import CardGenerator

        cg = CardGenerator()
        dct["Creature"] = cg.get_creature("Fire Dragon")
        dct["Spell"] = cg.get_creature("Lightning Bolt")
        dct["Artifact"] = cg.get_creature("Artifact")
    except ImportError as e:
        print(f"not found {e}")


def main():
    fd = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5,
    )
    gw = CreatureCard(
        name="Goblin Warrior",
        cost=3,
        rarity="Common",
        attack=7,
        health=3,
    )
    print(fd)
    build_deck()


if __name__ == "__main__":
    main()
