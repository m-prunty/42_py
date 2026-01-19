#!/usr/bin/env python3

class Plant():
    do
    class MyClass(object):
    
        """Docstring for MyClass. """
    
        def __init__(self):
            """TODO: to be defined. """
            
    def __init__(self, name: str, height: int, age: int):
        self._err = 0
        self._name = name
        self._height = 0
        self._age = 0
        self._ability = ""

        print(f"Plant created: {self._name}")
        self.height = height
        self.age = age
        self._time = 1
        self._growrate = 1

    def grow(self):
        self.height += self._growrate * self._time  # (self.height % 2) + 1

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height: int):
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")
        else:
            self.print_err(
                    f"height {height}cm [REJECTED]", "Neg height rejected")

    @property
    def ability(self):
        return self._ability

    @ability.setter
    def ability(self, ability):
        self._ability = ability

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days old [OK]")
        else:
            self.print_err(f"Age {age} [REJECTED]", "Neg age rejected")

    def __str__(self):
        str = f"{self._name} ({self.ptype}): "
        if self.height:
            str += f"{self.height}cm, "
        if self.age:
            str += f"{self.age} days, "
        return str

    def print_err(self, operation: str, msg: str):
        print("")
        print(f"Invalid operation attempted: {operation}")
        print(f"Security: {msg}")
        print("")
        print(f"Current plant: {self}", end="")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, colour: str):
        super().__init__(name, height, age)
        self.colour = colour
        self.ptype = "Flower"

    def __str__(self):
        str = super().__str__()
        str += f"{self.colour} colour"
        return str

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, colour):
        self._colour = colour

    @property
    def ability(self):
        super()._ability = self.bloom()
        return self._ability

    def bloom(self):
        tmp = self.age * self.height
        str = ""
        if tmp < 750:
            str += (f"{self._name} is not ready to bloom yet")
        elif tmp < 3000:
            str += (f"{self._name} is blooming beautifully")
        else:
            str += (f"{self._name} is probably dead...")
        return str


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: str):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.ptype = "Tree"

    @property
    def trunk_diameter(self):
        return self._trunk_diameter

    @trunk_diameter.setter
    def trunk_diameter(self, trunk_diameter):
        self._trunk_diameter = trunk_diameter

    def __str__(self):
        str = super().__str__()
        if self.trunk_diameter:
            str += f"{self.trunk_diameter}cm diameter"
        return str

    def get_shade(self):
        tmp = (self.height * self._trunk_diameter) * (1/12) * self.age
        tmp = ((tmp / 100000) * 2) + 2
        if tmp < 3000:
            print(f"{self._name} provides {int(tmp)} square meters of shade")
        else:
            print(f"{self._name} is probably dead...")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.ptype = "Vegetable"
        self.harvest_season = harvest_season

    def __str__(self):
        str = super().__str__()
        str += f"{self.harvest_season} harvest"
        return str

    @property
    def harvest_season(self):
        return self._harvest_season

    @harvest_season.setter
    def harvest_season(self, harvest_season):
        self._harvest_season = harvest_season

    def nutrional_value(self):
        tmp = self.age * self.height
        if tmp < 7200:
            print(f"{self._name} is not ripe yet")
        elif tmp < 10000:
            print(f"{self._name} is rich in vitamin C")
        else:
            print(f"{self._name} is probably dead...")

# def _age_pants(plnt: SecurePlant, days: int):
#    plnt
# def _from_dict(key: str, val: tuple)->SecurePlant:


class Garden():
    def __init__(self, plants: list):
        self.plants = []
        for plant in plants:
            self.add_ele(plant)
        self.n = self.plants.__len__()
        self.day = 1

    def add_ele(self, plant: Plant):
        if plant.height and plant.age:
            self.plants.append(plant)
        else:
            print("error")

    def pass_time(self, days):
        self.day = days
        for plant in self.plants:
            plant.time = self.day
            plant.age()
            plant.grow()

    def print_garden(self):
        print(f"=== Day {self.day} ===")
        for plant in self.plants:
            print(plant)

    def ex5(self):
        for plant in self.plants:
            print(plant)
            print(plant.ability)

    def ex5_test(self):
        self.plants[0].bloom()
        self.plants[0].height = 30
        self.plants[0].bloom()
        self.plants[0].age = 99
        self.plants[0].bloom()
        print("")
        self.plants[1].get_shade()
        self.plants[1].age = 1825
        self.plants[1].height = 500
        self.plants[1].get_shade()
        self.plants[1].age += 1825*20
        self.plants[1].get_shade()
        print(self.plants[1])
        print()
        self.plants[2].nutrional_value()
        self.plants[2].height = 100
        self.plants[2].nutrional_value()
        self.plants[2].age = 100
        self.plants[2].nutrional_value()
        print("")

    def verify(self):
        for p in self.plants:
            print(f"Created: {p}")
        print("")
        print(f"Total plants created: {self.n}")


def build_dict() -> dict:
    return {
        "Rose": ("Flower", 25, 30, "red"),
        "Oak": ("Tree", 500, 1825, 50),
        "Cactus": ("Vegetable", 80, 90, "summer"),
        }


def plant_factory(plant_dict: dict) -> list:
    r_list = []
    for k, v in plant_dict.items():
        if v[0] == "Flower":
            r_list.append(Flower(k, v[1], v[2], v[3]))
        elif v[0] == "Tree":
            r_list.append(Tree(k, v[1], v[2], v[3]))
        elif v[0] == "Vegetable":
            r_list.append(Vegetable(k, v[1], v[2], v[3]))
    return r_list


def main():
    print("=== Garden Plant Types ===")
    p_dict = build_dict()
    garden = Garden(plant_factory(p_dict))
    # garden.verify()
    garden.ex5()

# def _age_pants(plnt: SecurePlant, days: int):
#    plnt
# def _from_dict(key: str, val: tuple)->SecurePlant:


if __name__ == "__main__":
    main()
