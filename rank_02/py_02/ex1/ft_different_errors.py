#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_different_errors.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 02:01:23 by maprunty         #+#    #+#              #
#    Updated: 2026/01/22 07:26:52 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""A first look at exceptions."""


def garden_operations(i: int):
    """TODO: Docstring for garden_operations.

    Returns: TODO

    """
    d = {}
    try:
        if i == "missing.txt":
            open(i)
        if i == "missing\\_plant":
            d[i]
        x = int(i)
        _ = 10/x
        if x == 4:
            try:
                x/0 and d[x]
            except (KeyError, ZeroDivisionError):
                print("Caught an error, but program continues!")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{i}'")
    except KeyError:
        print(f"Caught KeyError: '{i}'")


def test_error_types() -> None:
    """Tests basic values of check_temperature()."""
    test_vals = {
            "ValueError": "abc",
            "ZeroDivisionError": "0",
            "FileNotFoundError": "missing.txt",
            "KeyError": "missing\\_plant",
            "muliple errors together": "4"}
    print("=== Garden Error Types Demo ===")
    for k, v in test_vals.items():
        print(f"\nTesting {k}...")
        garden_operations(v)
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
