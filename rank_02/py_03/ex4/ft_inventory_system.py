#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/11 22:40:31 by maprunty         #+#    #+#              #
#    Updated: 2026/02/18 05:14:25 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Inventory analysis and reporting utility.

This module provides an `Inventory` class that computes summary statistics and
category groupings (plenty/moderate/scarce) for a mapping of item names to
quantities. A small CLI parser is included to build an inventory from
command-line arguments in the form `name:count`.

Example:
    $ ./ft_inventory_system.py sword:2 potion:10 shield:1

dict(), len(), print(), keys(), values(), items(), get(),
update(), sys, sys.argv
"""


class Inventory:
    """Analyze and format reports for an inventory mapping.

    The inventory is a mapping from item name to integer quantity. Upon
    initialization, totals, unique count, and category dictionaries are
    computed.

    Attributes:
        inv: Raw inventory mapping (item -> quantity).
        tot: Total quantity across all items.
        unq: Count of unique item types.
        levels: Thresholds used for categorization.
        plenty: Items with quantity in the "plenty" range.
        moderate: Items with quantity in the "moderate" range.
        scarce: Items with quantity in the "scarce" range.
    """

    inv: dict[str, int]
    tot: int
    unq: int
    levels: tuple[int, int, int, int]
    plenty: dict[str, int]
    moderate: dict[str, int]
    scarce: dict[str, int]

    def __init__(self, inventory: dict[str, int]) -> None:
        """Initialize an inventory analyzer.

        Args:
            inventory: Mapping of item names to their quantities.
        """
        self.inv = inventory
        self.levels = (1, 4, 7, 99999999)

        self.tot = sum(self.item_values())
        self.unq = len(self.item_keys())

        self.plenty = {k: v for k, v in self.inv.items() if self.lvl_chk(v, 3)}
        self.moderate = {k: v for k, v in self.inv.items() if self.lvl_chk(v, 2)}
        self.scarce = {k: v for k, v in self.inv.items() if self.lvl_chk(v, 1)}

    def __str__(self) -> str:
        """Return a full formatted report."""
        r_str = ""
        r_str += "=== Inventory System Analysis ===\n"
        r_str += "Total items in inventory: " + str(self.tot) + "\n"
        r_str += "Unique item types: " + str(self.unq) + "\n\n"
        r_str += str(self.current_inv()) + "\n"
        r_str += str(self.inv_stats()) + "\n"
        r_str += str(self.item_cat()) + "\n"
        r_str += str(self.restock()) + "\n"
        r_str += str(self.dict_props()) + "\n"
        return r_str

    def item_values(self) -> list[int]:
        """Return all quantities in the inventory."""
        return list(self.inv.values())

    def item_keys(self) -> list[str]:
        """Return all item names in the inventory."""
        return list(self.inv.keys())

    def inv_sorted(self) -> list[tuple[str, int]]:
        """Return inventory entries sorted by quantity (descending)."""
        return sorted(self.inv.items(), key=lambda m: m[1], reverse=True)

    def current_inv(self) -> str:
        """Format the current inventory with percent breakdown.

        Returns:
            A formatted multi-line string.
        """
        r_str = "=== Current Inventory ===\n"
        for k, v in self.inv_sorted():
            r_str += f"{k}: {v} {self.plural('unit', v)} ({v / self.tot * 100:.1f}%)\n"
        return r_str

    def inv_stats(self) -> str:
        """Format most/least abundant items.

        Returns:
            A formatted multi-line string.
        """
        r_str = "=== Inventory Statistics ===\n"
        srt_lst = self.inv_sorted()

        def _fmt_inv_line(tupv: tuple[str, int]) -> str:
            return f"{tupv[0]} ({tupv[1]} {self.plural('unit', tupv[1])})"

        r_str += f"Most abundant: {_fmt_inv_line(srt_lst[0])}\n"
        r_str += f"Least abundant: {_fmt_inv_line(srt_lst[-1])}\n"
        return r_str

    def item_cat(self) -> str:
        """Format item category groupings.

        Returns:
            A formatted multi-line string.
        """
        r_str = "=== Item Categories ===\n"
        r_str += "Plenty: " + str(self.plenty) + "\n" if self.plenty else ""
        r_str += (
            "Moderate: " + str(self.moderate) + "\n" if self.moderate else ""
        )
        r_str += "Scarce: " + str(self.scarce) + "\n" if self.scarce else ""
        return r_str

    def restock(self) -> str:
        """Suggest items to restock based on scarce threshold.

        Returns:
            A formatted multi-line string.
        """
        r_str = "=== Management Suggestions ===\n"
        r_str += "Restock Needed: "
        r_str += ', '.join(k for k, v in self.scarce.items() 
                           if v <= self.levels[0])
        return r_str + '\n'

    def dict_props(self) -> str:
        """Demonstrate basic dictionary properties/operations.

        Returns:
            A formatted multi-line string.
        """
        r_str = "=== Dictionary Properties Demo ===\n"
        r_str += "Dictionary keys: "
        r_str += f"{', '.join(list(self.inv.keys()))}\n"
        r_str += "Dictionary values: "
        r_str += f"{', '.join(str(i) for i in self.inv.values())}\n"
        r_str += self.lookup("sword")
        return r_str

    def lookup(self, key: str) -> str:
        """Lookup an item presence by key.

        Args:
            key: Item name to look up.

        Returns:
            A formatted single-line string describing lookup result.
        """
        r_str = f"Sample lookup - {key} in inventory: "
        r_str += f"{bool(self.inv.get(key))}"
        return r_str

    def lvl_chk(self, v: int, level: int) -> bool:
        """Check whether quantity `v` belongs to the given category level.

        Levels map to half-open ranges using ``self.levels``:
            - level=1 -> [levels[0], levels[1])
            - level=2 -> [levels[1], levels[2])
            - level=3 -> [levels[2], levels[3])

        Args:
            v: Quantity value to test.
            level: Category level (1..3).

        Returns:
            True if `v` falls into the category range, otherwise False.

        Raises:
            IndexError: If `level` is outside 1..3.
        """
        return self.levels[level - 1] <= v < self.levels[level]

    @staticmethod
    def plural(name: str = "unit", quant: int = 0) -> str:
        """Return a simple pluralized unit label.

        Args:
            name: Base unit name.
            quant: Quantity used to decide pluralization.

        Returns:
            The unit name, optionally suffixed with 's'.
        """
        return f"{name}{'s'[: quant ^ 1]}"


def get_args_dict() -> tuple[int, dict[str, int]]:
    """Parse CLI args into an inventory mapping.

    Args:
        argv: Argument list (excluding program name). If None, uses `sys.argv[1:]`.

    Returns:
        A tuple ``(ac, inventory)`` where:
            - ac: A 42-style argument count (len(inventory) + 1)
            - inventory: Parsed mapping of item -> quantity

    """
    import sys

    av = sys.argv
    r_dct: dict[str, int] = dict()
    if len(av[1:]):
        for x in av[1:]:
            k, v = x.split(":")
            r_dct[k] = int(v)
    return (len(r_dct) + 1, r_dct)


def main() -> None:
    """CLI entrypoint."""
    ac, av = get_args_dict()
    if ac > 1:
        a = Inventory(av)
        print(a)


if __name__ == "__main__":
    main()
