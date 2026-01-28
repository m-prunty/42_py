#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/24 00:24:59 by maprunty         #+#    #+#              #
#    Updated: 2026/01/28 19:49:27 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Basic inventory tracking systems.

Authorized: dict(), len(), print(), keys(), values(), items(), get(),
update()
"""


class Item:
    """Item class."""

    def __init__(self, name: str, typ: str, value: int):
        """Instantiate an instance of Item class."""
        self.name = name
        self.typ = typ
        self.value = value

    def __str__(self) -> str:
        """Return a str represantation of a Player instance."""
        r_str = ""
        r_str += f"{self.name}: {self.typ}, {self.value}"
        return r_str

    @classmethod
    def from_name(cls, name: str) -> "Item":
        """TODO: Docstring for item_from_name.

        Args:
            name (str): TODO

        Returns: TODO

        """
        if name == "sword":
            return cls(name, "weapon", 500)
        elif name == "potion":
            return cls(name, "consumable", 50)
        elif name == "shield":
            return cls(name, "armor", 200)
        elif name == "magic_ring":
            return cls(name, "armor", 250)
        elif name == "helmet":
            return cls(name, "armor", 225)
        else:
            return cls("", "", 0)


class Player:
    """Player class."""

    def __init__(self, name: str):
        """Instantiate and instance of Player class."""
        self.name = name
        self.inventory: dict[str, Item] = dict()

    def __str__(self) -> str:
        """Return a str represantation of a Player instance."""
        r_str = ""
        r_str += f"{self.name}: {self.inventory}"
        return r_str

    @property
    def inventory(self) -> dict[str, list[Item]]:
        """Inventory get."""
        return self._inventory

    @inventory.setter
    def inventory(self, value: dict[str, list[Item]]) -> None:
        self._inventory = value

    def add_item(self, itm: Item) -> None:
        """TODO: Docstring."""
        try:
            self.inventory[itm.name].append(itm)
        except Exception as e:
            print(e)
            self.inventory[itm.name] = [itm]

    def pop_item(self, name: str) -> Item:
        """TODO: Docstring."""
        items = self.inventory.get(name)
        if not items:
            del self.inventory[name]
        else:
            r_item = items.pop()
        return r_item

    def inventory_from_dict(self, dct: dict[str, int]) -> None:
        """TODO: Docstring for inventory_from.

        Args:
            dct (TODO): TODO

        """
        for d in dct:
            i = 0
            while i < dct[d]:
                self.add_item(Item.from_name(d))
                i += 1

    @staticmethod
    def transfer_item(plyr_a: "Player", plyr_b: "Player", name: str) -> None:
        """TODO: Docstring for transfer_item.

        Args:
            plyr_a (Player): TODO
            plyr_b (Player): TODO
            name (str): TODO

        Returns: TODO

        """
        itm = plyr_a.pop_item(name)
        plyr_b.add_item(itm)


class ATracker:
    """Docstring for ATracker."""

    def __init__(self, plyr_lst: list[Player]):
        """TODO: to be defined."""
        self.player_lst = plyr_lst
        a = self.player_lst[0]
        b = self.player_lst[1]
        print(a, b)
        # Player.transfer_item(a, b, "potion")
        # Player.transfer_item(a, b, "potion")

    def __repr__(self) -> str:
        """TODO: Docstring."""
        return f"a {[i for i in self.player_lst]}"

    def __str__(self) -> str:
        """Return a str represantation of a Player instance.

        === Inventory System Analysis ===
        Total items in inventory: 12
        Unique item types: 5
        === Current Inventory ===
        potion: 5 units (41.7%)
        armor: 3 units (25.0%)
        shield: 2 units (16.7%)
        sword: 1 unit (8.3%)
        helmet: 1 unit (8.3%)
        === Inventory Statistics ===
        Most abundant: potion (5 units)
        Least abundant: sword (1 unit)
        === Item Categories ===
        Moderate: {'potion': 5}
        Scarce: {'sword': 1, 'shield': 2, 'armor': 3, 'helmet': 1}
        === Management Suggestions ===
        Restock needed: ['sword', 'helmet']
        === Dictionary Properties Demo ===
        Dictionary keys: ['sword', 'potion', 'shield', 'armor', 'helmet']
        Dictionary values: [1, 5, 2, 3, 1]
        Sample lookup - 'sword' in inventory: True
        """
        r_str = "a"
        r_str = str(self.all_items)
        # r_str += f"{self.name}: {self.achievements}"
        return r_str

    @property
    def all_items(self) -> dict[str, int]:
        """TODO: Docstring."""
        self._all_items: dict[str, int] = dict()
        for p in self.player_lst:
            for i in p.inventory:
                self._all_items[i] = self._all_items.get(i, 0) + 1
                print(self._all_items)
        return self._all_items

    @all_items.setter
    def all_items(self, value: dict[str, int]) -> None:
        self._all_items = value

    @property
    def player_lst(self) -> list[Player]:
        """TODO: Docstring."""
        return self._player_lst

    @player_lst.setter
    def player_lst(self, value: list[Player]) -> None:
        self._player_lst = value

    @staticmethod
    def common_toall(player_lst: list[Player]) -> set[str]:
        """TODO: Docstring for common_toall.

        Args:
            player_lst (list[Player]): TODO

        Returns: TODO

        """
        p_set = set(player_lst[0].inventory)
        for p in player_lst:
            p_set &= set(p.inventory)
        return p_set

    @staticmethod
    def unique_ofall(player_lst: list[Player]) -> set[str]:
        """TODO: Docstring for unique_ofall.

        Args:
            player_lst (list[Player): TODO

        Returns: TODO
        """
        p_set = ATracker.common_toall(player_lst)
        items = set()
        for p in player_lst:
            items |= set(p.inventory)
        p_set ^= items
        return p_set

    @staticmethod
    def diff_ofall(player_lst: list[Player]) -> set[str]:
        """TODO: Docstring for common_toall.

        Args:
            player_lst (list[Player]): TODO

        Returns: TODO

        """
        p_set: set[str] = set()
        for p in player_lst:
            p_set -= set(p.inventory)
        return p_set

    @classmethod
    def from_dict(cls, plyr_dict: dict[str, dict[str, int]]) -> "ATracker":
        """TODO: Docstring for from_dict.

        Args:
            plyr_dict (dict): TODO

        Returns: TODO

        """
        p_lst = []
        for p in plyr_dict:
            p_cls = Player(p)
            p_cls.inventory_from_dict(plyr_dict[p])
            p_lst += [p_cls]
        return cls(p_lst)


def main() -> None:
    """Driver creates dict and Player list."""
    d = {
        "alice": {
            "sword": 1,
            "potion": 5,
            "shield": 1,
        },
        "bob": {
            "magic_ring": 1,
            "shield": 1,
        },
    }
    a = ATracker.from_dict(d)
    print(a)
    # print(a.common_toall(a.player_lst))
    # print(a.unique_ofall(a.player_lst))


if __name__ == "__main__":
    main()
