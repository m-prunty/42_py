#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 03:20:50 by potz             #+#    #+#              #
#    Updated: 2026/02/18 03:17:47 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Exercise 1: Score Cruncher.

First foray into handling args and processing data.

Authorized: sys.argv, len(), sum(), max(), min(), int(), print()

Example:
    $ python3 ft_score_analytics.py 1500 2300 1800 2100 1950
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
    """Compute basic analytics on a list of player scores.

    Attributes:
        scores: The list of scores to analyze.
    """

    def __init__(self, ac: int, scores: list[int]) -> None:
        """Initialize the scorecard.

        Args:
            ac: Number of provided scores (kept for the exercise API).
            scores: List of integer scores.
        """
        _ = ac  # kept for signature compatibility with the exercise
        self.scores: list[int] = scores

    def __str__(self) -> str:
        """Format the score analytics as a human-readable multi-line string."""
        r_str = ""
        r_str += f"Scores processed: {self.scores!r}"
        r_str += f"\nTotal players: {len(self)}"
        r_str += f"\nTotal score: {sum(self.scores)}"
        r_str += f"\nAverage score: {self.avg(self.scores)}"
        r_str += f"\nHigh score: {max(self.scores)}"
        r_str += f"\nLow score: {min(self.scores)}"
        r_str += f"\nScore range: {self.sc_range(self.scores)}"
        return r_str

    def __len__(self) -> int:
        """Return the number of scores in the scorecard."""
        return len(self.scores)

    @staticmethod
    def avg(lst: list[int]) -> float:
        """Compute the average of a non-empty list of integers.

        Args:
            lst: Non-empty list of scores.

        Returns:
            The arithmetic mean as a float.
        """
        return float(sum(lst) / len(lst))

    @staticmethod
    def sc_range(lst: list[int]) -> int:
        """Compute the range (max - min) of a non-empty list of integers.

        Args:
            lst: Non-empty list of scores.

        Returns:
            The score range as an integer.
        """
        return max(lst) - min(lst)


def get_args_i() -> tuple[int, list[int]]:
    """Parse command-line arguments into a list of integers.

    Notes:
        - Does not include argv[0] (program name).
        - Invalid integers are reported and skipped.

    Returns:
        A tuple of (argc, argv_as_ints), where:
            - argc is the number of successfully parsed integers
            - argv_as_ints is the list of parsed scores
    """
    av: list[str] = sys.argv
    r_lst: list[int] = []
    for a in av[1:]:
        try:
            r_lst.append(int(a.strip(",'][")))
        except ValueError as ve:
            print(f"oops, I typed ’{a}’ instead of ’1000’ -- {ve}")
    return len(r_lst), r_lst


def main() -> None:
    """Program entrypoint: parse args, then print score analytics."""
    ac, av = get_args_i()
    print("=== Player Score Analytics ===")
    if ac <= 1:
        print(
            "No scores provided."
            "Usage: python3 ft_score_analytics.py <score1> <score2> ... "
        )
        return
    sc: Scorecard = Scorecard(ac, av)
    print(sc)


if __name__ == "__main__":
    main()
