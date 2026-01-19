#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_security.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 02:37:31 by potz             #+#    #+#              #
#    Updated: 2026/01/19 06:23:38 by potz            ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Create secure methods for getting and setting SecurePlant info."""


class SecurePlant:
    """Represent a plant and its info.

    Attributes:
        name (str): Name of plant
        _height (int): Height in cm
        _days (int): Age in days
        growrate (int): Growth in cm per day
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialise a SecurePlant object.

        Args:
            name (str): Name of plant
            height (int): Initial height in cm
            age (int): Initial age in days
        """
        self.name = name
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)
        self.growrate = 1

    def set_height(self, height: int) -> None:
        """Securely set a plants height."""
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height}cm", end=" ")
            print("\x1b[32m[OK]\x1b[0m")
        else:
            self.print_err(
                    f"height {height}cm", "Negative height rejected")

    def set_age(self, age: int) -> None:
        """Securely set a plants age."""
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days", end=" ")
            print("\x1b[32m[OK]\x1b[0m")
        else:
            self.print_err(f"Age {age}", "Negative age rejected")

    def get_height(self) -> int:
        """Get a plants height.

        Returns:
            int: The height of a plant
        """
        return self._height

    def get_age(self) -> int:
        """Get a plants age.

        Returns:
            int: The age of a plant
        """
        return self._age

    def get_info(self) -> str:
        """Get info about a plant.

        Returns:
            str: String representation of a plant
        """
        return (f"""{self.name}: ({self._height}cm, {self._age} days)""")

    def print_err(self, operation: str, msg: str) -> None:
        """Display an error.

        Args:
            operation (str): The operation that was attempted
            msg (str): The message to be printed
        """
        print("")
        print(f"Invalid operation attempted: {operation}", end=" ")
        print("\x1b[31m[REJECTED]\x1b[0m ")
        print(f"Security: {msg}")
        print("")
        print(f"Current plant: {self.get_info()}")


def ex4(plant: SecurePlant):
    """Attempt to set height to a negative value as per subject spec."""
    plant.set_height(-5)
    print()


def main():
    """Build plant dict, create list of plants and run ex4 test."""
    print("=== Garden Security System ===")
    p = SecurePlant("Rose", 25, 30)
    ex4(p)


if __name__ == "__main__":
    main()
