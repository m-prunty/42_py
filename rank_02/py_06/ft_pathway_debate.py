#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_pathway_debate.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 16:29:51 by maprunty         #+#    #+#              #
#    Updated: 2026/02/22 19:02:55 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


def open_context_fn(pckg) -> None:
    """Context manager to open package atttributes."""
    try:
        print(f"{pckg.__qualname__}: {pckg()}")
    except AttributeError:
        print(f"alchemy.{pckg}(): AttributeError - not exposed")


def absimports() -> None:
    """Testing Absolute Imports (from basic.py):."""
    from alchemy.transmutation import lead_to_gold, stone_to_gem

    print(absimports.__doc__[:-1])
    f_list = [lead_to_gold, stone_to_gem]
    [open_context_fn(fn) for fn in f_list]


def relimports() -> None:
    """Testing Relative Imports (from advanced.py):."""
    from alchemy.transmutation import elixir_of_life, philosophers_stone

    print(relimports.__doc__[:-1])
    f_list = [philosophers_stone, elixir_of_life]
    [open_context_fn(fn) for fn in f_list]


def pckg_access() -> None:
    """Testing Package Access:."""
    import alchemy.transmutation

    print(pckg_access.__doc__[:-1])
    f_list = [
        alchemy.transmutation.lead_to_gold,
        alchemy.transmutation.philosophers_stone,
    ]
    [print(fn.__module__ + "." + fn.__qualname__ + ":", fn()) for fn in f_list]


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===")
    print()
    absimports()
    print()
    relimports()
    print()
    pckg_access()
    print()
    print("Both pathways work! Absolute: clear, Relative: concise")
