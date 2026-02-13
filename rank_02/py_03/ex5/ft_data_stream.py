#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:23:59 by potz             #+#    #+#              #
#    Updated: 2026/02/13 01:17:17 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""TODO: Short module summary.
next(), iter(), range(), len(), print(), typing.Generator
Optional longer description.

=== Game Data Stream Processor ===
Processing 1000 game events...
Event 1: Player alice (level 5) killed monster
Event 2: Player bob (level 12) found treasure
Event 3: Player charlie (level 8) leveled up
...
=== Stream Analytics ===
Total events processed: 1000
High-level players (10+): 342
Treasure events: 89
Level-up events: 156
Memory usage: Constant (streaming)
Processing time: 0.045 seconds
=== Generator Demonstration ===
Fibonacci sequence (first 10): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
Prime numbers (first 5): 2, 3, 5, 7, 11
"""

from random import random

class GenEvent:
    """TODO: Docstring."""

    def __init__(self, n: int) -> None:
        """TODO: init summary for GenEvent.

        Args:
            n (int): n events to gen
        """
        self.n = n

    def get_preevents(self, e):
        self.events = [set(e.map(e.val_, val="player")),
                    set(e.map(e.val_, val="event_type")),
                    set(e.map(e.dataval_, val="level")),
                    set(e.map(e.dataval_, val="zone")),
                    set(e.map(e.dataval_, val="score_delta")),
                       ]

    def get_rands(self):
        r_list  = list()
        for i in self.events:
            r_list += [random() % len(i)]
        return r_list

    def genevents(self):
        rands = [self.get_rands() for i in range(self.n)]
        
    
    def genevent(self, id_:int ):
        r_dct: dict[str, int | str ] = dict()
        r_dct["id"] = id_
        r_dct["player"] = ""
        r_dct["event_type"] = ""
        r_dct["timestamp"] = ""
        r_dct["data"] = {"level": 0,
                        "score_delta": 0,
                        "zone": 0,
                         }

        {'id': 47, 'player': 'eve', 'event_type': 'level_up', 'timestamp': '2024-01-02T19:05', 
'data': {'level': 27, 'score_delta': 497, 'zone': 'pixel_zone_5'}}

            
            
        



class Event:
    """TODO: Docstring."""

    def __init__(self, event_list: list[dict]) -> None:
        """TODO: init summary for Event.

        Args:
            event_list (list[dict]): Description.
        """
        self.e_list = event_list

    def __iter__(self):
        e = iter(self.e_list)
        yield from e

    def filter(self, fn, it=None):
        it = it or self
        return (e for e in it if fn(e))

    def map(self, fn, it=None, val=None):
        it = it or self
        return (fn(e, val) for e in it)

    def n_e(self, e):
        if e["id"] <= 3:
            return 1

    def n_hilevel(self, e):
        if e["data"]["level"] >= 10:
            return 1

    def str_(self, e, val=None):
        r_str = "\n"
        r_str += f"Event {e['id']}: Player {e['player']} "
        r_str += f"(level {e['data']['level']}) "
        r_str += f"{e['event_type']}"
        return r_str

    def val_(self, e, key):
        r_val = e[key]
        return r_val

    def dataval_(self, e, key):
        e_val = e["data"]
        return self.val_(e_val, key)


def fib_n(n):
    """F_n=F_(n-1)+F_(n-2)"""
    n1, n2 = 0, 1
    for i in range(n):
        yield n1
        tmp = n1
        n1 = n2
        n2 = tmp + n2


def prime_n(n_iters):
    """A."""
    n = n_iters
    s_i = 2

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    while n_iters:
        for i in range(s_i, n):
            if is_prime(i) and n_iters:
                n_iters -= 1
                yield i
        if n_iters:
            s_i = n
            n = n * n


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
        a = Event(av)
    else:
        a = Event(av)
    it = iter(a)
    print(next(it))
    print(next(it))
    print(next(it))
    print(*a.map(a.str_, a.filter(a.n_e)))
    print(*a.map(a.str_, a.filter(a.n_hilevel)))
    print(*a.map(a.str_))
    print(set(a.map(a.val_, val="player")))
    print(set(a.map(a.val_, val="event_type")))
    print(set(a.map(a.dataval_, val="level")))
    print(set(a.map(a.dataval_, val="zone")))
    print(set(a.map(a.dataval_, val="score_delta")))
    print(set(a.map(a.val_, val="timestamp")))
    print(*fib_n(10))
    print(*prime_n(15))
    print("fin", ac, *av[-4:])


if __name__ == "__main__":
    main()
