#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    gen_pipe.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/12 23:42:02 by maprunty         #+#    #+#              #
#    Updated: 2026/09/14 18:17:50 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

"""V.3.2 The Generation Pipeline
The LLM generation process follows these steps:
1. Prompt: Your natural language question
Example: "What is the sum of 2 and 3?"
2. Tokenization: The text is broken into subword units (tokens). Unlike simple word
splitting, tokenizers often include leading spaces, handle punctuation, and split
words into smaller components using algorithms such as BPE or SentencePiece.
Example (realistic): ["What", "˙Gis", "˙Gthe", "˙Gsum", "˙Gof", "˙G2", "˙Gand", "˙G3", "?"]
Note: The symbol "˙G", indicates a preceding space; real tokenizers preserve such
details to reconstruct text accurately.
3. Input IDs: Tokens are converted to numerical IDs the model understands.
Example (illustrative): [892, 318, 262, 4771, 286, 16, 290, 17, 30]
4. LLM Processing: The model processes these numbers through its neural network.
5. Logits: The model outputs probability scores for each possible next token.
Example: token_5: 0.001, token_42: 0.85, token_100: 0.02, ...
6. Token Selection: The next token is chosen based on these probabilities, usually
the one with the highest score.
At this stage, techniques like constrained decoding can be applied to restrict the
token choices and ensure outputs follow a specific structure, such as generating
100% valid JSON.
12
call me maybe Introduction to function calling in LLMs
Important: This process repeats token-by-token. Each generated token is added to the
prompt, and steps 2-6 repeat until the complete response is generated.
Simplified view:
Prompt -> Tokenization -> Input IDs -> LLM -> Logits -> Next Token Selection
"""

import json

import numpy as np

from llm_sdk import Small_LLM_Model
from models import FnModel, PromptModel


class GrammarConstrainedSampler:
    """Apply grammar constraints during text generation.

    This simplified implementation assumes character-level tokenization.
    Real implementations must handle subword tokenization carefully.
    https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output#implementing-grammar-constraints
    """

    def __init__(self, grammar_valid_fn):
        """Initialize with a function that returns valid next tokens.

        Args:
            grammar_valid_fn: Function(current_text) -> set of valid tokens
        """
        self.grammar_valid_fn = grammar_valid_fn

    def constrained_sample(
        self,
        logits: np.ndarray,
        current_text: str,
        token_to_char: dict[int, str],
    ) -> int:
        """Sample from logits with grammar constraints.

        Args:
            logits: Raw model logits over vocabulary
            current_text: Text generated so far
            token_to_char: Mapping from token IDs to characters

        Returns:
            Selected token ID
        """
        # Get valid tokens from grammar
        valid_chars = self.grammar_valid_fn(current_text)

        # Create mask for valid token IDs
        valid_token_ids = {
            tid for tid, char in token_to_char.items() if char in valid_chars
        }

        # Apply mask: set invalid logits to -infinity
        masked_logits = logits.copy()
        for tid in range(len(logits)):
            if tid not in valid_token_ids:
                masked_logits[tid] = float("-inf")

        # Convert to probabilities and sample
        probs = self._softmax(masked_logits)
        return np.random.choice(len(probs), p=probs)

    def _softmax(self, x: np.ndarray) -> np.ndarray:
        """Compute softmax probabilities."""
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum()


class GenerationPipeline:
    """A class to handle the generation pipeline for a small LLM model."""

    def __init__(self, args):
        self.model = Small_LLM_Model()
        fns = self.get_from_json(args.functions_definition)
        self.fns: list[FnModel] = [
            FnModel(**i) for i in self.get_from_json(args.functions_definition)
        ]
        self.prompts: list[PromptModel] = [
            PromptModel(**i) for i in self.get_from_json(args.input)
        ]
        #        fn_logits = self.model.get_logits_from_input_ids(
        #            self.model.encode("function_calling").tolist()
        #        )
        output_path = args.output
        log_path = args.log
        with open(self.model.get_path_to_vocab_file()) as f:
            str2id = json.load(f)
        id2str = {v: k for k, v in str2id.items()}
        print(id2str)
        [print(i) for i in self.fns]
        [print(i) for i in self.prompts]
        self.generated = ""
        self.enum_constrained_generate(
            self.model,
            self.tokenize(self.prompts[0].prompt),
            ["fn_add_numbers", "fn_greet"],
            id2str,
        )
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        #        self.enum_constrained_generate(
        #            self.model,
        #            self.tokenize(self.prompts[0].prompt),
        #            nums,
        #            id2str,
        #        )
        print(
            self.decode(
                self.constrained_sample(
                    np.asarray(
                        self.model.get_logits_from_input_ids(
                            self.tokenize(self.prompts[0].prompt)
                        ),
                        dtype=float,
                    ),
                    self.generated,
                    nums,
                    id2str,
                )
            )
        )

        # try:
        # print(self.model.encode("return"))
        # print(self.model.decode([7592, 11, 995]))
        #   print(self.model.decode([i for i in range(100)]))
        print(self.model.get_path_to_vocab_file())
        print(self.model.get_path_to_merges_file())
        #        in_ids = self.model.encode("What is the sum of 2 and 3?").tolist()
        # in_ids += self.model.encode("Greet shrek").tolist()
        #        print(in_ids)
        # print(
        #    self.model.decode(init_model.get_logits_from_input_ids([9707, 11]))
        # )
        #        logits = self.model.get_logits_from_input_ids(in_ids[0])
        #        for token_id, score in enumerate(logits):
        #            token = self.model.decode([token_id])
        #            if score > 10:
        #                print(token_id, repr(token), score)
        #        print(
        #            f"Most probable next token: {repr(most_probable_token)} with score {max(logits)}"
        #        )
        #        sorted_logits = sorted(
        #            [(token_id, score) for token_id, score in enumerate(logits)],
        #            key=lambda x: x[1],
        #            reverse=True,
        #        )
        #        print("Top 10 tokens by score:")
        #        for token_id, score in sorted_logits[:10]:
        #            token = self.model.decode([token_id])
        #            print(token_id, repr(token), score)

        # print(self.get_response(prompt))

        #        for token_id, score in enumerate(logits):
        #            token = self.model.decode([token_id])
        #            if score > 10:
        #                print(token_id, repr(token), score)

        #        except Exception as e:
        #            print(f"Error during main loop: {e}")

        # print(logits)

    def constrained_sample(
        self,
        logits: np.ndarray,
        current_text: str,
        candidates: list[str],
        token_to_char: dict[int, str],
    ) -> int:
        """Sample from logits with grammar constraints.

        Args:
            logits: Raw model logits over vocabulary
            current_text: Text generated so far
            token_to_char: Mapping from token IDs to characters

        Returns:
            Selected token ID
        """
        # Get valid tokens from grammar
        # valid_chars = self.grammar_valid_fn(current_text)
        valid_chars = [c for c in candidates if c.startswith(current_text)]

        # Create mask for valid token IDs
        valid_token_ids = {
            tid for tid, char in token_to_char.items() if char in valid_chars
        }

        # Apply mask: set invalid logits to -infinity
        masked_logits = logits.copy()
        for tid in range(len(logits)):
            if tid not in valid_token_ids:
                masked_logits[tid] = float("-inf")

        # Convert to probabilities and sample
        probs = self._softmax(masked_logits)
        return np.random.choice(len(probs), p=probs)

    def _softmax(self, x: np.ndarray) -> np.ndarray:
        """Compute softmax probabilities."""
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum()

    def enum_constrained_generate(
        self, model, ids, candidates, id2str, max_steps=30
    ):
        generated = ""
        # print(model, ids, candidates, max_steps)
        for _ in range(max_steps):
            live = [c for c in candidates if c.startswith(generated)]
            print(f"Live candidates: {live}, generated so far: {generated!r}")
            if generated in live and len(live) == 1:
                return generated, ids  # unambiguous match — done

            logits = np.asarray(
                model.get_logits_from_input_ids(ids), dtype=float
            )
            allowed = [
                tid
                for tid, s in id2str.items()
                if s and any(c.startswith(generated + s) for c in live)
            ]
            print(
                f"Allowed token IDs: {allowed},{self.model.decode(allowed)} logits: {logits}"
            )
            if not allowed:
                raise RuntimeError(f"dead end after {generated!r}")

            masked = np.full_like(logits, -np.inf)
            masked[allowed] = logits[allowed]
            next_id = int(np.argmax(masked))

            ids.append(next_id)
            generated += id2str[next_id]
            print(
                f"Generated so far: {generated!r}, next token: {id2str[next_id]!r}"
            )
        self.generated = generated
        raise RuntimeError("exceeded max_steps")

    def get_response(self, prompt: str) -> str:
        """Get a response from the model for the given prompt."""
        prompt = "prompt: " + prompt
        prompt += " JSON style response:"
        ids = self.model.encode(prompt)[0].tolist()
        for _ in range(50):
            logits = self.model.get_logits_from_input_ids(ids)
            next_token = max(range(len(logits)), key=lambda i: logits[i])
            ids.append(next_token)
        return self.model.decode(ids)

    def get_from_json(self, path: str) -> dict:
        """Load the functions definition from a JSON file."""
        with open(path) as f:
            return json.load(f)

    def prompt_user(self, prompt: str) -> str:
        """Prompt the user for input and return their response."""
        return input(prompt)

    def run(self): ...
    def tokenize(self, text: str) -> list[str]:
        """Tokenize the input text and return a list of tokens."""
        print(f"Tokenizing text: {text}")
        return self.model.encode(text)[0].tolist()
        # try:
