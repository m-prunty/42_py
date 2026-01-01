# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2025/12/28 19:00:42 by maprunty         #+#    #+#              #
#    Updated: 2025/12/28 19:04:19 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder() -> None:
    if (int(input("Days since last watering: ")) > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")


if __name__ == "__main__":
    ft_water_reminder()
