# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2025/12/28 21:08:36 by maprunty         #+#    #+#              #
#    Updated: 2025/12/28 21:46:29 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    unitdict = {"packets": f"{quantity} packets available",
                "grams": f"{quantity} grams total",
                "area": f"covers {quantity} square meters"
                }
    if unit in unitdict:
        unitstr = unitdict[unit]
    else:
        unitstr = "Unknown unit type"
    print(f"{seed_type.capitalize()}: {unitstr}")


if __name__ == "__main__":
    ft_seed_inventory("tomato", 15, "packets")
    ft_seed_inventory("carrot", 8, "grams")
    ft_seed_inventory("lettuce", 12, "area")
    ft_seed_inventory("lette", 12, "ar")
