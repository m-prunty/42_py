# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_summary.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2025/12/28 20:59:04 by maprunty         #+#    #+#              #
#    Updated: 2025/12/28 21:06:50 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_garden_summary():
    name = str(input("Enter garden name: "))
    n = int(input("Enter number of plants: "))
    print(f"Garden: {name}")
    print(f"Plants: {n}")
    print("Status: Growing well!")


if __name__ == "__main__":
    ft_garden_summary()
