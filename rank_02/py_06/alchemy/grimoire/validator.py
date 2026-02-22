#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    validator.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 18:15:00 by maprunty         #+#    #+#              #
#    Updated: 2026/02/22 19:16:45 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Simple validation:  "fire", "water", "earth", or "air" are valid."""


def validate_ingredients(ingredients: str) -> str:
    """Returns '[ingredients] - VALID' or '[ingredients] - INVALID'."""
    valid_set = {"fire", "water", "earth", "air"}
    is_valid = valid_set.intersection({*ingredients.split(" ")})
    return f"{ingredients} - {'VALID' if is_valid else 'INVALID'}"
