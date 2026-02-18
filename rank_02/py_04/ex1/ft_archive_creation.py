#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/01/25 17:01:17 by maprunty         #+#    #+#              #
#    Updated: 2026/02/18 07:53:10 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Exercise 1: Archive Creation."""


def main():
    """Driver open file and write data."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    filename = "new_discovery.txt"
    str_lst = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee",
    ]
    print(f"\nInitializing new storage unit: {filename}")
    with open(filename, "w") as f:
        print("Storage unit created successfully.")
        print("\nInscribing preservation data...")
        i = 1
        for s in str_lst:
            f_str = f"[ENTRY {i:03}] {s}\n"
            f.write(f_str)
            print(f_str, end="")
            i += 1

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation")


if __name__ == "__main__":
    main()
