#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    spellbook.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 18:19:31 by maprunty         #+#    #+#              #
#    Updated: 2026/02/22 19:44:51 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    """Records spells after validation."""
    v_res = validate_ingredients(ingredients)
    return (
        f"Spell recorded: {spell_name} ({v_res})"
        if v_res.rsplit(" ")[-1] == "VALID"
        else f"Spell rejected: {spell_name} ({v_res})"
    )
