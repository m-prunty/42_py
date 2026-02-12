#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:23:24 by potz             #+#    #+#              #
#    Updated: 2026/02/05 23:42:18 by maprunty        ###   ########.fr        #
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


class Player:
    """Player class."""

    def __init__(self, name: str, achievements: list[str]):
        """TODO: to be defined."""
        self.name = name
        self.achievements = set(achievements)

    def __str__(self) -> str:
        """Return a str represantation of a Player instance."""
        r_str = ""
        r_str += f"{self.name}: {self.achievements}"
        return r_str

    def __repr__(self) -> str:
        """Represantation of a Vec3 instance."""
        cls = self.__class__.__name__
        return f"{cls}(name={self.name}, {[i for i in self.achievements]})"

    @property
    def achievements(self) -> set[str]:
        """Achievements are a set of strings."""
        return self._achievements

    @achievements.setter
    def achievements(self, value: set[str]) -> None:
        self._achievements = value


class ATracker:
    """Docstring for ATracker."""

    def __init__(self, plyr_lst: list[Player]):
        """TODO: to be defined."""
        self.player_lst = plyr_lst

    def __repr__(self) -> str:
        """TODO: Return a tuple represantation of a Vec3 instance."""
        cls = self.__class__.__name__
        return f"{cls}({[i for i in self.player_lst]})"

    def __str__(self) -> str:
        """TODO: Return a tuple represantation of a Vec3 instance."""
        r_str = ""
        r_str += f"{self.tracker_sys()}"
        r_str += f"\n{self.analytics()}"
        r_str += f"\n{self.player_cmp_ach(*self.player_lst[:2])}"
        return f"{r_str}"

    def tracker_sys(self) -> str:
        """Return a string of tracking info."""
        r_str = "\n=== Achievement Tracker System ===\n"
        for p in self.player_lst:
            r_str += f"\nPlayer {p.name} achievements: {p.achievements}"
        return r_str

    def analytics(self) -> str:
        """Return a string of analytics data."""
        all_ach = self.all_achievements
        r_str = "\n=== Achievement Analytics ==="
        r_str += f"\nAll unique Achievements: {all_ach}"
        r_str += f"\nTotal unique achievements: {len(all_ach)}"
        r_str += (
            f"\n\nCommon to all players: {self.common_toall(self.player_lst)}"
        )
        r_str += f"\nRare achievements: {self.unq_toplayer(self.player_lst)}"
        return r_str

    def player_cmp_ach(self, p1: Player, p2: Player) -> str:
        """Get achs common to 2 players and the 1's unique toeach other."""
        common = p1.achievements & p2.achievements
        p1_unq = p1.achievements - common
        p2_unq = p2.achievements - common
        r_str = f"\n{p1.name.capitalize()} vs {p2.name.capitalize()}: {common}"
        r_str += f"\n{p1.name.capitalize()}: {p1_unq}"
        r_str += f"\n{p2.name.capitalize()}: {p2_unq}"
        return r_str

    @property
    def all_achievements(self) -> set[str]:
        """Build a list of all achievements.

        Uses set Union (|) to build a list of all unique elemenmts

        Returns:
            type: Description.
        """
        self._all_achievements = set()
        for p in self.player_lst:
            self._all_achievements |= p.achievements
        return self._all_achievements

    @property
    def player_lst(self) -> list[Player]:
        """TODO: Docstring."""
        return self._player_lst

    @player_lst.setter
    def player_lst(self, value: list[Player]) -> None:
        """TODO: Docstring."""
        self._player_lst = value

    @staticmethod
    def common_toall(player_lst: list[Player]) -> set[str]:
        """Build a list of all achioevemnets common to all P.

        uses set intersection (&) to build a list of ach of ALL players
        Args:
            player_lst (list[Player]): the list of Players.
        """
        p_set = set(player_lst[0].achievements)
        for p in player_lst[1:]:
            p_set &= p.achievements
        return p_set

    @staticmethod
    def unq_toplayer(player_lst: list[Player]) -> set[str]:
        """Build a list of all achs unique to player(Rare).

        symetric difference (^) works well here for 2 sets however adding in
        the 3rd means its now going to give the symdiff of (A ^ B) ^ C
        this means the values in C not in (A ^ B) will be added. Essentially
        every even instance returns as unique while every Odd will not

        this uses seen_set built by the union of an intersection of diff_set
        and player to track what has already been seen more than once.

        The Difference (-) of diff_set and seen_set gives all unique Values

        Args:
            player_lst (list[Player]): the list of players
        """
        diff_set = set()
        seen_set = set()
        for p in player_lst:
            print(seen_set, diff_set, diff_set & p.achievements)
            seen_set |= diff_set & p.achievements
            diff_set ^= p.achievements
        print(diff_set, seen_set)
        return diff_set - seen_set

    @classmethod
    def from_dict(cls, plyr_dict: dict[str, list[str]]) -> "ATracker":
        """TODO: Docstring for from_dict.

        Args:
            plyr_dict (dict): TODO

        Returns: TODO

        """
        p_lst = []
        for p in plyr_dict:
            p_lst += [Player(p, plyr_dict[p])]
        return cls(p_lst)


def get_args_dict() -> tuple[int, dict[list[str]]]:
    """Retrieve program argc and argv as dict and return.

    NB: not including av[0] - program name str
    Returns: argc as int and argv as list[int]
    """
    import sys

    av = sys.argv
    r_dct: dict[list[str]] = dict()
    key = "Dummy"
    for a in av[1:]:
        try:
            if ":" in a:
                key = a.strip(",:'][(){}`")
                r_dct[key] = []
            else:
                r_dct[key].append(str(a.strip(",:'][(){}`")))
        except Exception as ve:
            print(f"oops, I typed {a} instead of ’1000’ -- {ve}")
    return (len(r_dct), r_dct)


def first_start() -> dict[list[str]]:
    """Define a default starting dict."""
    return {
        "alice": ["first_kill", "level_10", "treasure_hunter", "speed_demon"],
        "bob": ["first_kill", "level_10", "boss_slayer", "collector"],
        "charlie": [
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
        ],
    }


def main() -> None:
    """Driver creates dict and Player list."""
    ac, av = get_args_dict()
    if ac <= 1:
        a = ATracker.from_dict(first_start())
        print(a)
    else:
        a = ATracker.from_dict(av)
        print(a)


if __name__ == "__main__":
    main()
