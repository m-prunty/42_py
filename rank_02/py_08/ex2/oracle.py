#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    oracle.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/25 04:38:29 by maprunty         #+#    #+#              #
#    Updated: 2026/04/25 05:20:26 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import os

from dotenv import load_dotenv

print([i for i in os.environ])
load_dotenv()
print([i for i in os.environ])
