#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    __init__.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/17 09:43:20 by maprunty         #+#    #+#              #
#    Updated: 2026/04/18 19:50:45 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Package for creature factories."""

from .base import Creature, CreatureFactory
from .fire import FlameFactory
from .water import AquaFactory

__all__ = ["AquaFactory", "FlameFactory", "Creature", "CreatureFactory"]
