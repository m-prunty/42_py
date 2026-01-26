#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_raise_errors.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 02:01:28 by maprunty         #+#    #+#              #
#    Updated: 2026/01/26 08:18:26 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Exercise 4: Raising Your Own Errors.

A look at raise keyword and rasing custom Errors.
"""


class PlantError(ValueError):
    """Base Exception class type for all plant value errors."""

    def __init__(self, *args: str):
        """Initialise a generic garden error."""
        super().__init__(*args)


class NoneNameError(PlantError):
    """Name error for all name based Garden errors."""

    def __init__(self):
        """Initialise a name type garden error."""
        super().__init__("Plant name cannot be empty!")


class WaterError(PlantError):
    """Water error for all water based Garden errors."""

    def __init__(self, water_level):
        """Initialise a water type garden error."""
        msg = f"Water level {water_level} is too "
        if water_level > 10:
            msg += "high (max 10)"
        elif water_level < 1:
            msg += "low (min 1)"
        super().__init__(msg)


class SunError(PlantError):
    """Sun error for all Sun based Garden errors."""

    def __init__(self, sun_hours):
        """Initialise a sun type garden error."""
        msg = f"Sunlight hours {sun_hours} is too "
        if sun_hours > 12:
            msg += "high(max 12)"
        elif sun_hours < 2:
            msg += "low (min 2)"
        super().__init__(msg)


def check_plant_health(plant_name, water_level, sunlight_hours) -> None:
    """Check a plants health."""
    try:
        if not plant_name:
            print("\nTesting empty plant name...")
            raise NoneNameError()
        if water_level > 10 or water_level < 0:
            print("\nTesting bad water level...")
            raise WaterError(water_level)
        if sunlight_hours > 12 or sunlight_hours < 2:
            print("\nTesting bad sunlight hours...")
            raise SunError(sunlight_hours)
        print("\nTesting good values...")
        print(f"Plant {plant_name} is healthy!")
    except PlantError as e:
        print(f"Error: {e} ")


def test_plant_checks() -> None:
    """Tests basic values of check_temperature()."""
    print("=== Garden Plant Health Checker ===")
    check_plant_health("Tomato", 7, 7)

    check_plant_health(None, 3, 7)
    check_plant_health("Tomato", 15, 7)
    check_plant_health("Tomato", 4, 0)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
