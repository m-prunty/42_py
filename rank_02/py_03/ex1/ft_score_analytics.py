#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 03:20:50 by potz             #+#    #+#              #
#    Updated: 2026/01/28 20:20:00 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Exercise 1: Score Cruncher.

First Foray into handling args and processing data.

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
        return f"{self.scores!r}"

    def __str__(self) -> str:
        """TODO: Docstring."""
        r_str = ""
        r_str += f"Scores processed: {self!r}"
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


def get_args_i() -> tuple[int, list[int]]:
    """Retrieve program argc and argv(restricted to int) and return.

    NB: not including av[0] - program name str
    Returns: argc as int and argv as list[int]
    """
    av = sys.argv
    r_lst: list[int] = []
    for a in av[1:]:
        try:
            r_lst.append(int(a.strip(",'][")))
        except ValueError as ve:
            print(f"oops, I typed ’{a}’ instead of ’1000’ -- {ve}")
    return (len(r_lst), r_lst)


def main() -> None:
    """TODO: Docstring for main.

    Returns: TODO

    """
    ac, av = get_args_i()
    sc = None
    print("=== Player Score Analytics ===")
    if ac <= 1:
        print(
            "No scores provided. \
Usage: python3 ft_score_analytics.py <score1> <score2> ... "
        )
    else:
        sc = Scorecard(ac, av)
        print(sc)


if __name__ == "__main__":
    main()
