#!/usr/bin/env python3
# l:k

class Plant():
    time = 1

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self):
        print(f"{self.name.capitalize()}: ({self.height}cm, {self.age} days)")

    def grow(self):
        self.height += self.growrate  # (self.height % 2) + 1

    def age(self):
        self.age += 1

    def get_info(self):
        self.height += self.time
        self.age += self.time


# def _age_pants(plnt: Plant, days: int):
#    plnt
# def _from_dict(key: str, val: tuple)->Plant:

def plant_factory(plant_dict: dict) -> list:
    r_list = []
    for k, v in plant_dict.items():
        r_list.append(Plant(k, v[0], v[1]))
    return r_list


def build_dict() -> dict:
    return {
        "Rose": (25, 30),
        "Oak": (200, 365),
        "Cactus": (5, 90),
        }


def verify(plant_list: list):
    for p in plant_list:
        print("Created: ", end='')
        p.print_info()


def run_prg():
    print("=== Plant Factory Output ===")
    p_dict = build_dict()
    p_list = plant_factory(p_dict)
    verify(p_list)


if __name__ == "__main__":
    run_prg()
