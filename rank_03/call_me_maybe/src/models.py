#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    models.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/13 09:39:52 by maprunty         #+#    #+#              #
#    Updated: 2026/09/25 11:12:38 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


import re
from typing import Any

from pydantic import BaseModel, Field, model_serializer, model_validator

_TYPES = {
    "string": str,
    "number": float,
    "boolean": bool,
    "integer": int,
}


class ParamModel(BaseModel):
    """Pydantic model for a function parameter."""

    name: str
    type: type
    value: Any = Field(default=None)

    @model_validator(mode="after")
    def validate_param(self) -> "ParamModel":
        if isinstance(self.value, str) and self.type is str:
            if self.name == "regex":
                try:
                    re.compile(self.value)
                except re.error as e:
                    raise ValueError(
                        f"Value for parameter '{self.name}' must be a valid regex pattern. "
                        f"Error: {e}"
                    )
        #            elif self.value.isnumeric() and self.type is str:
        #                raise ValueError(
        #                    f"Value for parameter '{self.name}' must be a string, "
        #                    f"got a numeric string instead."
        #                )

        if self.type not in _TYPES.values():
            raise ValueError(
                f"Type '{self.type.__name__}' is not a valid type. "
                f"Valid types are: {', '.join(t.__name__ for t in _TYPES.values())}."
            )
        return self

    @model_serializer
    def serialize(self) -> dict[str, Any]:
        """Serialize the ParamModel instance to a JSON-serializable dictionary."""
        return {
            "name": self.name,
            "value": self.value,
        }

    def __str__(self) -> str:
        return f"{self.name}: {self.value}"


class FnModel(BaseModel):
    """Pydantic model for a function definition."""

    name: str
    description: str
    parameters: list[ParamModel] = Field(default_factory=list)
    returns: type

    @model_validator(mode="before")
    @classmethod
    def pre_process(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Pre-process the input values to convert strings to actual types."""
        #        print(values)

        if "parameters" in values:
            values["parameters"] = [
                ParamModel(name=k, type=_TYPES[v["type"]])
                for k, v in values["parameters"].items()
            ]
        if "returns" in values:
            values["returns"] = _TYPES[values["returns"]["type"]]
        return values

    @model_serializer
    def serialize(self) -> dict[str, Any]:
        """Serialize the FnModel instance to a JSON-serializable dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": [i.model_dump(mode="json") for i in self.parameters],
            "returns": {"type": self.returns.__name__},
        }

    def __str__(self) -> str:
        params_str = ", ".join(
            f"{p.name}: {p.type.__name__}" for p in self.parameters
        )
        return f"- {self.name}({params_str}) -> {self.returns.__name__}: {self.description}"

    def __getattr__(self, name: str) -> Any:
        try:
            return self.__dict__[name]
        except KeyError:
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}'"
            )


class PromptModel(BaseModel):
    """Pydantic model for a prompt."""

    prompt: str


class OutModel(BaseModel):
    """Pydantic model for an output."""

    prompt: str
    name: str = Field(default="")
    parameters: list[ParamModel] = Field(default_factory=list)

    def __str__(self) -> str:
        msg_ai = ""
        r_str = (
            f"{'Prompt: ' + self.prompt if self.prompt else msg_ai}\n"
            + f"{'Name: ' + self.name if self.name else msg_ai}\n"
            + f"{'Parameters: ' + str(self.parameters) if self.parameters else msg_ai}\n"
        )
        return r_str

    @model_serializer
    def serialize(self) -> dict[str, Any]:
        """Convert the OutModel instance to a JSON-serializable dictionary."""
        return {
            "prompt": self.prompt,
            "name": self.name,
            "parameters": [i.model_dump(mode="json") for i in self.parameters],
        }

    def __iter__(self):
        return [self.prompt, self.name, iter(self.parameters.items())]
