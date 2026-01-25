#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/25 15:35:58 by maprunty         #+#    #+#              #
#    Updated: 2026/01/25 17:00:30 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Exercise 0: Ancient Text Recovery."""


def main():
    """Driver open file and print data."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    filename = "ancient_fragment.txt"
    print(f"\nAccessing Storage Vault: {filename}")
    f = open(filename, 'r')
    print("Connection established...")
    print("\nRECOVERED DATA:")
    rd_str = f.read()
    print(rd_str)
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
