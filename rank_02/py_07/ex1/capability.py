#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    capability.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 19:19:42 by maprunty         #+#    #+#              #
#    Updated: 2026/04/18 20:49:03 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target):
        return f"{self.name} heals {target} for a"


class TransformCapability(ABC):
    def __init__(self):
        super().__init__()
        self.transformed = False

    @abstractmethod
    def transform(self):
        self.transformed = True
        return f"{self.name}"

    @abstractmethod
    def revert(self):
        self.transformed = False
        return f"{self.name}"
