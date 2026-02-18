#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:24:15 by potz             #+#    #+#              #
#    Updated: 2026/02/18 02:24:12 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""TODO: Short module summary.

Optional longer description.
=== Game Analytics Dashboard ===
=== List Comprehension Examples ===
High scorers (>2000): ['alice', 'charlie', 'diana']
Scores doubled: [4600, 3600, 4300, 4100]
Active players: ['alice', 'bob', 'charlie']
=== Dict Comprehension Examples ===
Player scores: {'alice': 2300, 'bob': 1800, 'charlie': 2150}
Score categories: {'high': 3, 'medium': 2, 'low': 1}
Achievement counts: {'alice': 5, 'bob': 3, 'charlie': 7}
=== Set Comprehension Examples ===
Unique players: {'alice', 'bob', 'charlie', 'diana'}
Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}
Active regions: {'north', 'east', 'central'}
=== Combined Analysis ===
Total players: 4
Total unique achievements: 12
Average score: 2062.5
Top performer: alice (2300 points, 5 achievements)
"""

import random


class Player:
    """Player class."""

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
        """Return a str represantation of a Player instance."""
        r_str = ""
        r_str += f"{self.name}: {self.achievements}"
        return r_str

    def __repr__(self) -> str:
        """Represantation of a Vec3 instance."""
        cls = self.__class__.__name__
        dct = self.__dict__
        d_str = ", ".join(f"{i}={dct[i]}" for i in dct)
        return f"{cls}({d_str})\n"


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
        r_str += "=== Game Analytics Dashboard ===\n\n"
        r_str += self.eg_list() + "\n"
        r_str += self.eg_dict() + "\n"
        r_str += self.eg_set() + "\n"
        r_str += self.eg_analysis() + "\n"
        return r_str

    def eg_list(self):
        hi_sc = [i.name for i in self.player_lst if i.total_score > 2000]
        sc_x2 = [i.total_score * 2 for i in self.player_lst]
        act_p = [i["player"] for i in self.filter(self.active, self.s_list)]
        r_str = ""
        r_str += "=== List Comprehension Examples ===\n"
        r_str += f"High Scorers: {hi_sc}\n"
        r_str += f"Scores Doubled: {sc_x2}\n"
        r_str += f"Active Players: {act_p}\n"
        return r_str

    def eg_dict(self):
        p_sc = {p.name: p.total_score for p in self.player_lst}
        sc_cat = {
            k: sum(
                1 for v in self.player_lst if self.levels(v.total_score) == k
            )
            for k in ("high", "medium", "low")
        }
        ach_c = {i.name: len(i.achievements) for i in self.player_lst}
        r_str = ""
        r_str += "=== Dict Comprehension Examples ===\n"
        r_str += f"Player scores: {p_sc}\n"
        r_str += f"Score categories: {sc_cat}\n"
        r_str += f"Achievement counts: {ach_c}\n"
        return r_str

    def eg_set(self):
        p_unq = {p.name for p in self.player_lst}
        ach_unq = {j for i in self.player_lst for j in i.achievements}
        act_reg = {i.active for i in self.player_lst}
        r_str = ""
        r_str += "=== Set Comprehension Examples ===\n"
        r_str += f"Unique players: {p_unq}\n"
        r_str += f"Unique achievements: {ach_unq}\n"
        r_str += f"Active regions: {act_reg}\n"
        return r_str

    def eg_analysis(self):
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
        """TODO: Docstring for from_dict.

        Args:
            plyr_dict (dict): TODO

        Returns: TODO

        """
        p_lst = []
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
        return (e for e in it if fn(e))

    @staticmethod
    def map(fn, it=None, val=None):
        return (fn(e, val) for e in it)

    @staticmethod
    def val_(e, key):
        return e[key]

    @staticmethod
    def active(e):
        return e["completed"] == False

    @staticmethod
    def levels(e):
        if e < 2000:
            return "low"
        elif e < 6000:
            return "medium"
        else:
            return "high"


#    def __str__(self) -> str:
#        """TODO: Return a tuple represantation of a Vec3 instance."""
#        r_str = ""
#        r_str += f"{self.tracker_sys()}"
#        r_str += f"\n{self.analytics()}"
#        r_str += f"\n{self.player_cmp_ach(*self.player_lst[:2])}"
#        return f"{r_str}"
#


def get_args_dict() -> tuple[int, dict[list[str]]]:
    """Retrieve program argc and argv as dict and return.

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
    a = ATracker.from_dict(av)
    print(a)


#    print(av.keys())
#    print(av["game_modes"])
#    print(av["achievements"])
#    print(av["players"])
#    if ac <= 1:
#        print("please enter seed list[dict]")
#    else:
#        a = Event(av)
#    g = GenEvent(1000)
#    g.get_preevents(a)
#    a.e_list = g.genevents()
#    print(a)
#    print(gen_demo())

if __name__ == "__main__":
    main()
