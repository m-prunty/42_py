#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: potz <maprunty@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 06:25:32 by potz             #+#    #+#              #
#    Updated: 2026/01/19 10:21:29 by potz            ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Create Specialised Plant types and their corresponding info."""


class Plant:
    """Represent a plant and its info.

    Attributes:
        name (str): Name of plant
        height (int): Height in cm
        age (int): Age in days
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
        self.height = height
        self.age = age
        self._growrate = 1

    def ability(self) -> None:
        """Plants special ability."""
        print("This plant has no special action.")

    @property
    def ptype(self) -> str:
        """Get Plant type.

        Returns:
            str: Plant type from class name
        """
        return self.__class__.__name__

    @property
    def height(self) -> int:
        """Get a plants height.

        Returns:
            int: The height of a plant
        """
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        """Securely set a plants height."""
        if height >= 0:
            self._height = height
            # print(f"Height updated: {self._height}cm", end=" ")
            # print("\x1b[32m[OK]\x1b[0m")
        else:
            self.print_err(
                    f"height {height}cm", "Neg height rejected")

    @property
    def age(self) -> int:
        """Get a plants age.

        Returns:
            int: The age of a plant
        """
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        """Securely set a plants age."""
        if age >= 0:
            self._age = age
            # print(f"Age updated: {self._age} days old", end=" ")
            # print("\x1b[32m[OK]\x1b[0m")
        else:
            self.print_err(f"Age {age}", "Neg age rejected")

    def __str__(self) -> str:
        """Get info about a plant.

        Returns:
            str: String representation of available info about a plant
        """
        ret_string = f"{self.name} ({self.ptype}): "
        if self.height:
            ret_string += f"{self.height}cm, "
        if self.age:
            ret_string += f"{self.age} days, "
        ret_string += self.ext_info()
        return ret_string

    def ext_info(self) -> str:
        """Get extra info specific to a Plant type.

        Returns:
            str: Plant specific info
        """
        return ""

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
        print(f"Current plant: {self}")


class Flower(Plant):
    """Represent a Flower and its info.

    Inherits from:
        Plant

    Attributes:
        colour (str): the colour of a flower
    """

    def __init__(self, name: str, height: int, age: int, colour: str) -> None:
        """Initialise a Flower object.

        Args:
            name (str): Name of Flower
            height (int): Initial height in cm
            age (int): Initial age in days
            colour (str): the colour of the flower
        """
        super().__init__(name, height, age)
        self.colour = colour

    def ext_info(self) -> None:
        """Extra info for Flower(Plant) class.

        Returns:
            str: Plant info, Flower specific colour
        """
        return f"{self.colour} colour"

    @property
    def colour(self) -> str:
        """Get a flowers colour property.

        Returns:
            str: Flower colour
        """
        return self._colour

    @colour.setter
    def colour(self, colour) -> None:
        """Set a flowers colour property."""
        self._colour = colour

    def ability(self) -> None:
        """Plants special ability."""
        self.bloom()

    def bloom(self) -> None:
        """Flowers special ability."""
        tmp = self.age * self.height
        if tmp < 750:
            print(f"{self.name} is not ready to bloom yet")
        elif tmp < 3000:
            print(f"{self.name} is blooming beautifully")
        else:
            print(f"{self.name} is probably dead...")


class Tree(Plant):
    """Represent a Tree and its info.

    Inherits from:
        Plant

    Attributes:
        trunk_diameter (int): the trunk_diameter of a Tree
    """

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialise a Tree object.

        Args:
            name (str): Name of Tree
            height (int): Initial height in cm
            age (int): Initial age in days
            trunk_diameter (int): the trunk_diameter of the Tree
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def ext_info(self) -> str:
        """Extra info for Tree(Plant) class.

        Returns:
            str: Plant info, Tree specific trunk_diameter
        """
        return f"{self.trunk_diameter}cm diameter"

    @property
    def trunk_diameter(self) -> int:
        """Get a Trees trunk_diameter property.

        Returns:
            int: Tree trunk_diameter
        """
        return self._trunk_diameter

    @trunk_diameter.setter
    def trunk_diameter(self, trunk_diameter) -> None:
        """Set a Trees trunk_diameter property."""
        self._trunk_diameter = trunk_diameter

    def ability(self) -> None:
        """Plants special ability."""
        self.produce_shade()

    def produce_shade(self) -> None:
        """Trees special ability."""
        tmp = (self.height * self._trunk_diameter) * (1/12) * self.age
        tmp = ((tmp / 100000) * 2) + 2
        if tmp < 3000:
            print(f"{self.name} provides {int(tmp)} square meters of shade")
        else:
            print(f"{self.name} is probably dead...")


class Vegetable(Plant):
    """Represent a Vegetable and its info.

    Inherits from:
        Plant

    Attributes:
        harvest_season (int): the harvest_season of a Vegetable
    """

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str) -> None:
        """Initialise a Vegetable object.

        Args:
            name (str): Name of Vegetable
            height (int): Initial height in cm
            age (int): Initial age in days
            harvest_season (int): the harvest_season of the Vegetable
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def ext_info(self) -> str:
        """Extra info for Vegetable(Plant) class.

        Returns:
            str: Plant info, Vegetable specific harvest_season
        """
        return f"{self.harvest_season} harvest"

    @property
    def harvest_season(self) -> str:
        """Get a Vegetables harvest_season property.

        Returns:
            str: Vegetable harvest_season
        """
        return self._harvest_season

    @harvest_season.setter
    def harvest_season(self, harvest_season) -> None:
        """Set a Vegetables harvest_season property."""
        self._harvest_season = harvest_season

    def ability(self) -> None:
        """Plants special ability."""
        self.nutritional_value()

    def nutritional_value(self) -> None:
        """Vegetables special ability."""
        tmp = self.age * self.height
        if tmp < 7200:
            print(f"{self.name} is not ripe yet")
        elif tmp < 10000:
            print(f"{self.name} is rich in vitamin C")
        else:
            print(f"{self.name} is probably dead...")


class Garden():
    """Represent a garden to hold mulitple plants.

    Attributes:
        plants (list): List of plants in Garden
    """

    def __init__(self, plants: list) -> None:
        """Initialise a garden object.

        Args:
            plants (list): List of plants
        """
        self.plants = []
        for plant in plants:
            self.add_plant(plant)

    def add_plant(self, plant: Plant) -> None:
        """Add a Plant object to the Garden list.

        Args:
            plant (Plant): Plant object to add to list
        """
        self.plants.append(plant)

    def print_garden(self) -> None:
        """Print info about a Gardens plants."""
        for plant in self.plants:
            print()
            print(plant)
            plant.ability()


def build_dict() -> dict:
    """Build a dict of plant info."""
    return {
        "Rose": ("Flower", 25, 30, "red"),
        "Oak": ("Tree", 500, 1825, 50),
        "Tomato": ("Vegetable", 80, 90, "summer"),
        "Clover": ("Flower", 10, 25, "green"),
        "Beech": ("Tree", 300, 100, 30),
        "Squash": ("Vegetable", 60, 100, "autumn"),
        }


def plant_factory(plant_dict: dict) -> list:
    """Generate a list of plants."""
    r_list = []
    for k, v in plant_dict.items():
        if v[0] == "Flower":
            r_list.append(Flower(k, v[1], v[2], v[3]))
        elif v[0] == "Tree":
            r_list.append(Tree(k, v[1], v[2], v[3]))
        elif v[0] == "Vegetable":
            r_list.append(Vegetable(k, v[1], v[2], v[3]))
    return r_list


def main() -> None:
    """Build plant dict, create list of plants and run ex5 test."""
    print("=== Garden Plant Types ===")
    p_dict = build_dict()
    garden = Garden(plant_factory(p_dict))
    garden.print_garden()


if __name__ == "__main__":
    main()
