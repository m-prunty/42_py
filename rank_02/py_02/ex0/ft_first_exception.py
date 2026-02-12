#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_first_exception.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 00:44:03 by maprunty         #+#    #+#              #
#    Updated: 2026/01/27 17:52:17 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Exercise 0: Agricultural Data Validation Pipeline.

A first look at exceptions.
"""


def check_temperature(temp_str: str) -> int | None:
    """Check if the temperature is reasonable for plants.

    Returns:
        int | None : Value of temp if optimal, otherwise None

    Raises:
        ValueError: if not an int or tmep is not optimal
    """
    min_val = 0
    max_val = 40
    temp = None
    try:
        temp = int(temp_str)
        if min_val > temp:
            raise ValueError(f"is too cold (min {min_val}°C)")
        elif max_val < temp:
            raise ValueError(f"is too hot (max {max_val}°C)")
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp
    except ValueError as ve:
        if temp is not None:
            print(f"Error: {temp}°C {ve}")
        else:
            print(f"Error: '{temp_str}' is not a valid number")
    return None


def test_temperature_input() -> None:
    """Tests basic values of check_temperature()."""
    test_vals = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===")
    for t in test_vals:
        print(f"\nTesting temperature: {t}")
        check_temperature(t)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
