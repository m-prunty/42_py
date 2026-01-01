# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2025/12/28 19:08:21 by maprunty         #+#    #+#              #
#    Updated: 2025/12/28 19:15:44 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative() -> None:
    daze = int(input("Days until harvest: "))
    for i in range(1, daze + 1):
        print(f"Day {i}")
    print(f"Harvest time!")


if __name__ == "__main__":
    ft_count_harvest_iterative()
