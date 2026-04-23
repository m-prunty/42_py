#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    capability.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 19:19:42 by maprunty         #+#    #+#              #
#    Updated: 2026/04/22 11:54:58 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Module defining capabilities for creatures."""

from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract base class for healing capability."""

    @abstractmethod
    def heal(self, target: str) -> str:
        """Heal the target creature."""
        ...


class TransformCapability(ABC):
    """Abstract base class for transformation capability."""

    def __init__(self) -> None:
        """Initialize the transformation state."""
        super().__init__()
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        """Transform the creature to boost its abilities."""
        ...

    @abstractmethod
    def revert(self) -> str:
        """Revert the creature back to its normal form."""
        ...
