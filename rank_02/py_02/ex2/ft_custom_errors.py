#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 02:01:26 by maprunty         #+#    #+#              #
#    Updated: 2026/01/26 09:25:07 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Exercise 2: Making Your Own Error Types.

A look at custom Error types
"""


class Plant:
    """Represent a plant and its info.

    Attributes:
        name (str): Name of plant
        water_level (int): water_level in cm
    """

    def __init__(self, name: str, water_level: int) -> None:
        """Initialise a Plant object.

        Args:
            name (str): Name of plant
            water_level (int): Initial water_level in cm
        """
        self.name = name
        self.water_level = water_level

    @property
    def water_level(self) -> int:
        """Get a plants water_level.

        Returns:
            int: The water_level of a plant
        """
        if self._water_level < 3:
            raise PlantError(self.name)
        return self._water_level

    @water_level.setter
    def water_level(self, water_level: int) -> None:
        """Securely set a plants water_level."""
        try:
            if water_level >= 0:
                self._water_level = water_level
            else:
                raise WaterError
        except ValueError:
            print(f"water_level {water_level}cm Negative water_level rejected")


class GardenError(Exception):
    """Base Exception class type for all Garden errors."""

    def __init__(self, args):
        """Initialise a generic garden error."""
        super().__init__(args)


class PlantError(GardenError):
    """Plant error for all plant based Garden errors."""

    def __init__(self, plant_name: str):
        """Initialise a plant type garden error."""
        self.name = plant_name
        super().__init__(f"The {plant_name} is wilting!")


class WaterError(GardenError):
    """Water error for all water based Garden errors."""

    def __init__(self):
        """Initialise a water type garden error."""
        super().__init__("Not enough water in the tank!")


def test_error_types() -> None:
    """Tests basic values of check_temperature()."""
    print("=== Custom Garden Errors Demo ===")
    a = Plant("Tomato plant", 2, 30)
    try:
        print(a.water_level)
    except Exception as e:
        print(f"\nTesting {e.__class__.__name__}...")
        print(f"Caught {e.__class__.__name__}: {e}")

    try:
        a.water_level = -1
    except Exception as e:
        print(f"\nTesting {e.__class__.__name__}...")
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting catching all garden errors......")
    try:
        print(a.water_level)
    except GardenError as ge:
        print(f"Caught GardenError: {ge}")
    try:
        a.water_level = -1
    except GardenError as ge:
        print(f"Caught GardenError: {ge}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
