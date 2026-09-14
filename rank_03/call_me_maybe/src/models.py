#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    models.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/13 09:39:52 by maprunty         #+#    #+#              #
#    Updated: 2026/09/13 12:20:12 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


from typing import Any

from pydantic import BaseModel, model_validator

_TYPES = {
    "string": str,
    "number": float,
}


class FnModel(BaseModel):
    """Pydantic model for a function definition."""

    name: str
    description: str
    parameters: dict[str, type]
    returns: type

    @model_validator(mode="before")
    @classmethod
    def pre_process(cls, values: dict[str, Any]) -> dict[str, str | type]:
        """Pre-process the input values to convert strings to actual types."""
        print(values)
        if "parameters" in values:
            values["parameters"] = {
                k: _TYPES[v["type"]] for k, v in values["parameters"].items()
            }
        if "returns" in values:
            values["returns"] = _TYPES[values["returns"]["type"]]
        return values

    def __str__(self) -> str:
        return self.name

    def __getattr__(self, name):
        return self.name


class ParamModel(BaseModel):
    """Pydantic model for a function parameter."""

    name: str
    type: type


class PromptModel(BaseModel):
    """Pydantic model for a prompt."""

    prompt: str


class OutModel(BaseModel):
    """Pydantic model for an output."""

    prompt: str
    name: str
    parameters: dict[str, Any]
