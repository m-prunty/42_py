#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    __main__.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/06 10:50:49 by maprunty         #+#    #+#              #
#    Updated: 2026/09/11 16:51:05 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

"""Main file to run A-maze-ing."""

import os

from llm_sdk import Small_LLM_Model

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


def main() -> None:
    """Run A-maze-ing."""
    """https://realpython.com/command-line-interfaces-python-argparse/"""
    print(
        f"\n{PURPLE}A_Maze_ing{END}:",
    )
    venv_path, venv_name = os.path.split(os.getenv("VIRTUAL_ENV", "None"))
    if venv_path:
        print("Welcome to the Maze")
        # try:
        init_model = Small_LLM_Model()
        print(init_model.encode("return"))
        # print(init_model.decode([7592, 11, 995]))
        #   print(init_model.decode([i for i in range(100)]))
        print(init_model.get_path_to_vocab_file())
        print(init_model.get_path_to_merges_file())
        #   print(init_model.encode("What is the sum of 2 and 3?"))
        # print(
        #    init_model.decode(init_model.get_logits_from_input_ids([9707, 11]))
        # )
        logits = init_model.get_logits_from_input_ids([470])

        print(logits)
    #        for token_id, score in enumerate(logits):
    #            token = init_model.decode([token_id])
    #            print(token_id, repr(token), score)
    #        except Exception as e:
    #            print(f"Error during main loop: {e}")
    else:
        print(not_venv_warning())


if __name__ == "__main__":
    main()
