#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_sacred_scroll.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 13:12:16 by maprunty         #+#    #+#              #
#    Updated: 2026/02/22 14:04:23 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import alchemy


def open_context_direct(pckg) -> None:
    """Context manager to directly open package atttributes."""
    try:
        fn = getattr(alchemy.elements, pckg)
        print(f"alchemy.elements.{pckg}(): {fn()}")
    except AttributeError:
        print(f"alchemy.elements.{pckg}(): AttributeError - not exposed")


def open_context(pckg) -> None:
    """Context manager to open package atttributes."""
    try:
        fn = getattr(alchemy, pckg)
        print(f"alchemy.{pckg}(): {fn()}")
    except AttributeError:
        print(f"alchemy.{pckg}(): AttributeError - not exposed")


print("=== Sacred Scroll Mastery ===\n")
p_list = ["create_fire", "create_water", "create_earth", "create_air"]
print("Testing direct module access:")
[open_context_direct(p) for p in p_list]

print("\nTesting package-level access (controlled by __init__.py):")
[open_context(p) for p in p_list]

print("Package metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
