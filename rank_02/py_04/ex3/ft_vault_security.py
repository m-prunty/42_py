#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_vault_security.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 08:49:07 by maprunty         #+#    #+#              #
#    Updated: 2026/02/18 09:04:40 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
def r_context(file):
    print("\nSECURE EXTRACTION:")
    with open(file) as f:
        content = f.read()
    return content.strip() + "\n"


def a_context(file, to_append):
    print("\nSECURE PRESERVATIVON:")
    with open(file, "a") as f:
        f.write("\n" + to_append)
    return to_append


filename = "classified_data.txt"
str_ = "[CLASSIFIED] New security protocols archived"

print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
print("\nInitiating secure vault access...")
print("Vault connection established with failsafe protocols")
print(r_context(filename))
print(a_context(filename, str_))

print("Vault automatically sealed upon completion")
print("\nAll vault operations completed with maximum security.")
