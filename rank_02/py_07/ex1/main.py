#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    main.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/02 17:32:19 by maprunty         #+#    #+#              #
#    Updated: 2026/03/02 21:14:53 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


from ex0.CreatureCard import CreatureCard


def main():
    fd = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        #        type="Creature",
        attack=7,
        health=5,
    )
    gw = CreatureCard(
        name="Goblin Warrior",
        cost=3,
        rarity="Common",
        #        type="Creature",
        attack=7,
        health=3,
    )
    print(fd)


if __name__ == "__main__":
    main()
