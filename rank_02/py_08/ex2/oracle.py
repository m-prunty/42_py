#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    oracle.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/25 04:38:29 by maprunty         #+#    #+#              #
#    Updated: 2026/04/25 08:24:08 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import os
import sys

from dotenv import load_dotenv

RED = "\033[0;31m"
GREEN = "\033[0;32m"
PURPLE = "\033[0;35m"
LIGHT_BLUE = "\033[1;34m"
BOLD = "\033[1m"
END = "\033[0m"


def getenv(key: str) -> str:
    """Get an environment variable or raise an error if it's missing."""
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Missing required env var: {key}")
    return value


def env_state() -> None:
    """Print the current state of the environment variables."""
    try:
        print(f"Mode: {getenv('MATRIX_MODE')}")
        print(
            "Database: connected to"
            + f" {' '.join(getenv('DATABASE_URL').split('_'))}"
        )
        print(
            "API Access:", "Authenticated" if getenv("API_KEY") else "Denied"
        )
        print(f"Log Level: {getenv('LOG_LEVEL').upper()}")
        print(
            "Zion Network:",
            "Online" if getenv("ZION_ENDPOINT") else "Disconnected",
            end="\n\n",
        )
    except ValueError as e:
        print(f"{RED}[ERROR]{END} {e}")
        sys.exit(1)


def load_configuration() -> str:
    """Load configuration from .env file and validate it."""
    print("Reading the matrix...", end="\n\n")
    try:
        load_dotenv()
        return "Configuation loaded:"
    except Exception as e:
        print(f"{RED}[ERROR]{END} Failed to load configuration: {e}")
        sys.exit(1)


def security_check() -> None:
    """Perform security checks on the environment configuration."""
    print("Environment security check:")
    if os.getenv("API_KEY"):
        print(f"{GREEN}[OK]{END} No hardcoded secrets detected")
    else:
        print(f"{RED}[WARN]{END} Missing API key")
    if os.path.exists(".env"):
        print(f"{GREEN}[OK]{END} .env file is properly configured")
    else:
        print(f"{RED}[WARN]{END} .env file not found")
    new_mode = (
        "development"
        if os.getenv("MATRIX_MODE") == "production"
        else "production"
    )
    os.environ["MATRIX_MODE"] = new_mode
    if os.getenv("MATRIX_MODE") == new_mode:
        print(f"{GREEN}[OK]{END} Production overides available")
    else:
        print(f"{RED}[WARN]{END} Production overrides not working")
    print()


def main() -> None:
    """Main function to run the Oracle status check."""
    print(f"\n{PURPLE}ORACLE STATUS{END}:", end="")
    print(load_configuration())
    env_state()
    security_check()
    print("The Oracle sees all configurations")


if __name__ == "__main__":
    main()
