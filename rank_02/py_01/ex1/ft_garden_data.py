#!/usr/bin/env python3
# l:k

class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self):
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age}days old")


def run_prg():
    rose = Plant("Rose", 25, 30)
    print("=== Garden Plant Registry ===")
    rose.print_info()


if __name__ == "__main__":
    run_prg()
