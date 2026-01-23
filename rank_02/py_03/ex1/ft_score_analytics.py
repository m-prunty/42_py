#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 03:20:50 by potz             #+#    #+#              #
#    Updated: 2026/01/23 04:47:25 by potz            ###   ########.fr        #
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

class Player(object):

    """Docstring for Player. """

    def __init__(self, ):
        """TODO: to be defined. """


class Scorecard:
    
    def __init__(self, ac:int, scores: list[int]):
        self.scores = get_args(ac, scores)
        self.n = len(self.scores)
   
    def __repr__(self):
        return self.scores
   
    def __str__(self):
        r_str = ""
        r_str += f"\nScores processed: {self.__repr__()}"
        r_str += f"\nTotal players: {len(self)}"
        r_str += f"\nTotal score: {sum(self)}"
        r_str += f"\nAverage score: {self.avg(self)}"
        r_str += f"\nHigh score: {max(self)}"
        r_str += f"\nLow score: {min(self)}"
        r_str += f"\nScore range: {self.sc_range(self)}"
        return r_str 
    
    def __iter__(self):
        return iter(self.scores)

    def __len__(self):
        return len(self.scores)

    @staticmethod
    def avg(lst: list[int]):
        """TODO: Docstring for avg.

        Args:
            lst (list[int]): TODO

        Returns: TODO

        """
        return sum(lst) / len(lst)

    @staticmethod
    def sc_range(lst: list[int]):
        """TODO: Docstring for range.

        Args:
            lst (list[int]): TODO

        Returns: TODO

        """
        return max(lst) - min(lst)


def get_name(path: str) -> str:
    """Get the name of the file being run from path."""
    i = len(path) - 1
    while i >= 0 and path[i] != '/':
        i -= 1
    return path[i + 1:]


def get_args(ac: int, av: list) -> list[int]:
    """TODO: Docstring for get_args.

    Args:
        ac (int): TODO
        av (list):
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


def main():
    """TODO: Docstring for main.

    Returns: TODO

    """
    ac = len(sys.argv)
    name = get_name(sys.argv[0])
    av = []
    if ac <= 1:
        print("No arguments provided!")
    else:
        sc = Scorecard(ac, sys.argv)
    print(f"Program name: {sc}")
    print(f"Total arguments: {ac}")


if __name__ == "__main__":
    main()
