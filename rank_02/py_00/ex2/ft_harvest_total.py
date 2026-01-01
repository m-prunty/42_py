# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2025/12/28 17:38:34 by maprunty         #+#    #+#              #
#    Updated: 2025/12/28 18:47:38 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total():
    i = 0
    tot = 0
    while (i := i + 1) <= 3:
        tot += int(input(f"Day {i} harvest: "))
    print(f"Total harvest: {tot}")


if __name__ == "__main__":
    ft_harvest_total()
