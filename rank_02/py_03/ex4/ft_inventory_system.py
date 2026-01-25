#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/24 00:24:59 by maprunty         #+#    #+#              #
#    Updated: 2026/01/24 10:44:35 by maprunty        ###   ########.fr        #
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

    def __str__(self):
        """Return a str represantation of a Player instance."""
        r_str = ""
        r_str += f"{self.name}: {self.typ}, {self.value}"
        return r_str
    
    @classmethod
    def from_name(cls, name: str):
        """TODO: Docstring for item_from_name.

        Args:
            name (str): TODO

        Returns: TODO

        """
        if name == "sword":
            return cls(name, 'weapon', 500)
        elif name == "potion":
            return cls(name, 'consumable', 50)
        elif name == "shield":
            return cls(name, 'armor', 200)
        elif name == "magic_ring":
            return cls(name, 'armor', 250)


class Player(object):
    """Player class."""

    def __init__(self, name: str):
        """Instantiate and instance of Player class."""
        self.name = name
        self.inventory = dict()

    def __str__(self):
        """Return a str represantation of a Player instance."""
        r_str = ""
        r_str += f"{self.name}: {self.inventory}"
        return r_str

    @property
    def inventory(self) -> dict:
        """inventory get."""
        return self._inventory

    @inventory.setter
    def inventory(self, value: dict):
        self._inventory = value

    def add_item(self, itm: Item):
        print(itm)
        try:
            self.inventory[itm.name].append(itm)
        except Exception as E:
            print(E)
            self.inventory[itm.name] = [itm]

    def pop_item(self, name: str) -> Item:
        itm = self.inventory.get(name).pop()
        if not self.inventory.get(name):
            del self.inventory[name]
        return itm

    def inventory_from_dict(self, dct: dict):
        """TODO: Docstring for inventory_from.

        Args:
            arg1 (TODO): TODO

        """
        for d in dct:
            i = 0
            while i < dct[d]:
                print(i, d)
                self.add_item(Item.from_name(d))
                i += 1

    @staticmethod
    def transfer_item(plyr_a, plyr_b, name: str):
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
        Player.transfer_item(a, b, "potion")
        Player.transfer_item(a, b, "potion")

        print(a.pop_item("potion"))

    def __repr__(self):
        return f"{[i.__str__() for i in self.player_lst]}"

    @property
    def a_items(self) -> set:
        """doc"""
        self._a_items = set()
        for p in self.player_lst:
            self._a_items |= p.inventory
        return self._a_items

    @a_items.setter
    def a_items(self, value: set):
        self._a_items = value

    @property
    def player_lst(self) -> list[Player]:
        """doc"""
        return self._player_lst

    @player_lst.setter
    def player_lst(self, value: list[Player]):
        self._player_lst = value
    
    @staticmethod
    def common_toall(player_lst: list[Player]):
        """TODO: Docstring for common_toall.

        Args:
            player_list (list[Player]): TODO

        Returns: TODO

        """
        p_set = set(player_lst[0].inventory)
        for p in player_lst:
            p_set &= set(p.inventory)
        return p_set

    @staticmethod
    def unique_ofall(player_lst: list[Player]):
        """TODO: Docstring for unique_ofall.

        Args:
            playe_lst (list[Player): TODO

        Returns: TODO

        """
        p_set = ATracker.common_toall(player_lst)
        items = set()
        for p in player_lst:
            items |= set(p.inventory)
        print(p, items)
        p_set ^= items
        return p_set

    @staticmethod
    def diff_ofall(player_lst: list[Player]):
        """TODO: Docstring for common_toall.

        Args:
            player_list (list[Player]): TODO

        Returns: TODO

        """
        p_set = set()
        for p in player_lst:
            print(p_set)
            p_set -= set(p.inventory)
        print(p_set)

    @classmethod
    def from_dict(cls, plyr_dict: dict):
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

def main():
    """Driver creates dict and Player list."""
    d = {
        "alice": {
            'sword': 1,
            'potion': 5,
            'shield': 1,
            },
        "bob": {
            'magic_ring': 1, 
            'shield': 1,
            }
        }
    a = ATracker.from_dict(d)
    print(a)
    print(a.common_toall(a.player_lst))
    print(a.unique_ofall(a.player_lst))

if __name__ == "__main__":
    main()
