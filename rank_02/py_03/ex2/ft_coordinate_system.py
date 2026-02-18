#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:21:53 by potz             #+#    #+#              #
#    Updated: 2026/02/18 03:21:26 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Build a 3D coordinate system using tuples.

This module provides a small 3D integer vector type (`Vec3`), a `Player` wrapper
around a position, and a tiny CLI demo.

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


class CoordError(ValueError):
    """Raised when a coordinate cannot be parsed or coerced to an integer.

    Args:
        *args: Message parts (kept compatible with `ValueError`).
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Vec3:
    """3D integer vector.

    The vector stores integer coordinates and supports basic vector arithmetic.

    Attributes:
        x: X coordinate (int).
        y: Y coordinate (int).
        z: Z coordinate (int).
    """

    def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
        """Initialize a `Vec3`.

        Args:
            x: X coordinate (coerced with `int()`).
            y: Y coordinate (coerced with `int()`).
            z: Z coordinate (coerced with `int()`).

        Raises:
            CoordError: If any coordinate cannot be coerced to `int`.
        """
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Vec3") -> "Vec3":
        """Add two vectors component-wise.

        Args:
            other: Another vector.

        Returns:
            A new `Vec3` equal to `self + other`.
        """
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vec3") -> "Vec3":
        """Subtract two vectors component-wise.

        Args:
            other: Another vector.

        Returns:
            A new `Vec3` equal to `self - other`.
        """
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __abs__(self) -> float:
        """Compute the Euclidean magnitude of the vector.

        Returns:
            Vector length as a float.
        """
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __repr__(self) -> str:
        """Return a debug representation.

        Returns:
            A string like `Vec3(1, 2, 3)`.
        """
        cls = self.__class__.__name__
        return f"{cls}({self.x}, {self.y}, {self.z})"

    def __str__(self) -> str:
        """Return a user-facing representation.

        Returns:
            A string like `(1, 2, 3)`.
        """
        return f"({self.x}, {self.y}, {self.z})"
    @property
    def x(self) -> int:
        """X coordinate."""
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        """Set X coordinate.

        Args:
            value: Value coerced to `int`.

        Raises:
            CoordError: If coercion fails.
        """
        try:
            self._x = int(value)
        except (ValueError, TypeError) as exc:
            raise CoordError(str(exc)) from exc

    @property
    def y(self) -> int:
        """Y coordinate."""
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        """Set Y coordinate.

        Args:
            value: Value coerced to `int`.

        Raises:
            CoordError: If coercion fails.
        """
        try:
            self._y = int(value)
        except (ValueError, TypeError) as exc:
            raise CoordError(str(exc)) from exc

    @property
    def z(self) -> int:
        """Z coordinate."""
        return self._z

    @z.setter
    def z(self, value: int) -> None:
        """Set Z coordinate.

        Args:
            value: Value coerced to `int`.

        Raises:
            CoordError: If coercion fails.
        """
        try:
            self._z = int(value)
        except (ValueError, TypeError) as exc:
            raise CoordError(str(exc)) from exc

    @staticmethod
    def ft_split(string: str, char: str) -> list[str]:
        """Split a string on a single delimiter (42-style helper).

        Args:
            string: Input string.
            char: Delimiter string (only `char[0]` is used).

        Returns:
            List of non-empty segments (consecutive delimiters are skipped).
        """
        i = 0
        j = 0
        n = len(string)
        r_list: list[str] = []
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
        """Parse a list of strings into integers.

        Args:
            av: List of strings to convert.

        Returns:
            List of integers.

        Raises:
            CoordError: If an element cannot be converted to `int`.
        """
        r_lst: list[int] = []
        for arg in av:
            try:
                r_lst += [int(arg)]
            except (ValueError, TypeError) as exc:
                raise CoordError(str(exc)) from exc
        return r_lst

    @classmethod
    def from_str(cls, coord: str) -> "Vec3":
        """Create a vector from a coordinate string `"x,y,z"`.

        Args:
            coord: Coordinates in the form `"x,y,z"`.

        Returns:
            A `Vec3` instance.

        Raises:
            CoordError: If parsing/conversion fails or not enough components.
        """
        try:
            parts = cls.ft_split(coord, ",")
            lst = cls.parse_args([ele for ele in parts])
            return cls(lst[0], lst[1], lst[2])
        except (IndexError, CoordError) as exc:
            raise CoordError(str(exc)) from exc


class Player:
    """Player holding a position in 3D space.

    Args:
        start_pos: Initial player position.
    """

    def __init__(self, start_pos: Vec3) -> None:
        self.pos = start_pos

    def __str__(self) -> str:
        """Demonstrate tuple-style unpacking with coordinates.

        Returns:
            A formatted multiline string.
        """
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
        """Current position."""
        return self._pos

    @pos.setter
    def pos(self, value: Vec3) -> None:
        """Set current position."""
        self._pos = value

    def teleport(self, to: Vec3) -> None:
        """Teleport player to a new position.

        Args:
            to: Target position.
        """
        self.pos = to


def first_start() -> None:
    """Run the built-in demonstration from the module docstring."""
    start_pos = Vec3(10, 20, 5)
    r_str = f"\nPosition crerated: {start_pos}"
    origin = Vec3()
    r_str += f"\nDistance between {origin} and {start_pos}"
    r_str += f":{abs(origin - start_pos): .2f}\n"
    str_coords = "3,4,0"
    r_str += f'\nParsing coordinates: "{str_coords}"'
    start_pos = new = Vec3.from_str(str_coords)
    r_str += f"\nParsed position: {new}"
    r_str += f"\nDistance between {origin} and {start_pos}"
    r_str += f":{abs(origin - start_pos): .1f}\n"
    print(r_str)

    str_coords = "abc,def,ghi"
    print(f"Parsing invalid coordinates: {str_coords}")
    try:
        _ = Vec3.from_str(str_coords)
    except CoordError as ce:
        orig = ce.__cause__
        if orig is None:
            print(f"Error parsing coordinates: {ce}")
            print(
                f"Error details - Type: {ce.__class__.__name__}, "
                f"Args: {ce.args}"
            )
        else:
            print(f"Error parsing coordinates: {orig.args[0]}")
            print(
                f"Error details - Type: {orig.__class__.__name__}, "
                f"Args: {orig.args}"
            )
    finally:
        p = Player(origin)
        p.teleport(new)
        print(p)


def get_args_i() -> tuple[int, list[int]]:
    """Parse CLI integer arguments.

    Skips `sys.argv[0]`. Each argument is stripped from common bracket/tuple
    punctuation to support inputs like "(1,2,3)".

    Returns:
        A tuple of:
            - argc: number of parsed integers
            - argv: list of parsed integers
    """
    av = sys.argv
    r_lst: list[int] = []
    for a in av[1:]:
        try:
            r_lst.append(int(a.strip(",'][()")))
        except (ValueError, TypeError) as exc:
            print(f"oops, I typed ’{a}’ instead of ’1000’ -- {exc}")
    return (len(r_lst), r_lst)


def main() -> None:
    """Program entrypoint.

    Behavior:
        - If <= 1 integer is provided, run the demo.
        - Otherwise, interpret integers by groups of 3 as `(x, y, z)` vectors.
    """
    ac, av = get_args_i()
    print("=== Game Coordinate System ===")
    if ac <= 1:
        first_start()
        return

    print(f"Total arguments: {ac}")
    i = 0
    coord_list: list[Vec3] = []
    while i < ac:
        coord_list += [Vec3(av[i], av[i + 1], av[i + 2])]
        i += 3
    print(coord_list)


if __name__ == "__main__":
    main()
