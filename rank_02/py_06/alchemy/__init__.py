#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    __init__.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 13:19:12 by maprunty         #+#    #+#              #
#    Updated: 2026/02/22 13:19:26 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from .elements import create_fire, create_water

__all__ = ["create_fire", "create_water"]

__version__ = "1.0.0"
__author__ = "Master Pythonicus"
