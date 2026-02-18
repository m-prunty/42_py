#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:24:15 by potz             #+#    #+#              #
#    Updated: 2026/02/18 07:21:46 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Game Analytics Dashboard.

This module builds a small dashboard from player/session seed data and prints
examples of list/dict/set comprehensions plus a combined summary analysis.

Input is expected via CLI as a Python-literal dict (parsed with
``ast.literal_eval``). The schema is roughly:

- players: dict[str, dict[str, int | str]]
    Must include: level, total_score, sessions_played, favorite_mode,
    achievements_count (int)
- achievements: list[str]
- sessions: iterable[dict[str, object]]
    Used by ``eg_list()`` to report active players (sessions where completed is
    False).

The printed output sections are:
- List Comprehension Examples
- Dict Comprehension Examples
- Set Comprehension Examples
- Combined Analysis
"""

import random


class Player:
    """A game player model.

    Attributes:
        name: Player name/identifier.
        level: Current player level.
        total_score: Total accumulated score.
        sessions_played: Number of sessions played.
        favorite_mode: Favorite game mode.
        achievements: List of achievement identifiers.
        active: Region string assigned deterministically (historical name kept).
    """

    def __init__(
        self,
        name: str,
        level: int,
        total_score: int,
        sessions_played: int,
        favorite_mode: str,
        achievements: list[str],
        active: bool,
    ):
        """TODO: to be defined."""
        self.name = name
        self.level = level
        self.total_score = total_score
        self.sessions_played = sessions_played
        self.favorite_mode = favorite_mode
        self.achievements = achievements
        self.active = active

    def __str__(self) -> str:
        """Return a user-friendly representation."""
        return f"{self.name}: {self.achievements}"


class ATracker:
    """Analytics tracker that formats a dashboard from a list of players.

    Instances are typically built via :meth:`from_dict`.
    """


    def __init__(self, plyr_lst: list[Player]) -> None:
        """Initialize tracker.

        Args:
            plyr_lst: Players to analyze.
        """
        self.player_lst = plyr_lst

    def __repr__(self) -> str:
        """Return debug representation."""
        cls = self.__class__.__name__
        return f"{cls}({self.player_lst!r})"

    def __str__(self) -> str:
        """Render the full dashboard as a string."""
        r_str = ""
        r_str += "=== Game Analytics Dashboard ===\n\n"
        r_str += self.eg_list() + "\n"
        r_str += self.eg_dict() + "\n"
        r_str += self.eg_set() + "\n"
        r_str += self.eg_analysis() + "\n"
        return r_str

    def eg_list(self) -> str:
        """Generate list-comprehension examples section.

        Returns:
            Formatted section string.
        """
        hi_sc: list[str] = [p.name for p in self.player_lst if p.total_score > 2000]
        sc_x2: list[int] = [p.total_score * 2 for p in self.player_lst]
        act_p: list[str] = [s["player"] for s in self.filter(self.active, self.s_list)]
        r_str = ""
        r_str += "=== List Comprehension Examples ===\n"
        r_str += f"High Scorers: {hi_sc}\n"
        r_str += f"Scores Doubled: {sc_x2}\n"
        r_str += f"Active Players: {act_p}\n"
        return r_str

    def eg_dict(self) -> str:
        """Generate dict-comprehension examples section.

        Returns:
            Formatted section string.
        """
        p_sc: dict[str, int] = {p.name: p.total_score for p in self.player_lst}
        sc_cat: dict[str, int] = {
            k: sum(1 for p in self.player_lst if self.levels(p.total_score) == k)
            for k in ("high", "medium", "low")
        }
        ach_c: dict[str, int] = {p.name: len(p.achievements) for p in self.player_lst}
        r_str = ""
        r_str += "=== Dict Comprehension Examples ===\n"
        r_str += f"Player scores: {p_sc}\n"
        r_str += f"Score categories: {sc_cat}\n"
        r_str += f"Achievement counts: {ach_c}\n"
        return r_str

    def eg_set(self) -> str:
        """Generate set-comprehension examples section.

        Returns:
            Formatted section string.
        """
        p_unq: set[str] = {p.name for p in self.player_lst}
        ach_unq: set[str] = {a for p in self.player_lst for a in p.achievements}
        act_reg: set[str] = {p.active for p in self.player_lst}
        r_str = ""
        r_str += "=== Set Comprehension Examples ===\n"
        r_str += f"Unique players: {p_unq}\n"
        r_str += f"Unique achievements: {ach_unq}\n"
        r_str += f"Active regions: {act_reg}\n"
        return r_str
    
    def eg_analysis(self) -> str:
        """Generate combined summary analysis section.

        Returns:
            Formatted section string.

        Raises:
            ValueError: If there are no players.
        """
        p_unq = len({p.name for p in self.player_lst})
        ach_unq = len({j for i in self.player_lst for j in i.achievements})
        p_sc = [p.total_score for p in self.player_lst]
        p_top = [p for p in self.player_lst if p.total_score == max(p_sc)][0]
        r_str = ""
        r_str += "=== Combined Analysis ===\n"
        r_str += f"Total players: {p_unq}\n"
        r_str += f"Total unique achievements: {ach_unq}\n"
        r_str += f"Average score: {sum(p_sc) / len(p_sc):.2f}\n"
        r_str += f"Top performer: {p_top.name} ({p_top.total_score} points, {len(p_top.achievements)} achievements)\n"
        return r_str

    @classmethod
    def from_dict(cls, _dict: dict[str, list[str]]) -> "ATracker":
        """Build an :class:`ATracker` from seed data.

        This expands each player's ``achievements_count`` into a concrete
        achievements list sampled from ``data["achievements"]`` and assigns
        a deterministic region string to ``Player.active``.

        Args:
            data: Parsed seed dictionary.

        Returns:
            A fully constructed tracker instance.
        """
        p_lst: list[Player] = []
        p_dict = _dict["players"]
        a_list = _dict["achievements"]
        for p, v in p_dict.items():
            n_ach = v["achievements_count"]
            del v["achievements_count"]
            v["achievements"] = [ach for ach in cls.yd_rand(a_list, n_ach)]
            v["active"] = ("north", "south", "east", "west", "central")[
                sum([ord(i) for i in p]) % 5
            ]
            p_lst += [Player(p, **p_dict[p])]
        cls.s_list = _dict["sessions"]
        return cls(p_lst)

    @staticmethod
    def yd_rand(a_list, n):
        yield from random.sample(a_list, k=n)

    @staticmethod
    def filter(fn, it=None):
        """Lazy filter generator (kept to mirror builtins.filter usage)."""
        return (e for e in it if fn(e))

    @staticmethod
    def map(fn, it=None, val=None):
        """Lazy map generator applying `fn(e, val)`."""
        return (fn(e, val) for e in it)

    @staticmethod
    def val_(e, key):
        """Return dict value for key."""
        return e[key]

    @staticmethod
    def active(e):
        """Return True if a session dict is marked as not completed."""
        return e["completed"] == False

    @staticmethod
    def levels(score: int) -> str:
        """Bucketize score into low/medium/high.

        Args:
            score: Player score.

        Returns:
            One of: "low", "medium", "high".
        """
        if score < 2000:
            return "low"
        elif score < 6000:
            return "medium"
        return "high"


def get_args_dict() -> tuple[int, dict[str, str]]:
    """Parse CLI args as a Python-literal dict.

    The CLI is expected to provide a single Python-literal dict or fragments
    that join into one (original behavior preserved).

    Returns:
        A tuple of:
        - argc: Pseudo-argc defined as ``len(parsed_dict) + 1``.
        - argv_dict: Parsed seed dict (empty if nothing provided).

    NB: not including av[0] - program name str
    Returns: argc as int and argv as list[int]
    """
    import ast
    import sys

    av = sys.argv
    r_dct: dict[list[str]] = dict()
    if len(av[1:]):
        av = " ".join(str(x) for x in av[1:])
        r_dct = ast.literal_eval(av)
    return (len(r_dct) + 1, r_dct)


def main() -> None:
    """Driver creates dict and Player list."""
    ac, av = get_args_dict()
    if ac <= 1:
        print("please enter seed list[dict]")
        return
    print(ATracker.from_dict(av))


if __name__ == "__main__":
    main()
