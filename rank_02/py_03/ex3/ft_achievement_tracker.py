#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:23:24 by potz             #+#    #+#              #
#    Updated: 2026/02/18 03:35:02 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Achievement tracker and analytics using set operations.

This module builds simple player/achievement structures and provides analytics:
- Union of all achievements
- Intersection common to all players
- Rare achievements (present in exactly one player)
- Pairwise comparison between two players

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
    """A player with a name and a set of achievements.

    Args:
        name: Player identifier.
        achievements: Iterable of achievement names (converted to a set).
    """

    def __init__(self, name: str, achievements: list[str]) -> None:
        self.name: str = name
        self.achievements = set(achievements)

    def __str__(self) -> str:
        """Return a human-readable representation."""
        return f"{self.name}: {self.achievements}"

    def __repr__(self) -> str:
        """Return a debug representation."""
        cls = self.__class__.__name__
        return f"{cls}(name={self.name!r}, achievements={sorted(self.achievements)!r})"

    @property
    def achievements(self) -> set[str]:
        """The player's achievements as a set of strings."""
        return self._achievements

    @achievements.setter
    def achievements(self, value: set[str]) -> None:
        """Set the player's achievements.

        Args:
            value: Set of achievement names.
        """
        self._achievements = value


class ATracker:
    """Achievement tracker for multiple players.

    Args:
        plyr_lst: List of players to track.
    """

    def __init__(self, plyr_lst: list[Player]) -> None:
        self.player_lst = plyr_lst

    def __repr__(self) -> str:
        """Return a debug representation."""
        cls = self.__class__.__name__
        return f"{cls}(player_lst={self.player_lst!r})"

    def __str__(self) -> str:
        """Return a formatted report including system, analytics and comparison."""
        r_str = ""
        r_str += f"{self.tracker_sys()}"
        r_str += f"\n{self.analytics()}"
        r_str += f"\n{self.player_cmp_ach(*self.player_lst[:2])}"
        return r_str

    def tracker_sys(self) -> str:
        """Build the tracker overview output.

        Returns:
            A formatted string listing each player's achievements.
        """
        r_str = "\n=== Achievement Tracker System ===\n"
        for p in self.player_lst:
            r_str += f"\nPlayer {p.name} achievements: {p.achievements}"
        return r_str

    def analytics(self) -> str:
        """Build the analytics output.

        Returns:
            A formatted string showing union, count, intersection and rare set.
        """
        all_ach = self.all_achievements
        r_str = "\n=== Achievement Analytics ==="
        r_str += f"\nAll unique achievements: {all_ach}"
        r_str += f"\nTotal unique achievements: {len(all_ach)}"
        r_str += (
            f"\n\nCommon to all players: {self.common_toall(self.player_lst)}"
        )
        r_str += f"\nRare achievements: {self.unq_toplayer(self.player_lst)}"
        return r_str

    def player_cmp_ach(self, p1: Player, p2: Player) -> str:
        """Compare achievements between two players.

        Computes:
        - common achievements
        - achievements unique to each player

        Args:
            p1: First player.
            p2: Second player.

        Returns:
            A formatted comparison string.
        """
        common = p1.achievements & p2.achievements
        p1_unq = p1.achievements - common
        p2_unq = p2.achievements - common
        r_str = f"\n{p1.name.capitalize()} vs {p2.name.capitalize()} common: {common}"
        r_str += f"\n{p1.name.capitalize()} unique: {p1_unq}"
        r_str += f"\n{p2.name.capitalize()} unique: {p2_unq}"
        return r_str

    @property
    def all_achievements(self) -> set[str]:
        """Build a list of all achievements.

        Uses set Union (|) to build a list of all unique elemenmts

        Returns:
            A set containing all unique achievements from all players.
        """
        self._all_achievements = set()
        for p in self.player_lst:
            self._all_achievements |= p.achievements
        return self._all_achievements

    @property
    def player_lst(self) -> list[Player]:
        """List of tracked players."""
        return self._player_lst

    @player_lst.setter
    def player_lst(self, value: list[Player]) -> None:
        """Set the list of tracked players.

        Args:
            value: List of Player objects.
        """
        self._player_lst = value

    @staticmethod
    def common_toall(player_lst: list[Player]) -> set[str]:
        """Build a list of all achioevemnets common to all P.

        uses set intersection (&) to build a list of ach of ALL players
        Args:
            player_lst: List of players.

        Returns:
            A set of achievements shared by every player.

        Raises:
            ValueError: If player_lst is empty.
        """
        if not player_lst:
            raise ValueError("player_lst must not be empty")
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
        
        Returns:
            A set of achievements achieved by exactly one player.
        """
        diff_set: set[str] = set()
        seen_set: set[str] = set()
        for p in player_lst:
            seen_set |= diff_set & p.achievements
            diff_set ^= p.achievements
        return diff_set - seen_set

    @classmethod
    def from_dict(cls, plyr_dict: dict[str, list[str]]) -> "ATracker":
        """Construct a tracker from a dict mapping names to achievements.

        Args:
            plyr_dict: Mapping of player name to list of achievement strings.

        Returns:
            An initialized ATracker instance.
        """
        p_lst: list[Player] = []
        for name, ach_list in plyr_dict.items():
            p_lst.append(Player(name, ach_list))
        return cls(p_lst)


def get_args_dict() -> tuple[int, dict[str, list[str]]]:
    """Parse CLI arguments into a mapping of player->achievements.

    Expected format:
        name: ach1 ach2 ach3 name2: ach1 ...

    Example:
        ./ft_achievement_tracker.py alice: first_kill level_10 bob: collector

    Returns:
        A tuple (argc, argv_dict) where:
            argc: Number of parsed player entries.
            argv_dict: Mapping of player name -> list of achievements.
    """
    import sys

    av = sys.argv
    r_dct: dict[str, list[str]] = {}
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


def first_start() -> dict[str, list[str]]:
    """Provide a default dataset for demonstration.

    Returns:
        Mapping of player names to their achievement lists.
    """
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
    """Program entry point."""
    ac, av = get_args_dict()
    if ac <= 1:
        tracker = ATracker.from_dict(first_start())
    else:
        tracker = ATracker.from_dict(av)
    print(tracker)


if __name__ == "__main__":
    main()
