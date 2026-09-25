#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    gen_pipe.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/12 23:42:02 by maprunty         #+#    #+#              #
#    Updated: 2026/09/25 05:55:51 by maprunty        ###   ########.fr        #
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

from generators import GreedyGenerator
from llm_sdk import Small_LLM_Model


class GenerationPipeline:
    """A class to handle the generation pipeline for a small LLM model."""

    def __init__(self, args):
        self.model = Small_LLM_Model()
        gen = GreedyGenerator(args, self.model)
        gen.run()

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

    def prompt_user(self, prompt: str) -> str:
        """Prompt the user for input and return their response."""
        return input(prompt)
