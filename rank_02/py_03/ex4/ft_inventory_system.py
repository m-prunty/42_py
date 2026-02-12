#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/11 22:40:31 by maprunty         #+#    #+#              #
#    Updated: 2026/02/12 06:41:55 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""TODO: Short module summary.

dict(), len(), print(), keys(), values(), items(), get(),
update(), sys, sys.argv
Optional longer description.
"""


class Inventory:
    """TODO: Docstring."""

    def __init__(self, inventory: dict[str, int]) -> None:
        """TODO: init summary for Inventory.

        Args:
            inventory (dict[str, int]): Description.
        """
        self.inv: dict[str, int] = inventory
        self.tot: int = sum(self.item_values())
        self.unq: int = len(self.item_keys())
        self.levels: tuple[int] = (1, 4, 7)
        self.plenty = {k: v for k, v in self.inv.items() if self.lvl_chk(v, 3)}
        self.moderate = {
            k: v for k, v in self.inv.items() if self.lvl_chk(v, 2)
        }
        self.scarce = {k: v for k, v in self.inv.items() if self.lvl_chk(v, 1)}

    def __str__(self):
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
        return list(self.inv.values())

    def item_keys(self) -> list[str]:
        return list(self.inv.keys())

    def inv_sorted(self) -> list[tuple[str, int]]:
        return sorted(self.inv.items(), key=lambda m: m[1], reverse=True)

    def current_inv(self):
        r_str = "=== Current Inventory ===\n"
        for k, v in self.inv_sorted():
            r_str += f"{k}: {v} {self.plural('unit', v)} ({v / self.tot * 100:.1f}%)\n"
        return r_str

    def inv_stats(self):
        r_str = "=== Inventory Statistics ===\n"
        srt_lst = self.inv_sorted()

        def _fmt_inv_line(tupv):
            return f"{tupv[0]} ({tupv[1]} {self.plural('unit', tupv[1])})"

        r_str += f"Most abundant: {_fmt_inv_line(srt_lst[0])}\n"
        r_str += f"Least abundant: {_fmt_inv_line(srt_lst[-1])}\n"
        return r_str

    def item_cat(self):
        r_str = "=== Item Categories ===\n"
        r_str += "Plenty: " + str(self.plenty) + "\n" if self.plenty else ""
        r_str += (
            "Moderate: " + str(self.moderate) + "\n" if self.moderate else ""
        )
        r_str += "Scarce: " + str(self.scarce) + "\n" if self.scarce else ""
        return r_str

    def restock(self):
        r_str = "=== Management Suggestions ===\n"
        r_str += "Restock Needed:"
        r_str += (
            f"{[k for k, v in self.scarce.items() if v <= self.levels[0]]}\n"
        )

        return r_str

    def dict_props(self):
        r_str = "=== Dictionary Properties Demo ===\n"
        r_str += "Dictionary keys: "
        r_str += f"{list(self.inv.keys())}\n"
        r_str += "Dictionary values: "
        r_str += f"{list(self.inv.values())}\n"
        r_str += self.lookup("sword")
        return r_str

    def lookup(self, key):
        r_str = f"Sample lookup - {key} in inventory: "
        r_str += f"{bool(self.inv.get(key))}"
        return r_str

    def lvl_chk(self, v, level):
        if self.levels[level - 1] <= v < self.levels[level]:
            return 1
        return 0

    @staticmethod
    def plural(name: str = "unit", quant: int = 0) -> str:
        return f"{name}{'s'[: quant ^ 1]}"


def get_args_dict():
    import sys

    av = sys.argv
    r_dct: dict[list[str]] = dict()
    if len(av[1:]):
        for x in av[1:]:
            k, v = x.split(":")
            r_dct[k] = int(v)
    return (len(r_dct) + 1, r_dct)


def main() -> None:
    """Driver creates dict and Player list."""
    ac, av = get_args_dict()
    if ac > 1:
        a = Inventory(av)
        print(a)


if __name__ == "__main__":
    main()
