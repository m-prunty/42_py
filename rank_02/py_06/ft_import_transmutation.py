#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_import_transmutation.py                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 14:18:26 by maprunty         #+#    #+#              #
#    Updated: 2026/02/22 15:41:02 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


def m1() -> None:
    """Method 1 - Full module import:."""
    import alchemy.elements

    print(m1.__doc__[:-1])
    pckg = "create_fire"
    try:
        fn = getattr(alchemy.elements, pckg)
        print(f"alchemy.elements.{pckg}(): {fn()}")
    except AttributeError:
        print(f"alchemy.elements.{pckg}(): AttributeError - not exposed")


def m2() -> None:
    """Method 2 - Specific function import:."""
    from alchemy.elements import create_water

    print(m2.__doc__[:-1])
    fn = create_water
    try:
        print(f"{fn.__name__}(): {fn()}")
    except AttributeError:
        print(f"{fn.__name__}(): AttributeError - not exposed")


def m3() -> None:
    """Method 3 - Aliased import:."""
    from alchemy.potions import healing_potion as heal

    print(m3.__doc__[:-1])
    try:
        print(f"heal(): {heal()}")
    except AttributeError:
        print(f"alchemy.elements.{heal}(): AttributeError - not exposed")


def m4() -> None:
    """Method 4 - Multiple imports:."""
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion

    print(m4.__doc__[:-1])
    f_list = [create_fire, create_earth, strength_potion]
    try:
        [print(f"{fn.__name__}(): {fn()}") for fn in f_list]
    except AttributeError as e:
        print(f"{e}: AttributeError - not exposed")


print("=== Import Transmutation Mastery ===")
print()
m1()
print()
m2()
print()
m3()
print()
m4()
print("\nAll import transmutation methods mastered")
