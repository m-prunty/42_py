#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    potions.py                                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 14:18:38 by maprunty         #+#    #+#              #
#    Updated: 2026/02/22 15:32:49 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Master the art of from...import.

summoning specific spells from distant grimoires with-
out bringing the entire book.i
"""

from alchemy.elements import create_earth, create_fire, create_water


def healing_potion():
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion():
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion():
    return (
        f"Invisibility potion brewed with {create_air()} and {create_water()}"
    )


def wisdom_potion():
    return "Wisdom potion brewed with all elements: [all_four_results]"
