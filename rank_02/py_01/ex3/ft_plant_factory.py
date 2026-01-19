#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 00:36:38 by potz             #+#    #+#              #
#    Updated: 2026/01/19 01:27:59 by potz            ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Creat multiple Plant instances and verify."""


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
        return (f"""{self.name}: {self._height}cm, {self._days} days""")


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
        self.nplants = 0
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
        self.nplants += 1

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

    def verify(self):
        """Step through a gardens plant list and verify proper creation."""
        for p in self.plants:
            print("Created: ", end='')
            print(p.get_info())
        print("")
        print(f"Total plants created: {self.nplants}", end='')


def build_dict() -> dict:
    """Build a dict of plant info."""
    return {
        "Rose": (25, 30),
        "Oak": (200, 365),
        "Cactus": (5, 90),
        "Sunflower": (80, 45),
        "Fern": (15, 120),
        }


def plant_factory(plant_dict: dict) -> list[Plant]:
    """Generate a list of plants."""
    r_list = []
    for k, v in plant_dict.items():
        r_list.append(Plant(k, v[0], v[1]))
    return r_list


def main():
    """Build plant dict, create list of plants and verify."""
    print("=== Plant Factory Output ===")
    p_dict = build_dict()
    garden = Garden(plant_factory(p_dict))
    garden.verify()


if __name__ == "__main__":
    main()
