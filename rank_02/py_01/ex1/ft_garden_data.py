#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/17 10:45:49 by maprunty         #+#    #+#              #
#    Updated: 2026/01/18 21:04:28 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Create an instance of plant and print the info."""


class Plant():
    """represent a plant and its info.

    Attributes:
        name (str): Name of plant
        height (int): height in cm
        age (int): age in days
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialise a Plant object.

        Args:
            name (str): Name of plant
            height (int): height in cm
            age (int): age in days

        """
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        """Print info about a plant."""
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age}days old")


def main() -> None:
    """Create a Plant and print the info."""
    rose = Plant("Rose", 25, 30)
    print("=== Garden Plant Registry ===")
    rose.print_info()


if __name__ == "__main__":
    main()
