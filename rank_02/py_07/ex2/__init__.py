#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    __init__.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 21:39:26 by maprunty         #+#    #+#              #
#    Updated: 2026/04/23 01:05:35 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Battle strategies for creatures in the tournament simulation."""

from .strategy import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
)

__all__ = [
    "AggressiveStrategy",
    "BattleStrategy",
    "DefensiveStrategy",
    "NormalStrategy",
]
