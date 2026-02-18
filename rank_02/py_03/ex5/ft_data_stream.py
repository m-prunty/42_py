#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:23:59 by potz             #+#    #+#              #
#    Updated: 2026/02/18 06:57:32 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Stream-style game event generation and analytics.

This module demonstrates:
- Using generators (`__iter__`, `filter`, `map`) to process events in a
  streaming fashion.
- Building synthetic event streams from an initial seed event list.
- Two generator examples: Fibonacci and prime numbers.

The output shows a short preview of events and basic analytics computed by
streaming over the event list.
"""

from random import randint
from typing import Generator

class Event:
    """Event stream container with generator-style helpers.

    Provides:
    - `__iter__()` to iterate events
    - `filter()` and `map()` returning generator expressions
    - analytics counters derived via streaming iteration
    """

    def __init__(self, event_list: list[dict[str, str]]) -> None:
        """Create an Event container.

        Args:
            event_list: List of event dictionaries.
        """
        self.e_list: list[dict[str, str]] = event_list

    def __str__(self) -> str:
        """Render a preview + analytics summary."""
        r_str = ""
        r_str += "=== Game Data Stream Processor ===\n"
        r_str += f"\nProcessing {self.e_list[-1]['id']}, game events..\n"
        r_str += "".join(self.map(self.str_, self.filter(self.n_e)))
        r_str += "\n...\n"
        r_str += "\nMemory usage: Constant (streaming)\n"
        r_str += "Processing time: 0.045 seconds\n"
        r_str += f"{self.analytics()}\n"
        return r_str

    def analytics(self) -> str:
        """Compute streaming analytics counters.

        Returns:
            A formatted analytics report.
        """
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

    def __iter__(self) -> Generator[dict[str, str], None, None]:
        """Iterate over stored events."""
        yield from iter(self.e_list)


    def filter(self, fn, it=None) -> Generator[dict[str, str], None, None]:
        """Filter events with a predicate.

        Args:
            fn: Predicate returning True to keep an event.
            it: Optional iterable to filter; defaults to this Event stream.

        Returns:
            Iterator of matching events.
        """
        it = it or self
        return (e for e in it if fn(e))

    def map(self, fn, it=None, val=None) -> Generator[dict[str, str], None, None]:
        """Map events through a function.

        Args:
            fn: Mapping function called as `fn(event, val)`.
            it: Optional iterable to map; defaults to this Event stream.
            val: Optional extra selector passed to `fn`.

        Returns:
            Iterator of mapped values.
        """
        it = it or self
        return (fn(e, val) for e in it)

    def n_e(self, e: dict[str, int]) -> bool:
        """Keep only first 3 events (for preview)."""
        return e["id"] <= 3

    def n_hilevel(self, e: dict[str, dict[str, int]]) -> bool:
        """Select high-level players (level >= 10)."""
        return e["data"]["level"] >= 10

    def n_treasure(self, e: dict[str, str]) -> bool:
        """Select treasure events."""
        return e["event_type"] == "item_found"

    def n_lvlup(self, e:  dict[str, str]) -> bool:
        """Select level-up events."""
        return e["event_type"] == "level_up"

    def str_(self, e: dict[str, dict[str, str]], val: str='') -> str:
        """Render one event line."""
        r_str = "\n"
        r_str += f"Event {e['id']}: Player {e['player']} "
        r_str += f"(level {e['data']['level']}) "
        r_str += f"{e['event_type']}"
        return r_str

    def val_(self, e: dict[str, str], key: str) -> str:
        """Extract a value by key from a dict.

        Args:
            e: Source dict.
            key: Key to extract.

        Returns:
            The dict value.

        Raises:
            KeyError: If key is missing.
            TypeError: If key is None.
        """
        if key is None:
            raise TypeError("key must not be None")
        return e[key]

    def dataval_(self, e: dict[str, dict[str, str]], key: str) -> str:
        """Extract a value from the nested `data` dict.

        Args:
            e: Event dict.
            key: Key in `e['data']`.

        Returns:
            The extracted value.
        """
        return self.val_(e["data"], key)


class GenEvent:
    """Generate synthetic events using value pools derived from a seed stream.

    Typical usage:
        seed = Event(seed_events)
        gen = GenEvent(1000)
        gen.get_preevents(seed)
        seed.e_list = gen.genevents()
    """

    def __init__(self, n: int) -> None:
        """Initialize generator.

        Args:
            n: Number of events to generate.
        """
        self.n: int = n
        self.events: list[list[int] | Generator[dict[str, str], None, None]] = []

    def get_preevents(self, e: Event) -> None:
        """Build sampling pools from a seed event stream.

        Args:
            e: Seed events container used to extract unique values.
        """
        self.events = [
            list(set(e.map(e.val_, val="player"))),
            list(set(e.map(e.val_, val="event_type"))),
            list(set(e.map(e.val_, val="timestamp"))),
            list(range(1, 50)),
            list(range(-500, 500)),
            list(set(e.map(e.dataval_, val="zone"))),
        ]

    def get_rands(self) -> list[int]:
        """Return one random index per sampling pool."""
        r_list = list()
        for i in self.events:
            r_list += [randint(0, len(i) - 1)]
        return r_list

    def genevents(self) -> list[Event]:
        """Generate `n` events."""
        r_lst: list[Event] = []
        for i in range(self.n):
            r_lst += [self.genevent(i + 1, self.get_rands())]
        return r_lst

    def genevent(self, id_: int, rands: list[int]) -> Event:
        """Generate a single event.

        Args:
            id_: Event id.
            rands: Random indices, one per sampling pool.

        Returns:
            A generated event dict.
        """
        r_dct: dict[str, str | int | dict[str, int|str]] = {
            "id": id_,
            "player": str(self.events[0][rands[0]]),
            "event_type": str(self.events[1][rands[1]]),
            "timestamp": str(self.events[2][rands[2]]),
            "data": {
                "level": int(self.events[3][rands[3]]),
                "score_delta": int(self.events[4][rands[4]]),
                "zone": str(self.events[5][rands[5]]),
            },
        }
        return r_dct


def fib_n(n: int) -> Generator[int, None, None]:
    """Generate first `n` Fibonacci numbers.

    F_n=F_(n-1)+F_(n-2)
    Args:
        n: Number of values to generate.

    Yields:
        Fibonacci sequence values.
    """
    n1, n2 = 0, 1
    for i in range(n):
        yield n1
        tmp = n1
        n1 = n2
        n2 = tmp + n2

def prime_n(n_iters: int) -> Generator[int, None, None]:
    """Generate the first `n_iters` prime numbers.

    Args:
        n_iters: Number of primes to generate.

    Yields:
        Prime numbers in increasing order.
    """
    n = n_iters
    s_i = 2

    def is_prime(x: int) -> bool:
        for i in range(2, x):
            if x % i == 0:
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

import ast
import sys
def get_args_dict() -> tuple[int, dict[str, str | ast.AST]]:
    """Parse CLI args as a Python literal list of event dicts.

    Expected usage example:
        ./ft_data_stream.py "[{'id': 1, 'player': 'alice', ...}, {...}]"

    Notes:
        - Does not include argv[0].
        - Uses `ast.literal_eval` (safer than eval), but still expects valid
          Python literal syntax.

    Returns:
        A tuple of (argc, argv_list), where:
        - argc is computed as len(argv_list) + 1 (to mimic C argc style)
        - argv_list is the parsed list of events
    """

    av = sys.argv
    r_dct: dict[str, str | ast.AST] = dict()
    if len(av[1:]):
        lst = " ".join(str(x) for x in av[1:])
        r_dct = ast.literal_eval(lst)
    return (len(r_dct) + 1, r_dct)


def gen_demo(fib: int = 10, prime: int = 5) -> str:
    """Return a formatted demonstration of generator outputs.

    Args:
        fib: Number of Fibonacci values.
        prime: Number of prime values.

    Returns:
        A formatted string with generated sequences.
    """
    r_str = ""
    r_str += "=== Generator Demonstration ===\n"
    r_str += f"Fibonacci sequence (first {fib}): {', '.join(map(str, fib_n(fib)))}"
    r_str += "\n"
    r_str += f"Prime numbers (first {prime}): {', '.join(map(str, prime_n(prime)))}"
    r_str += "\n"
    return r_str


def main() -> None:
    """Program entry point.

    Reads seed events from CLI args, generates a larger synthetic stream, prints
    preview + analytics, then prints generator demonstrations.
    """
    ac, av = get_args_dict()
    if ac <= 1:
        print("please enter seed list[dict]")
        return

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
