#!/usr/bin/env python3

class SecurePlant():
    """
    doc
    """
    def __init__(self, name: str, height: int, age: int):
        self._err = 0
        self._name = name
        print(f"Plant created: {self._name}")
        self._set_height(height)
        self._set_age(age)
        self._time = 1
        self._growrate = 1

    def grow(self):
        self._height += self._growrate * self._time  # (self.height % 2) + 1

    def age(self):
        self._age += self._time

    def get_info(self):
        if self._name:
            print(f"{self._name}: ", end="")
        print("(", end="")
        if self._height:
            print(f"{self.get_height()}cm, ", end="")
        if self._age:
            print(f"{self.get_age()} days", end="")
        print(")")

    def print_err(self, operation: str, msg: str):
        print("")
        print(f"Invalid operation attempted: {operation}")
        print(f"Security: {msg}")
        print("Current plant: ", end="")
        self.get_info()

    def _set_height(self, height: int):
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")
        else:
            self.print_err(
                    f"height {height}cm [REJECTED]", "Neg height rejected")

    def _set_age(self, age: int):
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age}cm [OK]")
        else:
            self.print_err(f"Age {age} [REJECTED]", "Neg age rejected")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


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

    def add_ele(self, plant: SecurePlant):
        if plant.get_height() and plant.get_age():
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
            plant.get_info()

    def ex4(self):
        self.plants[0]._set_height(-5)
        print()

    def verify(self):
        for p in self.plants:
            print("Created: ", end='')
            p.get_info()
        print("")
        print(f"Total plants created: {self.n}", end='')


def build_dict() -> dict:
    return {
        "Rose": (25, 30),
        "Oak": (200, 365),
        "Cactus": (5, 90),
        }


def plant_factory(plant_dict: dict) -> list:
    r_list = []
    for k, v in plant_dict.items():
        r_list.append(SecurePlant(k, v[0], v[1]))
    return r_list


def main():
    print("=== SecurePlant Factory Output ===")
    p_dict = build_dict()
    garden = Garden(plant_factory(p_dict))
    garden.verify()
    garden.ex4()

# def _age_pants(plnt: SecurePlant, days: int):
#    plnt
# def _from_dict(key: str, val: tuple)->SecurePlant:


if __name__ == "__main__":
    main()
