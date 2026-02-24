#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    stream_processor.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/20 21:07:52 by maprunty         #+#    #+#              #
#    Updated: 2026/02/22 00:59:49 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """TODO: Docstring."""

    def init_s(self, init_str: str):
        self.init_str = init_str

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string."""
        self.init_str += f"Processing data: {data}\n"

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        self.init_str += f"Validation: {data} verified\n"

    def format_output(self, result: str) -> str:
        """Format the output string."""
        self.result = result
        self.init_str += f"Output: {result}\n"
        return f"{result}"


class NumericProcessor(DataProcessor):
    """TODO: Docstring."""

    def __init__(self) -> None:
        """TODO: init summary for DataProcessor.

        Args:
            arg (type): Description.
        """
        super().init_s("Initializing Numeric Processor...\n")

    def process(self, data: Any) -> str:
        """Process the data and return result string."""
        super().process(data)
        self.validate(data)
        n = len(data)
        s = sum(data)
        result = f"Processed {n} numeric values, sum={s}, avg={s / n}"
        return super().format_output(result)

    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        try:
            [int(i) for i in data]
            super().validate("Numeric data")
            return True
        except ValueError as e:
            raise ProcException(e) from e
            return False


class TextProcessor(DataProcessor):
    """TODO: Docstring."""

    def __init__(self) -> None:
        """TODO: init summary for DataProcessor.

        Args:
            arg (type): Description.
        """
        super().init_s("Initializing Text Processor...\n")

    def process(self, data: Any) -> str:
        """Process the data and return result string."""
        super().process(data)
        self.validate(data)
        nwords = len(data.split(" "))
        nchars = len(data)
        result = f"Processed text: {nchars} characters, {nwords} words"
        return super().format_output(result)

    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        try:
            if type(data) == str:
                super().validate("Text data")
                return True
            raise ValueError("Not a string")
        except ValueError as e:
            raise ProcException(e) from e
            return False


class LogProcessor(DataProcessor):
    """TODO: Docstring."""

    log_levels = {"ERROR": "ALERT", "INFO": "INFO"}

    def __init__(self) -> None:
        """TODO: init summary for DataProcessor.

        Args:
            arg (type): Description.
        """
        super().init_s("Initializing Numeric Processor...\n")

    def process(self, data: Any) -> str:
        """Process the data and return result string."""
        super().process(data)
        t_log, entry = data.split(":")
        self.validate(t_log)
        result = f"[{self.log_levels[t_log]}] {t_log} level detected:{entry}"
        return super().format_output(result)

    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        try:
            if data in self.log_levels:
                super().validate("Log entry")
                return True
            raise ValueError("Not a log entry")
        except ValueError as e:
            raise ProcException(e) from e
            return False


class ProcException(Exception):
    """TODO: Summary of the exception.

    Args:
        detail (type): Description.
    """

    def __init__(self, *args: str):
        """Initialise a Processor error."""
        super().__init__(*args)


def processors_run(processor: DataProcessor, data: Any):
    try:
        p = processor()
        p.process(data)
        return p
    except ProcException as e:
        print("\n", e)


print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
processors = [NumericProcessor, TextProcessor, LogProcessor]
set_1 = [[1, 2, 3, 4, 5], "Hello Nexus World", "ERROR: Connection timeout"]
p_data = [processors_run(processors[i], set_1[i]) for i in range(3)]
[print(p.init_str) for p in p_data]

print("=== Polymorphic Processing Demo ===\n")
set_2 = [[1, 2, 3], "Hello Nexus!", "INFO: System ready"]
p_data = [processors_run(processors[i], set_2[i]) for i in range(3)]
[print(f"Result {i + 1}: {p.result}") for i, p in enumerate(p_data)]
# print(p_data[0].result)
# print(p_data[0].__dict__)
