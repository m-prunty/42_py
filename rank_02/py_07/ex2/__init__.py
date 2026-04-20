#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    __init__.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 21:39:26 by maprunty         #+#    #+#              #
#    Updated: 2026/04/20 02:33:52 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Battle strategies for creatures in the tournament simulation."""

from .strategy import AggressiveStrategy, DefensiveStrategy, NormalStrategy

__all__ = ["AggressiveStrategy", "DefensiveStrategy", "NormalStrategy"]
