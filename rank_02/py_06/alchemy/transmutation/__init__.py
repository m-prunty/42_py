#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    __init__.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 16:25:15 by maprunty         #+#    #+#              #
#    Updated: 2026/02/22 16:27:37 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from .advanced import elixir_of_life, philosophers_stone
from .basic import lead_to_gold, stone_to_gem

__all__ = [elixir_of_life, philosophers_stone, lead_to_gold, stone_to_gem]
