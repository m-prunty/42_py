#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_command_quest.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:29:57 by potz             #+#    #+#              #
#    Updated: 2026/01/28 19:58:37 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Exercise 0: Command Quest.

First Foray into handling args.

Authorized: import sys, sys.argv, len(), print()
"""

import sys


def get_args() -> tuple[int, list[str]]:
    """Retrieve program argc and argv and return.

    Returns: argc as int and argv as list[str]
    """

    def get_name(path: str) -> str:
        """Get the name of the file being run from path."""
        i = len(path) - 1
        while i >= 0 and path[i] != "/":
            i -= 1
        return path[i + 1 :]

    av = sys.argv
    r_lst = [get_name(av[0])]
    for a in av[1:]:
        r_lst.append(a.strip(",']["))
    return (len(r_lst), r_lst)


def main() -> None:
    """Call get_args to retrieve av, ac and print the result."""
    ac, av = get_args()
    p_lst = "No arguments provided!\n" if ac == 1 else ""
    p_lst += f"Program name: {av[0]}\n"
    p_lst += f"Arguments received: {ac - 1}\n"
    i = 1
    while i < ac:
        p_lst += f"Argument {i}: {av[i]}\n"
        i += 1
    p_lst += f"Total arguments: {ac}"
    print(p_lst)


if __name__ == "__main__":
    main()
