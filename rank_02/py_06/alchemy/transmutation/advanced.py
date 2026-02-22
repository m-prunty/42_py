#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    advanced.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 15:51:23 by maprunty         #+#    #+#              #
#    Updated: 2026/02/22 16:24:33 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ..potions import healing_potion
from .basic import lead_to_gold


def philosophers_stone():
    """Philosopher’s stone created."""
    return (
        philosophers_stone.__doc__[:-1]
        + " using "
        + lead_to_gold()
        + " "
        + healing_potion()
    )


def elixir_of_life():
    """Elixir of life: eternal youth achieved!"""
    return elixir_of_life.__doc__[:-1]
