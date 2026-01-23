#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:23:24 by potz             #+#    #+#              #
#    Updated: 2026/01/23 16:25:47 by potz            ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Build a 3D coordinate system using tuples.

Authorized: set(), len(), print(), union(), intersection(), difference()

Example: > python3 ft_achievement_tracker.py
    === Achievement Tracker System ===
    Player alice achievements: {
    'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    Player bob achievements: {
    'first_kill', 'level_10', 'boss_slayer', 'collector'}
    Player charlie achievements: {
    'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', '
    perfectionist'}
    === Achievement Analytics ===
    All unique achievements: {
    'boss_slayer', 'collector', 'first_kill', 'level_10', 'perfectionist', '
    speed_demon', 'treasure_hunter'}
    Total unique achievements: 7
    Common to all players: {'level_10'}
    Rare achievements (1 player): {'collector', 'perfectionist'}
    Alice vs Bob common: {'first_kill', 'level_10'}
    Alice unique: {'speed_demon', 'treasure_hunter'}
    Bob unique: {'boss_slayer', 'collector'}
"""


class Player(object):
    """Player class."""

    def __init__(self, name: str, achievements: list[str]):
        """TODO: to be defined."""
        self.name = name
        self.achievements = set(achievements)

    def __str__(self):
        """Return a str represantation of a Player instance."""
        r_str = ""
        r_str += f"{self.name}: {self.achievements}"
        return r_str

    @property
    def achievements(self) -> set:
        """achievements set."""
        return self._achievements

    @achievements.setter
    def achievements(self, value: set):
        self._achievements = value


class ATracker:
    """Docstring for ATracker."""

    def __init__(self, plyr_lst: list[Player]):
        """TODO: to be defined."""
        self.player_lst = plyr_lst

    def __repr__(self):
        return f"{[f"{i}" for i in self.player_lst]}"

    @property
    def a_achievements(self) -> set:
        """doc"""
        self._a_achievements = set()
        for p in self.player_lst:
            self._a_achievements |= p.achievements
        return self._a_achievements

    @a_achievements.setter
    def a_achievements(self, value: set):
        self._a_achievements = value

    @property
    def player_lst(self) -> list[Player]:
        """doc"""
        return self._player_lst

    @player_lst.setter
    def player_lst(self, value: list[Player]):
        self._player_lst = value
    
    
    @staticmethod
    def common_toall(player_lst: list[Player]):
        """TODO: Docstring for common_toall.

        Args:
            player_list (list[Player]): TODO

        Returns: TODO

        """
        p_set = set(player_lst[0].achievements)
        for p in player_lst:
            p_set &= p.achievements
        print(p_set)

    @staticmethod
    def diff_ofall(player_lst: list[Player]):
        """TODO: Docstring for common_toall.

        Args:
            player_list (list[Player]): TODO

        Returns: TODO

        """
        p_set = set()
        for p in player_lst:
            print(p_set)
            p_set -= p.achievements
        print(p_set)

    @classmethod
    def from_dict(cls, plyr_dict: dict):
        """TODO: Docstring for from_dict.

        Args:
            plyr_dict (dict): TODO

        Returns: TODO

        """
        p_lst = []
        for p in plyr_dict:
            p_lst += [Player(p, plyr_dict[p])]
        return cls(p_lst)

def main():
    """Driver creates dict and Player list."""
    d = {
        "alice": {
            'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'},
        "bob": {
            'first_kill', 'level_10', 'boss_slayer', 'collector'},
        "charlie": {
            'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
            'perfectionist'},
        }
    a = ATracker.from_dict(d)
    print(a)
    print(a.a_achievements)
    print(a.common_toall(a.player_lst))
    print(a)
    print(a.diff_ofall(a.player_lst))


if __name__ == "__main__":
    main()
