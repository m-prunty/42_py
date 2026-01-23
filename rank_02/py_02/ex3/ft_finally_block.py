#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_finally_block.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 02:01:27 by maprunty         #+#    #+#              #
#    Updated: 2026/01/22 07:36:58 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Intro to the finally block."""


class Plant:
    """Represent a plant and its info.

    Attributes:
        name (str): Name of plant
        water_level (int): water_level in cm
    """

    def __init__(self, name: str, water_level: int) -> None:
        """Initialise a Plant object.

        Args:
            name (str): Name of plant
            water_level (int): Initial water_level in cm
            age (int): Initial age in days
        """
        self.name = name
        self.water_level = water_level


def water_plants(plant_list: list[Plant]) -> None:
    """Water a list of Plants."""
    print("Opening watering system")
    err = False
    try:
        for p in plant_list:
            if p.name:
                print(f"Watering {p.name}")
            else:
                raise Exception
        return
    except Exception:
        err = True
        print(f"Error: Cannot water {p.name} - invalid plant!")
        return
    finally:
        print("Closing watering system (cleanup)")
        if not err:
            print("Watering completed successfully!")


def test_watering_system() -> None:
    """Tests basic values of check_temperature()."""
    print("=== Garden Watering System ===")
    lst1 = [("tomato", 2), ("lettuce", 4), ("carrots", 3)]
    lst2 = []
    for e in lst1:
        lst2 += [Plant(e[0], e[1])]
    print("\nTesting normal watering...")
    water_plants(lst2)
    print("\nTesting with error...")
    lst2[1].name = None
    water_plants(lst2)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
