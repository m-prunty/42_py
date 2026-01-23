#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 02:21:53 by potz             #+#    #+#              #
#    Updated: 2026/01/23 11:41:09 by potz            ###   ########.fr        #
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


class Vec3():
    """Class for storing 3D Coords."""

    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        """TODO: to be defined."""
        self.x = 0
        self.y = 0
        self.z = 0
        try:
            self.x = x
            self.y = y
            self.z = z
        except Exception as e:
            print(e)
         #   raise ValueError(e)

    def __add__(self, other):
        """Adds a vec3 instance with another."""
        return Vec3(self.x + other.x,
                    self.y + other.y,
                    self.z + other.z,
                    )
    
    def __sub__(self, other):
        """Subs a vec3 instance with another."""
        return Vec3(self.x - other.x,
                    self.y - other.y,
                    self.z - other.z,
                    )
     
    def __abs__(self):
        """Returns magnitude of a vector."""
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __repr__(self):
        """Return a tuple represantation of a Vec3 instance."""
        return (self.x, self.y, self.z)
    
    def __str__(self):
        """Return a str tuple represantation of a Vec3 instance."""
        return f"{self.__repr__()}" 
    
    def __iter__(self):
        """Return a str tuple represantation of a Vec3 instance."""
        return iter(self.__repr__())
    
    @property
    def x(self) -> int:
        """doc"""
        return self._x
    
    @x.setter
    def x(self, value: int):
        try:
            self._x = int(value)
        except ValueError as ve:
            print(f"Error parsing coordinates: {ve}")
            self._x = 0 
            raise ValueError(ve)
    
    @staticmethod
    def ft_split(string: str, char: str):
        """TODO: Docstring for ft_split.
        Returns: TODO

        """
        i = 0
        j = 0
        l = len(string)
        r_list = []
        while i < l:
            while i < l and string[i] == char[0]:
                i += 1
            if i < l and string[i] != char[0]:
                if char not in string[i:]:
                    j = l
                else:
                    j = i
                    while j < l and string[j] != char[0]:
                        j += 1
                r_list += [string[i:j]] 
                i += j - i
        return r_list
    
    @classmethod
    def from_str(cls, coord: str) -> "Vec3":
        """TODO: Docstring for from_str.

        Args:
            coord (str): coordinates in form "x,y,z"

        Returns: An instance of Vec3

        """
        try:
            lst = [0]
            lst += cls.ft_split(coord, ",")
            lst = cls.parse_args(len(lst), lst)
            return cls(lst[0], lst[1], lst[2])
        except Exception as e:
            print(f"Error details - Type: {e.__class__.__name__}", end='')
            print(f", Args: (\"{e.args[0]}\",)")

    
    @classmethod
    def assign_coord(cls, lst: list[int]):
        """TODO: Docstring for assign_coord.

        Args:
            lst (list [int]): TODO

        Returns: TODO

        """
        
        print(len(lst), lst)
        try:
            if len(lst) > 3:
               raise ValueError 
            cls.x: int = lst[0]
            cls.y: int = lst[1]
            cls.z: int = lst[2]
        except ValueError as ve:
            print(f"ierr>>>{ve}")
        except IndexError as ie:
            print(f"ierr>>>{ie}")
    
    @staticmethod
    def is_int(i: int):
        """TODO: Docstring for is_int.
        Returns: TODO

        """
        r_i = None
        try:
            r_i = int(i)
        except ValueError as ve:
            print(f"ierr>>>{ve}")

    
    @staticmethod
    def parse_args(ac: int, av: list) -> list[int]:
        """TODO: Docstring for get_args.

        Args:
            ac (int): TODO
            av (list):
        Returns: TODO

        """
        i = 1
        r_lst = []
        while i < ac:
            try:
                r_lst += [int(av[i])]
            except ValueError as ve:
                print(f"Error parsing coordinates: {ve}")
                raise ValueError(ve)
            i += 1
        return r_lst

class Player(object):

    """Docstring for Player. """

    def __init__(self, start_pos: Vec3):
        """TODO: to be defined. """
        self.pos = start_pos

    def __str__(self):
        r_str = ""
        i = 0
        while i :
           r_str += f"{self.pos[i]}"
           i += 1
        return r_str
    
    @property
    def pos(self) -> Vec3:
        """doc"""
        return self._pos
    
    @pos.setter
    def pos(self, value: Vec3):
        self._pos = value

    def teleport(self, to: Vec3):
        self.pos = to
    
        
def first_start():
    start_pos = Vec3(10, 20, 5)
    print(start_pos)
    origin = Vec3()
    print(abs(origin - start_pos))
    new = Vec3.from_str("3,4,0")
    print(new)
    new2 = Vec3.from_str("iabc,cds,asjkl")
    p = Player(origin)
    p.teleport(new)
    print(p)

def main():
    """TODO: Docstring for main.

    Returns: TODO

    """
    ac = len(sys.argv)
    av = []
    if ac <= 1:
        print("No arguments provided!")
        first_start()
    else:
        print(f"Total arguments: {ac}")
    # print(f"Program name: {sc}")


if __name__ == "__main__":
    main()
