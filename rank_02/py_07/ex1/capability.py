#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    capability.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 19:19:42 by maprunty         #+#    #+#              #
#    Updated: 2026/04/20 02:29:14 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Module defining capabilities for creatures."""

from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract base class for healing capability."""

    @abstractmethod
    def heal(self, target):
        """Heal the target creature."""
        return f"{self.name} heals {target} for a"


class TransformCapability(ABC):
    """Abstract base class for transformation capability."""

    def __init__(self):
        """Initialize the transformation state."""
        super().__init__()
        self.transformed = False

    @abstractmethod
    def transform(self):
        """Transform the creature to boost its abilities."""
        self.transformed = True
        return f"{self.name}"

    @abstractmethod
    def revert(self):
        """Revert the creature back to its normal form."""
        self.transformed = False
        return f"{self.name}"
