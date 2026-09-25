#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    generators.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/25 04:25:56 by maprunty         #+#    #+#              #
#    Updated: 2026/09/25 11:14:03 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import json
from abc import ABC, abstractmethod

import numpy as np

from llm_sdk import Small_LLM_Model
from models import FnModel, OutModel, ParamModel, PromptModel

_NUMS = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    ".",
    "-",
]
_BOOL = ["True", "False"]


class GeneratorBase(ABC):
    """Base class for generators."""

    def __init__(self, args, model: Small_LLM_Model):
        print(type(args), args)
        self.model = model
        fns = self.get_from_json(args.functions_definition)
        self.fns: list[FnModel] = [
            FnModel(**i) for i in self.get_from_json(args.functions_definition)
        ]
        self.prompts: list[PromptModel] = [
            PromptModel(**i) for i in self.get_from_json(args.input)
        ]
        self.num_tokens = [self.tokenize(i) for i in _NUMS]
        self.bool_tokens = [self.tokenize(i) for i in _BOOL]
        self.vocab = self.get_from_json(self.model.get_path_to_vocab_file())
        self.vocab_ids = {v: k for k, v in self.vocab.items()}
        print(self.fns)
        [print(i) for i in self.fns]
        [print(i) for i in self.prompts]
        output_path = args.output
        log_path = args.log

    @abstractmethod
    def run(self) -> None:
        """Run the generation process."""
        pass

    def get_fn_by_name(self, name: str) -> FnModel:
        """Retrieve a function definition by its name."""
        for fn in self.fns:
            if fn.name == name:
                return fn
        raise ValueError(f"Function with name {name} not found.")

    def tokenize(self, text: str) -> list[str]:
        """Tokenize the input text and return a list of tokens."""
        # print(f"Tokenizing text: {text}")
        return self.model.encode(text)[0].tolist()

    def get_from_json(self, path: str) -> dict:
        """Load the functions definition from a JSON file."""
        with open(path) as f:
            return json.load(f)


class GreedyGenerator(GeneratorBase):
    """A generator that uses a greedy approach to generate outputs."""

    def __init__(self, args, model: Small_LLM_Model):
        super().__init__(args, model)
        self.run()

    def run(self) -> None:
        for p in self.prompts:
            out = OutModel(prompt=p.prompt)
            self.pick_fn(out)
            self.fill_params(out)
            print(out.model_dump_json(indent=4))

    def fill_params(self, res: OutModel) -> None:
        fn = self.get_fn_by_name(res.name)
        print(fn.parameters)
        for param in fn.parameters:
            if param.name not in res.parameters:
                next_param = self.generate_param_value(res, fn, param)
                next_param = param.type(next_param.strip("'"))

                res.parameters += [
                    ParamModel(
                        name=param.name, type=param.type, value=next_param
                    )
                ]

    #                print(res.parameters[0])

    def generate_param_value(
        self, res: OutModel, fn: FnModel, param: ParamModel
    ) -> str:
        header = (
            "Terminate token genertation with a newline.\n"
            "Select a value for the parameter based on the following information:\n"
            f"Current function: {fn}\n"
            f"Request: {res.prompt}\n"
            f"Generated so far: {[str(i) for i in res.parameters]}\n"
            f"Parameter: {param.name}\n"
            f"Expected type: {param.type}\n"
            f"Value: "
        )
        response = ""
        while response[-1:] != "\n":
            # print(f"Current response: {response!r}, header: {header}")
            next_token = self.constrained_sample(
                logits=np.asarray(
                    self.model.get_logits_from_input_ids(
                        self.tokenize(header)
                    ),
                    dtype=float,
                ),
                current_text=res.name,
                candidates=[],
                token_to_char=self.vocab_ids,
            )
            response += self.model.decode([next_token])
            header += self.model.decode([next_token])
        return response.strip()

    def pick_fn(self, res: OutModel) -> None:
        fns_withdescriptions = "\n".join(str(fn) for fn in self.fns)
        header = (
            f"Available functions:\n{fns_withdescriptions}\n\n"
            f"Request: {res.prompt}\n"
            f"Function name: "
        )
        while res.name not in [i.name for i in self.fns]:
            next_token = self.constrained_sample(
                logits=np.asarray(
                    self.model.get_logits_from_input_ids(
                        self.tokenize(header + res.name)
                    ),
                    dtype=float,
                ),
                current_text=res.name,
                candidates=[i.name for i in self.fns],
                token_to_char=self.vocab_ids,
            )
            #            print(
            #                f"Next token ID: {next_token}, decoded: {self.model.decode([next_token])}"
            #            )
            res.name += self.model.decode([next_token])

    def constrained_sample(
        self,
        logits: np.ndarray,
        current_text: str,
        candidates: list[str],
        token_to_char: dict[int, str],
    ) -> int:
        valid_chars = [c for c in candidates if c.startswith(current_text)]
        valid_token_ids = {
            tid
            for tid, s in token_to_char.items()
            if s and any(c.startswith(current_text + s) for c in valid_chars)
        }
        masked_logits = logits.copy()
        if valid_token_ids:
            for tid in range(len(logits)):
                if tid not in valid_token_ids:
                    masked_logits[tid] = float("-inf")

        probs = self._softmax(masked_logits)
        return np.argmax(probs)

    def _softmax(self, x: np.ndarray) -> np.ndarray:
        """Compute softmax probabilities.

        https://en.wikipedia.org/wiki/Softmax_function
        https://www.delftstack.com/howto/numpy/numpy-softmax/
        """
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum()
