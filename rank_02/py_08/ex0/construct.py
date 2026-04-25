#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    construct.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/20 07:52:43 by maprunty         #+#    #+#              #
#    Updated: 2026/04/24 08:00:11 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Welcome to the Matrix Construct."""

import os
import sys

RED = "\033[0;31m"
GREEN = "\033[0;32m"
PURPLE = "\033[0;35m"
LIGHT_BLUE = "\033[1;34m"
BOLD = "\033[1m"
END = "\033[0m"

venv_path, venv_name = os.path.split(os.getenv("VIRTUAL_ENV", "None detected"))

print(
    f"\n{PURPLE}MATRIX STATUS{END}:",
    "You're still plugged in" if not venv_path else "Welcome to the construct",
    end="\n\n",
)

print("Current Python:", sys.executable)
print("Virtual Environment:", venv_name)
if venv_path:
    print("Environment Path:", venv_path)
    print(
        f"\n{GREEN}SUCCESS{END}:"
        + " You're in an isolated environment!\n"
        + "Safe to install packages without affecting\n"
        + "the global system.\n"
    )
    print("Package installation path:\n" + f"{BOLD}{sys.prefix}{END}")
else:
    print(
        f"\n{RED}WARNING{END}:"
        + " You're in the global environment!\n"
        + "The machines can see everything you install.\n"
    )
    print(
        "To enter the construct, run:\n"
        + f"{BOLD}python -m venv matrix_env{END}\n"
        + f"{BOLD}source matrix_env/bin/activate{LIGHT_BLUE} # On Unix{END}\n"
        + f"{BOLD}matrix_env\\Scripts\\activate{LIGHT_BLUE}"
        + f" # On Windows{END}\n"
    )
    print("Then run this program again.")
