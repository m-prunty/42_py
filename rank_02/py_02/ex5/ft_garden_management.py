#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_management.py                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 02:01:29 by maprunty         #+#    #+#              #
#    Updated: 2026/01/26 11:43:08 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""
• Has methods to add plants, water plants, and check plant health
• Uses your custom error types from previous exercises
• Handles different types of errors appropriately
• Uses try/except/finally blocks where needed
• Raises its own errors when something is wrong
• Keeps working even when some operations fail
"""


class Plant:
    """Represent a plant and its info.

    Attributes:
        name (str): Name of plant
        water_level (int): water_level in cm
        sun (int): sun hrs recieved
    """

    def __init__(self, name: str, water_level: int, sun: int) -> None:
        """Initialise a Plant object.

        Args:
            name (str): Name of plant
            water_level (int): Initial water_level in cm
            sun (int): sun hrs recieved
        """
        try:
            self.name = name
            if not self.name:
                raise NoneNameError
            print(f"Added {self.name} successfully")
        except NoneNameError:
            raise NoneNameError
        self.water_level = water_level
        self.sun = sun

    @property
    def water_level(self) -> int:
        """Get a plants water_level.

        Returns:
            int: The water_level of a plant
        """
        return self._water_level

    @water_level.setter
    def water_level(self, water_level: int) -> None:
        """Securely set a plants water_level."""
        try:
            self._water_level = water_level
        except WaterError:
            raise WaterError


class GardenManager:
    """Docstring for . """

    def __init__(self):
        """TODO: to be defined. """
        self.plants = []
        self.tank = 14

    def check_garden(self):
        try:
            if self.tank < 5:
                raise GardenError("Not enough water in tank")
        except GardenError as ge:
            print(f"Caught GardenError: {ge}")

    def add_plant(self, name: str, water_level: int, sun: int) -> None:
        try:
            self.plants += [Plant(name, water_level, sun)] 
        except NoneNameError as e:
            print(f"Error adding plant: {e}")

    def check_plant_health(self) -> None:
        """Check a self.plants health."""
        for p in self.plants:
            try:
                if not p:
                    raise NoneNameError()
                if p.water_level > 10 or p.water_level < 0:
                    raise WaterError(p.water_level)
                if p.sun > 12 or p.sun < 2:
                    raise SunError(p.sun)
                print(f"{p.name} (water: {p.water_level}, sun: {p.sun})")
            except PlantError as e:
                print(f"Error checking {p.name}: {e} ")

    def water_plants(self) -> None:
        """Water a list of self.Plants."""
        print("Opening watering system")
        try:
            for p in self.plants:
                print(f"Watering {p.name}", end=' - ')
                p.water_level += 5
                self.tank -= 5
                print("success")
        except Exception as e:
            print(f"Error: Cannot water {p.name} - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")


class GardenError(ValueError):
    """Base Garden class type for all garden value errors."""
    
    def __init__(self, *args: str):
        """Initialise a generic garden error."""
        super().__init__(*args)

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


def main() -> None:
    """Tests basic values of check_temperature()."""
    print("=== Garden Management System ===")
    g = GardenManager()
    print("\nAdding plants to garden...")
    g.add_plant("tomato", 0, 8)
    g.add_plant("lettuce", 10, 8)
    g.add_plant("", 7, 8)
    
    print("\nWatering plants...")
    g.water_plants()
    
    print("\nChecking plant health...")
    g.check_plant_health()

    print("\nTesting error recovery..")
    g.check_garden()
    print("System recovered and continuing...")

    print("\nGarden management system test complete!")

if __name__ == "__main__":
    main()
