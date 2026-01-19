#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/17 12:46:23 by maprunty         #+#    #+#              #
#    Updated: 2026/01/19 02:35:31 by potz            ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Track how plants change and provide operations to modify their state."""


class Plant:
    """Represent a plant and its info.

    Attributes:
        name (str): Name of plant
        _height (int): Height in cm
        _days (int): Age in days
        growrate (int): Growth in cm per day
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialise a Plant object.

        Args:
            name (str): Name of plant
            height (int): Initial height in cm
            age (int): Initial age in days
        """
        self.name = name
        self._height = height
        self._days = age
        self.growrate = 1

    def grow(self) -> None:
        """Grows a plants height by growrate."""
        self._height += self.growrate

    def age(self) -> None:
        """Age a plant by one day."""
        self._days += 1

    def pass_day(self) -> None:
        """Simulate the passing of a day for a plant."""
        self.age()
        self.grow()

    def get_info(self) -> str:
        """Get info about a plant.

        Returns:
            str: String representation of a plant
        """
        return (f"""{self.name}: {self._height}cm, {self._days} days old""")


class Garden:
    """Represent a garden to hold mulitple plants.

    Attributes:
        plants (list): List of plants in Garden
        day (int): Number of days passed
        start_day (int): Day to start on
    """

    def __init__(self, plants: list[Plant]) -> None:
        """Initialise a garden object.

        Args:
            plants (list): List of plants
        """
        self.plants = []
        for plant in plants:
            self.add_plant(plant)
        self.start_day = 1
        self.day = self.start_day

    def add_plant(self, plant: Plant) -> None:
        """Add a Plant object to the Garden list.

        Args:
            plant (Plant): Plant object to add to list
        """
        self.plants.append(plant)

    def pass_time(self, days: int) -> None:
        """Simulate time until days passed.

        Args:
            days (int): N of days to pass
        """
        while self.day < days:
            for plant in self.plants:
                plant.pass_day()
            self.day += 1

    def print_garden(self) -> None:
        """Print info about a Gardens plants."""
        print(f"=== Day {self.day} ===")
        for plant in self.plants:
            print(plant.get_info())
            growth = (self.day - self.start_day) * plant.growrate
            if (growth):
                print(f"Growth this week: +{growth}cm")


def main() -> None:
    """Create a Garden, add Plants, and print the info."""
    plant_list = [Plant("Rose", 25, 30),
                  # Plant("Cactus", 10, 180),
                  # Plant("Tulip", 22, 26),
                  ]
    garden = Garden(plant_list)
    garden.print_garden()
    garden.pass_time(7)
    garden.print_garden()


if __name__ == "__main__":
    main()
