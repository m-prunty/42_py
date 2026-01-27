#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 03:20:50 by potz             #+#    #+#              #
#    Updated: 2026/01/27 20:31:06 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""First Foray into handling args and processing data.

Authorized: import sys, sys.argv, len(), print()

=== Player Score Analytics ===
Scores processed: [1500, 2300, 1800, 2100, 1950]
Total players: 5
Total score: 9650
Average score: 1930.0
High score: 2300
Low score: 1500
Score range: 800


"""

import sys


class Scorecard:
    """TODO: Docstring.

    Optional longer description.

    Attributes:
        attr (type): Description.
    """

    def __init__(self, ac: int, scores: list[int]) -> None:
        """TODO: Docstring."""
        self.scores = scores
        self.n = len(self.scores)

    def __repr__(self) -> str:
        """TODO: Docstring."""
        cls = self.__class__.__name__
        return f"{cls}(scores={self.scores!r})"

    def __str__(self) -> str:
        """TODO: Docstring."""
        r_str = ""
        r_str += f"\nScores processed: {self.__repr__()}"
        r_str += f"\nTotal players: {len(self)}"
        r_str += f"\nTotal score: {sum(self.scores)}"
        r_str += f"\nAverage score: {self.avg(self.scores)}"
        r_str += f"\nHigh score: {max(self.scores)}"
        r_str += f"\nLow score: {min(self.scores)}"
        r_str += f"\nScore range: {self.sc_range(self.scores)}"
        return r_str

    def __len__(self) -> int:
        """TODO: Docstring."""
        return len(self.scores)

    @staticmethod
    def avg(lst: list[int]) -> float:
        """TODO: Docstring for avg.

        Args:
            lst (list[int]): TODO

        Returns: TODO

        """
        return float(sum(lst) / len(lst))

    @staticmethod
    def sc_range(lst: list[int]) -> int:
        """TODO: Docstring for range.

        Args:
            lst (list[int]): TODO

        Returns: TODO

        """
        return max(lst) - min(lst)


def get_args(ac: int, av: list[str]) -> list[int]:
    """TODO: Docstring for get_args.

    Args:
        ac (int): argc
        av (list): argv
    Returns: TODO

    """
    i = 1
    r_lst = []
    while i < ac:
        try:
            r_lst += [int(av[i])]
        except ValueError:
            print(f"Error: {av[i]} Not an int")
        i += 1
    return r_lst


def main() -> None:
    """TODO: Docstring for main.

    Returns: TODO

    """
    ac = len(sys.argv)
    sc = None
    if ac <= 1:
        print("No arguments provided!")
    else:
        sc = Scorecard(ac, get_args(ac, sys.argv))
    print(f"Program name: {sc}")
    print(f"Total arguments: {ac}")


if __name__ == "__main__":
    main()
