#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 09:05:56 by maprunty         #+#    #+#              #
#    Updated: 2026/02/18 10:02:35 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""akjhsgdghasgdj.

=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===
CRISIS ALERT: Attempting access to 'lost_archive.txt'...
RESPONSE: Archive not found in storage matrix
STATUS: Crisis handled, system stable
CRISIS ALERT: Attempting access to 'classified_vault.txt'...
RESPONSE: Security protocols deny access
STATUS: Crisis handled, security maintained
ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...
SUCCESS: Archive recovered - ``Knowledge preserved for humanity''
STATUS: Normal operations resumed
All crisis scenarios handled successfully. Archives secure.

"""


def access_archive(path: str) -> str:
    try:
        path_str = f"Attempting access to '{path}'..."
        with open(path) as f:
            r_str = f.read()
        print(f"ROUTINE ACCESS: {path_str}")
        print(f"SUCCESS: Archive recovered - {r_str}")
        print("STATUS: Normal operations resumed")
    except FileNotFoundError as e:
        raise CrisisFileNotFound(path_str) from e
    except PermissionError as e:
        raise CrisisPermissionDenied(path_str) from e


class CrisisAlert(Exception):
    def __init__(self, path_str: str, response: str, status: str):
        self.path_str = path_str
        super().__init__(f"CRISIS ALERT: {path_str}{response}{status}")


class CrisisFileNotFound(CrisisAlert):
    """Raised when path_str is missing."""

    def __init__(self, path_str: str):
        response = "\nRESPONSE: path_str not found in storage matrix"
        status = "\nSTATUS: Crisis handled, system stable\n"
        super().__init__(path_str, response, status)


class CrisisPermissionDenied(CrisisAlert):
    """Raised when access is denied by security."""

    def __init__(self, path_str: str):
        response = "\nRESPONSE: Security protocols deny access"
        status = "\nSTATUS: Crisis handled, security maintained\n"
        super().__init__(path_str, response, status)


def main():
    files = [
        "lost_archive.txt",
        "classified_data.txt",
        "standard_archive.txt",
    ]
    for f in files:
        try:
            access_archive(f)
        except CrisisAlert as e:
            print(e)

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
