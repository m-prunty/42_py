#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    __main__.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/06 10:50:49 by maprunty         #+#    #+#              #
#    Updated: 2026/09/13 08:50:32 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

"""Main file to run Call Me Maybe."""

import os
import sys
from argparse import ArgumentParser, Namespace

from gen_pipe import GenerationPipeline

RED = "\033[0;31m"
GREEN = "\033[0;32m"
PURPLE = "\033[0;35m"
LIGHT_BLUE = "\033[1;34m"
BOLD = "\033[1m"
END = "\033[0m"


def not_venv_warning() -> str:
    """Return a warning message if the user is not in a virtual environment."""
    return (
        f"\n{RED}WARNING{END}:"
        + "You're not in a virtual environment!\n"
        + "To enter the construct, run:\n"
        + (
            f"{BOLD}make install{END}\nfollowed by:\n"
            if not os.path.exists("./.venv")
            else ""
        )
        + f"{BOLD}make run{END}\n"
        + "or activate the venv manually:\n"
        + f"{BOLD}source .venv/bin/activate{LIGHT_BLUE}"
    )


"""
IV.3.2 Usage
Your program must be run using the following command (where src is the folder con-
taining your files):
Running the program
uv run python -m src [--functions_definition <function_definition_file>] [--input <input_file>] [--
output <output_file>]
By default, the program will read input files from the data/input/
directory and write output to the data/output/ directory. You
can optionally specify custom paths using the --input and --output
arguments. For example:
uv run python -m src
--functions_definition data/input/functions_definition.json
--input data/input/function_calling_tests.json
--output data/output/function_calls.json
"""


def args_parse() -> Namespace:
    """https://realpython.com/command-line-interfaces-python-argparse/"""
    parser = ArgumentParser(description="Call Me Maybe")
    parser.add_argument(
        "-f",
        "--functions_definition",
        type=str,
        default="data/input/functions_definition.json",
        help="Path to the functions definition file",
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default="data/input/function_calling_tests.json",
        help="Path to the input file",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="data/output/function_calls.json",
        help="Path to the output file",
    )
    parser.add_argument(
        "-l",
        "--log",
        type=str,
        default=sys.stdout,
        help="Path to the log file",
    )
    return parser.parse_args()


def main() -> None:
    """Run Call Me Maybe."""
    args = args_parse()
    print(
        f"\n{PURPLE}Call Me Maybe{END}:",
    )
    print(args)
    venv_path, venv_name = os.path.split(os.getenv("VIRTUAL_ENV", "None"))
    if venv_path:
        print("Welcome to Call Me Maybe!")
        pipe = GenerationPipeline(args)
    else:
        print(not_venv_warning())


if __name__ == "__main__":
    main()
