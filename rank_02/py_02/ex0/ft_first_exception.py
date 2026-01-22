#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_first_exception.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 00:44:03 by maprunty         #+#    #+#              #
#    Updated: 2026/01/22 02:33:19 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""A first look at exceptions."""


def check_temperature(temp_str: str) -> int | None:
    """Check if the temperature is reasonable for plants.

    Returns:
        int : Value of temp if optimal

    Raises:
        ValueError if not an int or tmep is not optimal
    """
    min_val = 0
    max_val = 40
    temp = None
    try:
        temp = int(temp_str)
        if min_val > temp or temp > max_val:
            raise ValueError
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp

    except ValueError:
        if temp:
            if temp <= min_val:
                print(f"Error: {temp}°C is too cold (min {min_val})°C")
            if temp >= max_val:
                print(f"Error: {temp}°C is too hot (max {max_val})°C")
        else:
            print(f"Error: '{temp_str}' is not a valid number")


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
