#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    stream_processor.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/20 21:07:52 by maprunty         #+#    #+#              #
#    Updated: 2026/02/21 00:32:01 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """TODO: Docstring."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string."""
        print(f"Processing data: {data}", end="")
        self.data = data

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        print(f"\nValidation: {data} verified")

    def format_output(self, result: str) -> str:
        """Format the output string."""
        return f"{result}"


class NumericProcessor(DataProcessor):
    """TODO: Docstring."""

    def __init__(self) -> None:
        """TODO: init summary for DataProcessor.

        Args:
            arg (type): Description.
        """
        print("\nInitializing Numeric Processor...")

    def process(self, data: Any) -> str:
        """Process the data and return result string."""
        super().process(data)
        n = len(data)
        s = sum(data)
        self.result = f"Processed {n} numeric values, sum={s}, avg={s / n}"
        return data

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
        print("\nInitializing Text Processor...")

    def process(self, data: Any) -> str:
        """Process the data and return result string."""
        super().process(data)
        return data

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

    def __init__(self) -> None:
        """TODO: init summary for DataProcessor.

        Args:
            arg (type): Description.
        """
        print("\nInitializing Numeric Processor...")

    def process(self, data: Any) -> str:
        """Process the data and return result string."""
        super().process(data)
        return data

    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        try:
            super().validate("Log entry")
            return True
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
        p.validate(data)
        return processor
    except ProcException as e:
        print("\n", e)


processors = [NumericProcessor, TextProcessor, LogProcessor]
datas = [[1, 2, 3], "Hello Nexus", "INFO: System ready"]
p_data = [processors_run(processors[i], datas[i]) for i in range(3)]
print(p_data[0].__dict__)
