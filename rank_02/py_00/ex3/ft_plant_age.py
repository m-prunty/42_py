# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2025/12/28 18:52:01 by maprunty         #+#    #+#              #
#    Updated: 2025/12/28 18:58:29 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_plant_age() -> None:
    if (int(input("Enter plant age in days: ")) > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")


if __name__ == "__main__":
    ft_plant_age()
