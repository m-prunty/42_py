# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plot_area.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2025/12/28 17:31:13 by maprunty         #+#    #+#              #
#    Updated: 2025/12/28 17:34:33 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_plot_area() -> None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print(f"Plot area: {area}")


if __name__ == "__main__":
    ft_plot_area()
