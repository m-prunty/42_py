# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2025/12/28 19:08:21 by maprunty         #+#    #+#              #
#    Updated: 2025/12/28 20:57:45 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def _help_count_harvest_recursive(daze: int, day: int) -> None:
    if day <= daze:
        print(f"Day {day}")
        return _help_count_harvest_recursive(daze, day + 1)
    else:
        print(f"Harvest time!")
        return


def ft_count_harvest_recursive() -> None:
    daze = int(input("Days until harvest: "))
    _help_count_harvest_recursive(daze, 1)


if __name__ == "__main__":
    ft_count_harvest_recursive()
