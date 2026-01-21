#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_intro.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/17 08:12:07 by maprunty         #+#    #+#              #
#    Updated: 2026/01/21 21:02:06 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Print plant name height and age."""


def ft_garden_intro() -> None:
    """Print plant name height and age."""
    name = "Rose"
    height = 25
    age = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("=== End  of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
