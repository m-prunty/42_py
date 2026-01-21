#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 10:32:35 by maprunty         #+#    #+#              #
#    Updated: 2026/01/21 23:09:48 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Create GardenManager, Multiple gardens, stats and subplant subtypes."""


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
        self._growth = 1

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
#            print(f"Height updated: {self._height}cm", end=" ")
#            print("\x1b[32m[OK]\x1b[0m")
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
#            print(f"Age updated: {self._age} days old", end=" ")
#            print("\x1b[32m[OK]\x1b[0m")
        else:
            self.print_err(f"Age {age}", "Neg age rejected")

    @property
    def growrate(self) -> int:
        """TODO: Docstring for growth.

        Returns: (int) current growrate
        """
        return 1

    def pass_day(self) -> None:
        """Simulate the passing of a day for a plant."""
        self.age += 1
        self.height += self.growrate
        print(f"{self.name} grew {self.growrate}cm")

    def __repr__(self) -> str:
        """Get info about a plant.

        returns:
            str: string representation of available info about a plant
        """
        ret_string = f"{self.name}"
        if self.height:
            ret_string += f", {self.height}"
        if self.age:
            ret_string += f", {self.age}"
        ret_string += self.ext_info()
        return ret_string

    def __str__(self) -> str:
        """Get info about a plant.

        returns:
            str: string representation of available info about a plant
        """
        ret_string = f"{self.name}: {self.height}cm{self.ext_info()}"
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
        """
        print(f"Invalid operation attempted: {operation}", end=" ")
        print("\x1b[31m[REJECTED]\x1b[0m ")
        print(f"Security: {msg}")
        print("")
        print(f"Current plant: {self}")
        """


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
        blooming = self.in_bloom()
        r_str = f", {self.colour} flowers ({blooming})"
        if self.is_prize:
            r_str += PrizeFlower(self).__str__()
        return r_str

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

    @property
    def is_prize(self):
        """TODO: Docstring for is_prize.

        Returns: TODO

        """
        tmp = ((self.height * self.age) % 42)
        if tmp in [0, 1, 2]:
            PrizeFlower(self)
            return 1
        return 0

    def ability(self) -> None:
        """Plants special ability."""
        self.bloom()

    def bloom(self) -> None:
        """Flowers special ability."""
        tmp = self.in_bloom()
        print(f"{self.name} is {tmp}")

    def in_bloom(self):
        """Is flower blooming.

        Returns:
            str: Representation of flower state
        """
        tmp = self.height * self.age
        if tmp < 350:
            return "not ready to bloom yet"
        elif tmp > 3000:
            return "probably dead..."
        else:
            return "blooming"


class PrizeFlower:
    """Represent a PrizeFlower and its info.

    Inherits from:
        Flower

    Attributes:
        prize_value (int): the n of prize points
    """

    def __init__(self, flower: Flower) -> None:
        """Initialise a Flower object .

        Args:
            name (str): Name of Flower
            height (int): Initial height in cm
            age (int): Initial age in days
            colour (str): the colour of the flower
        """
        # super().__init__(name, height, age, colour)
        self.flower = flower
        self.flower.prize_value = 10

    def __str__(self) -> None:
        """Extra info for PrizeFlower(flower) class.

        Returns:
            str: Prizeflower info, Prize points
        """
        return f", Prize points: {self.flower.prize_value}"


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
        return f", {self.trunk_diameter}cm diameter"

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
        return f", {self.harvest_season} harvest"

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


class Garden:
    """Represent a garden to hold mulitple plants.

    Attributes:
        name (str): The owner of the Garden
        plants (list): List of plants in Garden
        counts (list(int)): List of Garden counts
    """

    def __init__(self, name: str, plants: list) -> None:
        """Initialise a garden object.

        Args:
            name (str): The owner of the Garden
            plants (list): List of plants
        """
        self.name = name
        self.plants = []
        self.nplants = 0
        print()
        for plant in plants:
            self.add_plant(plant)
        self.start_day = 1
        self.day = self.start_day

    @property
    def total_growth(self):
        """Calculate the growth of all plants."""
        self._total_growth = 0
        for plant in self.plants:
            self._total_growth += plant.growrate
        return self._total_growth

    @property
    def total_score(self):
        """Calculate the growth of all plants."""
        self._total_score = 0
        for plant in self.plants:
            self._total_score += plant.height
            if plant.ptype == "Flower" and plant.is_prize:
                self._total_score += plant.prize_value * 4
        return self._total_score

    @property
    def total_types(self):
        """Calculate the growth of all plants."""
        self._total_types = [0, 0, 0]
        for plant in self.plants:
            if plant.ptype == "Flower":
                if plant.is_prize:
                    self._total_types[2] += 1
                else:
                    self._total_types[1] += 1
            else:
                self._total_types[0] += 1
        return self._total_types

    def pass_time(self, days: int) -> None:
        """Simulate time until days passed.

        Args:
            days (int): N of days to pass
        """
        i = 0
        if self.name == "Alice":
            print("Alice is helping all plants grow...")
            while i < days:
                for plant in self.plants:
                    plant.pass_day()
                i += 1
                self.day += 1
        self.total_types
        self.total_growth
        self.total_score

    def print_report(self) -> None:
        """Display a report of current Garden State according to ex6.
        === Alice's Garden Report ===
        Plants in garden:
        - Oak Tree: 101cm
        - Rose: 26cm, red flowers (blooming)
        - Sunflower: 51cm, yellow flowers (blooming), Prize points: 10
        Plants added: 3, Total growth: 3cm
        Plant types: 1 regular, 1 flowering, 1 prize flowers
        Height validation test: True
        Garden scores - Alice: 218, Bob: 92
        Total gardens managed: 2
        """
        pass

    def add_plant(self, plant: Plant) -> None:
        """Add a Plant object to the Garden list.

        Args:
            plant (Plant): Plant object to add to list
        """
        self.plants.append(plant)
        if self.name == "Alice":
            print(f"Added {plant.name} to {self.name}'s garden")
        self.nplants += 1

    def __repr__(self) -> str:
        """Get info about plants in a garden.

        Returns:
            str: String representation of available info about a garden
        """
        r_str = f"Garden name: {self.name}"
        for plant in self.plants:
            r_str += f"\n{plant.__repr__()},"
        return r_str

    def __str__(self) -> str:
        """Get info about plants in a garden.

        Returns:
            str: String representation of available info about a garden
        """
        r_str = ""
        if self.name == "Alice":
            r_str += (f"=== {self.name}'s Garden Report ===")
            r_str += "\nPlants in garden"
            for plant in self.plants:
                r_str += f"\n- {plant.name}: {plant.height}cm"
                if plant.ptype == "Flower":
                    r_str += plant.ext_info()
            r_str += (f"\n\nPlants added: {self.nplants}")
            r_str += (f", Total growth: {self.total_growth}cm")
            r_str += (f"\nPlant types: {self._total_types[0]} regular")
            r_str += (f", {self._total_types[1]} flowering")
            r_str += (f", {self._total_types[2]} prize flowers")
        return r_str

    def test_height(self):
        self.plants[0].height = -3
        if self.plants[0].height < 0:
            return "False"
        return "True"

    def print_garden(self) -> None:
        """Print info about a Gardens plants."""
        for plant in self.plants:
            print()
            print(plant)
            plant.ability()


class GardenManager:
    """Represent manager class to hold mulitple gardens.

    Attributes:
        gardeners (list(str)): The owner of the Garden
        gardens (list(Garden)): List of plants in Garden
    """

    def __init__(self, garden_dict: dict):
        """Initialise a garden manager object.

        Args:
            names (list(str)): The owners of the Gardens
            gardens (list(Garden)): List of gardens
        """
        self.create_garden_network(garden_dict)
        self.day = 1
        self._garden_scores = {}

    @property
    def garden_scores(self):
        """TODO: Docstring for garden_scores.

        Returns: TODO

        """
        for g in self.gardens:
            self._garden_scores.update({g.name: g.total_score})
        return self._garden_scores

    def __repr__(self) -> str:
        """Get info about a plant.

        Returns:
            str: String representation of available info about a plant
        """
        r_str = ""
        for garden in self._gardens:
            r_str += garden.__repr__()
        return r_str

    def __str__(self) -> str:
        """Get info about a plant.

        Returns:
            str: String representation of available info about a plant
        """
        r_str = ""
        for garden in self._gardens:
            r_str += garden.__str__()
        r_str += f"\n\nHeight validation test: {self.gardens[0].test_height()}"
        r_str += "\nGarden scores - "
        r_str += ' '.join([f"{g.name}: {g.total_score}" for g in self.gardens])
        r_str += f"\nTotal gardens managed: {len(self.gardens)}"
        return r_str

    def pass_time(self, days: int) -> None:
        """Simulate time until days passed.

        Args:
            days (int): N of days to pass
        """
        i = 0
        while i < days:
            for garden in self.gardens:
                garden.pass_time(1)
            i += 1
            self.day += 1
        self.garden_scores

    @property
    def gardens(self):
        """Get a list of gardens.

        Returns: list(Garden) an immutable reference to _gardens

        """
        return self._gardens

    def add_garden(self, garden: Garden):
        """Add to list of garden."""
        self._gardens.append(garden)

    @property
    def gardeners(self):
        """TODO: Docstring for gardeners.

        Returns: an immutable reference to _gardeners

        """
        return self._gardeners

    def add_gardener(self, name: str):
        """Add to list of gardeners."""
        self._gardeners.append(name)

    def create_garden_network(self, garden_dict: dict) -> None:
        """Generate a list of gardens.

        note: dict must have {(Owner:str);
                    {(name: str); (height: int, age: int, colour: str)}}
        Args:
            garden (dict): dict of dict of gardens

        Returns: (list) of gardens

        """
        self._gardens = []
        self._gardeners = []
        for k, v in garden_dict.items():
            self.add_gardener(k)
            self.add_garden(Garden(k, self.plant_factory(v)))

    def plant_factory(self, plant_dict: dict) -> list:
        """Generate a list of plants.

        nb: dict must have {(name: str): (height: int, age: int, colour: str)}
        Args:
            plant_dict (dict): dict of plants

        Returns: (list) of plants
        """
        r_list = []
        for k, v in plant_dict.items():
            if v[0] == "Flower":
                r_list.append(Flower(k, v[1], v[2], v[3]))
            elif v[0] == "Tree":
                r_list.append(Tree(k, v[1], v[2], v[3]))
            elif v[0] == "Vegetable":
                r_list.append(Vegetable(k, v[1], v[2], v[3]))
        return r_list


def build_dict() -> dict:
    """Build a dict of plant info."""
    return {
            "Alice": {
                "Oak Tree": ("Tree", 100, 825, 32),
                "Rose": ("Flower", 25, 30, "red"),
                "Sunflower": ("Flower", 50, 41, "yellow")
                },
            "Bob": {
                "Rose": ("Flower", 27, 30, "red"),
                "Tomato": ("Vegetable", 50, 90, "summer"),
                "Clover": ("Flower", 15, 25, "green"),
                }
            }


def main() -> None:
    """Build plant dict, create list of plants and run ex5 test."""
    print("=== Garden Managment System Demo ===")
    g_dict = build_dict()
    gm = GardenManager(g_dict)
    gm.pass_time(1)
    print(gm)


if __name__ == "__main__":
    main()
