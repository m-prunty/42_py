#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_command_quest.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:29:57 by potz             #+#    #+#              #
#    Updated: 2026/01/27 17:49:45 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Exercise 0: Command Quest.

First Foray into handling args.

Authorized: import sys, sys.argv, len(), print()

"""

import sys


def get_name(path: str) -> str:
    """Get the name of the file being run from path."""
    i = len(path) - 1
    while i >= 0 and path[i] != "/":
        i -= 1
    return path[i + 1 :]


def get_args(ac: int, av: list[str]) -> list[str]:
    """Retrieve args to a list.

    Args:
        ac (int): TODO
        av (list): aksjhdkj
    Returns: TODO
    """
    i = 1
    r_lst = [f"Arguments received: {ac - i}"]
    while i < ac:
        r_lst += [f"Argument {i}: {av[i]}"]
        i += 1
    return r_lst


def main() -> None:
    """TODO: Docstring for main.

    Returns: TODO
    """
    ac = len(sys.argv)
    name = get_name(sys.argv[0])
    av = []
    if ac <= 1:
        print("No arguments provided!")
    else:
        av = get_args(ac, sys.argv)
    print(f"Program name: {name}")
    for a in av:
        print(a)
    print(f"Total arguments: {ac}")


if __name__ == "__main__":
    main()
