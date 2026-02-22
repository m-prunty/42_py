#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    basic.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 15:41:35 by maprunty         #+#    #+#              #
#    Updated: 2026/02/22 15:50:57 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from alchemy.elements import create_earth, create_fire


def lead_to_gold():
    """Lead transmuted to gold."""
    return lead_to_gold.__doc__[:-1] + " using " + create_fire()


def stone_to_gem():
    """Stone transmuted to gem."""
    return stone_to_gem.__doc__[:-1] + " using " + create_earth()
