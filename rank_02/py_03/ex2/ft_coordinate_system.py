#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:21:53 by potz             #+#    #+#              #
#    Updated: 2026/01/30 21:15:40 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Build a 3D coordinate system using tuples.

Authorized:
    import sys, sys.argv, import math, tuple(), int(), float(),
    print(), split(), try/except, math.sqrt()

Example:
    $> python3 ft_coordinate_system.py
    === Game Coordinate System ===
    Position created: (10, 20, 5)
    Distance between (0, 0, 0) and (10, 20, 5): 22.91
    Parsing coordinates: "3,4,0"
    Parsed position: (3, 4, 0)
    Distance between (0, 0, 0) and (3, 4, 0): 5.0
    Parsing invalid coordinates: "abc,def,ghi"
    Error parsing coordinates: invalid literal for int() with base 10: 'abc'
    Error details - Type: ValueError, Args: ("invalid literal for int() with/
 base 10: 'abc'",)
    Unpacking demonstration:
    Player at x=3, y=4, z=0
    Coordinates: X=3, Y=4, Z=0
"""

import sys
from math import sqrt


class Vec3:
    """TODO: Summary of the class.

    Optional longer description.

    Attributes:
        attr (type): Description.
    """

    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        """TODO: init summary for MyClass.

        Args:
            x (int): x coordinate; defaults to 0 if none given.
            y (int): y coordinate; defaults to 0 if none given.
            z (int): z coordinate; defaults to 0 if none given.
        """
        try:
            self.x = x
            self.y = y
            self.z = z
        except CoordError as ce:
            raise CoordError(ce) from ce

    def __add__(self, other: "Vec3") -> "Vec3":
        """Add a vec3 instance with another."""
        return Vec3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __sub__(self, other: "Vec3") -> "Vec3":
        """Sub a vec3 instance with another."""
        return Vec3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    def __abs__(self) -> float:
        """Return magnitude of a vector."""
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __repr__(self) -> str:
        """Return a tuple represantation of a Vec3 instance."""
        cls = self.__class__.__name__
        return f"{cls}({self.x}, {self.y}, {self.z})"

    def __str__(self) -> str:
        """Return a str tuple represantation of a Vec3 instance."""
        return f"{self.__repr__()}"

    @property
    def x(self) -> int:
        """X coordinate value."""
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        try:
            self._x = int(value)
        except (ValueError, TypeError) as ce:
            raise CoordError(ce) from ce

    @property
    def y(self) -> int:
        """Y coordinate value."""
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        try:
            self._y = int(value)
        except (ValueError, TypeError) as ce:
            raise CoordError(ce) from ce

    @property
    def z(self) -> int:
        """Z coordinate value."""
        return self._z

    @z.setter
    def z(self, value: int) -> None:
        try:
            self._z = int(value)
        except (ValueError, TypeError) as ce:
            raise CoordError(ce) from ce

    @staticmethod
    def ft_split(string: str, char: str) -> list[str]:
        """TODO: Docstring for ft_split.

        Returns: TODO

        """
        i = 0
        j = 0
        n = len(string)
        r_list = []
        while i < n:
            while i < n and string[i] == char[0]:
                i += 1
            if i < n and string[i] != char[0]:
                if char not in string[i:]:
                    j = n
                else:
                    j = i
                    while j < n and string[j] != char[0]:
                        j += 1
                r_list += [string[i:j]]
                i += j - i
        return r_list

    @staticmethod
    def parse_args(av: list[str]) -> list[int]:
        """TODO: Docstring for get_args.

        Args:
             av (list): TODO: descriptin for av

        Returns: TODO
        """
        r_lst = []
        for arg in av:
            try:
                r_lst += [int(arg)]
            except (ValueError, TypeError) as ce:
                raise CoordError(ce.args[0]) from ce
        return r_lst

    @classmethod
    def from_str(cls, coord: str) -> "Vec3":
        """TODO: Docstring for from_str.

        Args:
            coord (str): coordinates in form "x,y,z"

        Returns: An instance of Vec3

        """
        try:
            lst = cls.parse_args([ele for ele in cls.ft_split(coord, ",")])
            return cls(lst[0], lst[1], lst[2])
        except CoordError as ce:
            raise CoordError(ce.args[0]) from ce


class Player:
    """Player class."""

    def __init__(self, start_pos: Vec3):
        """TODO: to be defined."""
        self.pos = start_pos

    def __str__(self) -> str:
        """Return a str represantation of a Player instance."""
        r_str = ""
        x, y, z = [3, 4, 0]
        r_str += "\nUnpacking Demonstation:"

        def co_str(x: int, y: int, z: int) -> str:
            return f"x={x}, y={y}, x={z}\n"

        r_str += f"\nPlayer at {co_str(x, y, z)}"
        x, y, z = [self.pos.x, self.pos.y, self.pos.z]
        r_str += f"Coordinates: {co_str(x, y, z).upper()}"
        return r_str

    @property
    def pos(self) -> Vec3:
        """Pos."""
        return self._pos

    @pos.setter
    def pos(self, value: Vec3) -> None:
        """Pos."""
        self._pos = value

    def teleport(self, to: Vec3) -> None:
        """Teleport to."""
        self.pos = to


def first_start() -> str:
    """Primer function display output from e.g."""
    start_pos = Vec3(10, 20, 5)
    r_str = f"\nPosition crerated: {start_pos}"
    origin = Vec3()
    r_str += f"\nDistance between {origin} and {start_pos}"
    r_str += f":{abs(origin - start_pos): .2f}\n"
    str_coords = "3,4,-0"
    r_str += f'\nParsing coordinates: "{str_coords}"'
    start_pos = new = Vec3.from_str(str_coords)
    r_str += f"\nParsed position: {new}"
    r_str += f"\nDistance between {origin} and {start_pos}"
    r_str += f":{abs(origin - start_pos): .1f}\n"
    print(r_str)

    str_coords = "abc,def,ghi"
    print(f"Parsing invalid coordinates: {str_coords}")
    try:
        new2 = Vec3.from_str(str_coords)
        _ = new2
    except CoordError as ce:
        orig = ce.__cause__
        print(f"Error parsing coordinates: {orig.args[0][0]}")
        print(
            f"Error details - Type: {orig.__class__.__name__}, "
            f"Args: {orig.args[0]}"
        )

    finally:
        p = Player(origin)
        p.teleport(new)
        print(p)
    return


def get_args_i() -> tuple[int, list[int]]:
    """Retrieve program argc and argv(restricted to int) and return.

    NB: not including av[0] - program name str
    Returns: argc as int and argv as list[int]
    """
    av = sys.argv
    r_lst: list[int] = []
    for a in av[1:]:
        try:
            r_lst.append(int(a.strip(",'][()")))
        except CoordError as ve:
            print(f"oops, I typed ’{a}’ instead of ’1000’ -- {ve}")
    return (len(r_lst), r_lst)


class CoordError(ValueError):
    """Error class for coordinates."""

    def __init__(self, *args: str):
        """Initialise a coord error."""
        super().__init__(args)


def main() -> None:
    """TODO: Docstring for main.

    Returns: TODO

    """
    ac, av = get_args_i()
    print("=== Game Coordinate System ===")
    if ac <= 1:
        first_start()
    else:
        print(f"Total arguments: {ac}")
        i = 0
        coord_list = []
        while i < ac:
            coord_list += [Vec3(av[i], av[i + 1], av[i + 2])]
            i += 3
        print(coord_list)


if __name__ == "__main__":
    main()
