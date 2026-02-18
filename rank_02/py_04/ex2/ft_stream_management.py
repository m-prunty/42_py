#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_stream_management.py                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 07:54:38 by maprunty         #+#    #+#              #
#    Updated: 2026/02/18 08:47:16 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""$> python3 ft_stream_management.py.

=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===
Input Stream active. Enter archivist ID: ARCH_7742
Input Stream active. Enter status report: All systems nominal
[STANDARD] Archive status from ARCH_7742: All systems nominal
[ALERT] System diagnostic: Communication channels verified
[STANDARD] Data transmission complete
Three-channel communication test successful.
"""

from sys import stderr, stdin, stdout


def archive_in(msg) -> str:
    stdout.write("Input stream active. ")
    stdout.write(msg)
    stdout.flush()
    return stdin.readline().rstrip("\n")


def archive_out(msg):
    stdout.write("[STANDARD] ")
    stdout.write(msg)


def archive_err(msg):
    stderr.write("[ALERT] ")
    stderr.write(msg)


id_ = archive_in("Enter archivist ID: ")
report = archive_in("Enter status report: ")
print()
archive_out(f"Archive status from {id_}: {report}\n")
archive_err("System diagnostic: Communication channels verified\n")
archive_out("Data transmission complete\n")
print()
print("Three-channel communication test successful.")
