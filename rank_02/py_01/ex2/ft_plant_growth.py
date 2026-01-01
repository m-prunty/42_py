#!/usr/bin/env python3

# l:k

class Plant():
    time = 1

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self):
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age}days old")

    def grow(self):
        self.height += self.growrate  # (self.height % 2) + 1

    def age(self):
        self.age += 1

    def get_info(self):
        self.height += self.time
        self.age += self.time


# def _age_pants(plnt: Plant, days: int):
#    plnt


def run_prg():
    days = 1
    print(f"=== Day {days} ===")
    rose = Plant("Rose", 25, 30)
    rose.print_info()
    rose.time = 7
    rose.get_info()
    rose.print_info()


if __name__ == "__main__":
    run_prg()
