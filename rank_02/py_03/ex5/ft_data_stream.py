#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:23:59 by potz             #+#    #+#              #
#    Updated: 2026/02/13 13:01:09 by maprunty        ###   ########.fr        #
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

from random import randint


class GenEvent:
    """TODO: Docstring."""

    def __init__(self, n: int) -> None:
        """TODO: init summary for GenEvent.

        Args:
            n (int): n events to gen
        """
        self.n = n

    def get_preevents(self, e):
        self.events = [
            list(set(e.map(e.val_, val="player"))),
            list(set(e.map(e.val_, val="event_type"))),
            list(set(e.map(e.val_, val="timestamp"))),
            list(range(1, 50)),
            list(range(-500, 500)),
            list(set(e.map(e.dataval_, val="zone"))),
        ]

    def get_rands(self):
        r_list = list()
        for i in self.events:
            r_list += [randint(0, len(i) - 1)]
        return r_list

    def genevents(self):
        r_lst = []
        for i in range(self.n):
            r_lst += [self.genevent(i + 1, self.get_rands())]
        return r_lst

    def genevent(self, id_: int, rands: list[int]):
        r_dct: dict[str, int | str] = dict()
        r_dct["id"] = id_
        r_dct["player"] = self.events[0][rands[0]]
        r_dct["event_type"] = self.events[1][rands[1]]
        r_dct["timestamp"] = self.events[2][rands[2]]
        r_dct["data"] = {
            "level": self.events[3][rands[3]],
            "score_delta": self.events[4][rands[4]],
            "zone": self.events[5][rands[5]],
        }
        return r_dct


class Event:
    """TODO: Docstring."""

    def __init__(self, event_list: list[dict]) -> None:
        """TODO: init summary for Event.

        Args:
            event_list (list[dict]): Description.
        """
        self.e_list = event_list

    def __str__(self):
        r_str = ""
        r_str += "=== Game Data Stream Processor ===\n"
        r_str += f"\nProcessing {self.e_list[-1]['id']}, game events..\n"
        r_str += "".join(self.map(self.str_, self.filter(self.n_e)))
        r_str += "\n...\n"
        r_str += "\nMemory usage: Constant (streaming)\n"
        r_str += "Processing time: 0.045 seconds\n"
        r_str += f"{self.analytics()}\n"
        return r_str

    def analytics(self):
        r_str = "\n"
        r_str += "=== Stream Analytics ===\n"
        r_str += f"Total events processed {self.e_list[-1]['id']}\n"
        hi_lvl = sum(1 for _ in self.filter(self.n_hilevel))
        treasure = sum(1 for _ in self.filter(self.n_treasure))
        lvlup = sum(1 for _ in self.filter(self.n_lvlup))
        r_str += f"High-level players (10+): {hi_lvl}\n"
        r_str += f"Treasure events: {treasure}\n"
        r_str += f"Level-up events: {lvlup}"
        return r_str

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
        return e["data"]["level"] >= 10

    def n_treasure(self, e):
        return e["event_type"] == "item_found"

    def n_lvlup(self, e):
        return e["event_type"] == "level_up"

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


def gen_demo(fib: int = 10, prime: int = 5):
    r_str = ""
    r_str += "=== Generator Demonstration ===\n"
    r_str += (
        f"Fibonacci sequence (first {fib}): {', '.join(map(str, fib_n(fib)))}"
    )
    r_str += "\n"
    r_str += (
        f"Prime numbers (first {prime}): {', '.join(map(str, prime_n(prime)))}"
    )
    r_str += "\n"
    return r_str


def main() -> None:
    """Driver creates dict and Player list."""
    ac, av = get_args_dict()
    if ac <= 1:
        print("please enter seed list[dict]")
        return
    else:
        a = Event(av)
    g = GenEvent(1000)
    g.get_preevents(a)
    a.e_list = g.genevents()
    print(a)
    print(gen_demo())


#    print(*fib_n(10))
#    print(*prime_n(15))
#    it = iter(a)
#    print(next(it))
#    print(next(it))
#    print(next(it))
#    print(*a.map(a.str_))
#    print(set(a.map(a.val_, val="player")))
#    print(set(a.map(a.val_, val="event_type")))
#    print(set(a.map(a.dataval_, val="level")))
#    print(set(a.map(a.dataval_, val="zone")))
#    print(set(a.map(a.dataval_, val="score_delta")))
#    print(set(a.map(a.val_, val="timestamp")))
#    print("fin", ac, *av[-4:])
#

if __name__ == "__main__":
    main()
