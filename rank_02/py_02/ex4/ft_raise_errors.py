#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_raise_errors.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 02:01:28 by maprunty         #+#    #+#              #
#    Updated: 2026/01/22 07:10:11 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Intro to the finally block."""


class PlantError(ValueError):
    """Docstring for PlantError."""

    def __init__(self, *args: str):
        """TODO: to  tebe defined."""
        super().__init__(*args)


class NoneNameError(PlantError):
    """Docstring for WaterError."""

    def __init__(self):
        """TODO: to  tebe defined."""
        super().__init__("Plant name cannot be empty!")


class WaterError(PlantError):
    """Docstring for WaterError."""

    def __init__(self, water_level):
        """TODO: to  tebe defined."""
        if water_level > 10:
            super().__init__(f"Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            super().__init__(f"Water level {water_level} is too low (min 1)")


class SunError(PlantError):
    """Docstring for SunError."""

    def __init__(self, sun_hours):
        """TODO: to  tebe defined."""
        if sun_hours > 12:
            super().__init__(f"Sunlight hours {sun_hours} is too high(max 12)")
        elif sun_hours < 2:
            super().__init__(f"Sunlight hours {sun_hours} is too low (min 2)")


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
    except ValueError as e:
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
