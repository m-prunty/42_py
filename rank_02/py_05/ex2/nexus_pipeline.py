#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    nexus_pipeline.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/23 05:35:28 by maprunty         #+#    #+#              #
#    Updated: 2026/02/26 06:34:03 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===
Initializing Nexus Manager...
Pipeline capacity: 1000 streams/second
Creating Data Processing Pipeline...
Stage 1: Input validation and parsing
Stage 2: Data transformation and enrichment
Stage 3: Output formatting and delivery
=== Multi-Format Data Processing ===
Processing JSON data through pipeline...
Input: {"sensor": "temp", "value": 23.5, "unit": "C"}
Transform: Enriched with metadata and validation
Output: Processed temperature reading: 23.5°C (Normal range)
Processing CSV data through same pipeline...
Input: "user,action,timestamp"
Transform: Parsed and structured data
Output: User activity logged: 1 actions processed
Processing Stream data through same pipeline...
Input: Real-time sensor stream
Transform: Aggregated and filtered
Output: Stream summary: 5 readings, avg: 22.1°C
=== Pipeline Chaining Demo ===
Pipeline A -> Pipeline B -> Pipeline C
Data flow: Raw -> Processed -> Analyzed -> Stored
Chain result: 100 records processed through 3-stage pipeline
Performance: 95% efficiency, 0.2s total processing time
=== Error Recovery Test ===
Simulating pipeline failure...
Error detected in Stage 2: Invalid data format
Recovery initiated: Switching to backup processor
Recovery successful: Pipeline restored, processing resumed
Nexus Integration complete. All systems operational
"""

from abc import ABC, abstractmethod
from typing import Any, Protocol


# Stages
class ProcessingStage(Protocol):
    """Processing Stage"""

    def process(self, data: Any) -> Any: ...

    def log(self, name=__doc__):
        """Log string:."""
        print(">>", self.log.__doc__)
        print(">>>", self.__doc__)
        print(">>>>", name)
        return name


class InputStage:
    """Input:."""

    def process(self, data: Any) -> dict:
        """Input validation and parsing"""
        r_dct = data["data"]
        print("Input:", end=" ")
        if data["id"] == "Stream":
            print("Real-time sensor stream")
        else:
            print(r_dct)
        return r_dct


class TransformStage:
    """Transform:."""

    T_STRS = {
        "JSON": "Enriched with metadata and validation",
        "CSV": "Parsed and structured data",
        "Stream": "Aggregated and filtered",
    }

    def process(self, data: Any) -> dict:
        """Data transformation and enrichment"""
        r_dct = data
        print("Transform:", self.T_STRS[r_dct["id"]])
        return r_dct


class OutputStage:
    """Output:."""

    O_STRS = {
        "JSON": (
            lambda dct: f"Processed temperature reading: {dct['value']}°{dct['unit']} (Normal range)"
        ),
        "CSV": (
            lambda lst: f"User activity logged: {len(lst)} actions processed"
        ),
        "Stream": lambda lst_dct: f"Stream summary: {len(lst_dct)} readings, avg: {sum(dct['value'] for dct in lst_dct) / len(lst_dct)}°C",
    }

    def process(self, data: Any) -> str:
        """Output formatting and delivery"""
        r_dct = data
        # print(r_dct)
        d = r_dct["data"]
        print("Output:", self.O_STRS[r_dct["id"]](d))
        print()
        return r_dct


class ProcessingPipeline(ABC):
    """ProcessingPipe."""

    def __init__(self) -> None:
        self.stages: list[ProcessingStage] = []
        self.r_str = (
            f"Processing {self.__doc__.split(' ')[0]} data through pipeline..."
        )

    @abstractmethod
    def process(self, data: Any) -> Any:
        result = {}
        # print(data)
        d = {"id": self.pipeline_id, "data": data}
        result[self.pipeline_id] = {key: None for key in self.stages}
        for s in self.stages:
            result[self.pipeline_id][s] = s.process(d)
        return result

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def log(self, name=__doc__):
        """Log string:."""
        print(">", name, ">>", self.log.__doc__, ">>>", self.__doc__)
        print(", ".join(s.__doc__ for s in self.stages))
        print(self.pipeline_id, "id")
        return name


# Adapters
class JSONAdapter(ProcessingPipeline):
    """JSON Adapter."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        return super().process(data)


class CSVAdapter(ProcessingPipeline):
    """CSV Adapter."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        data = {key: None for key in data.split("\n")}
        r = super().process(data)
        return r


class StreamAdapter(ProcessingPipeline):
    """Stream Adapter."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        # print("adpt", data)
        # result = {}
        # for i in data:
        #    print(i)
        result = super().process(data)
        return result


# Manager
class NexusManager:
    """=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ==="""

    def __init__(self) -> None:
        print(self.__doc__ + "\n")
        print("Initializing Nexus Manager...")
        self.pipelines: List[ProcessingPipeline] = []
        self.metrics = {}
        self.cap = 1000
        print(f"Pipeline capacity: {self.cap} streams/second")

    def process_data(self, data: Any) -> None:
        if isinstance(data, dict) and any(key in ADAPTERS for key in data):
            result = {key: None for key in dct}
            # print(result)
            # print(">>>>>", self.pipelines[0].stages)
            for k, v in data.items():
                result[k] = PIPES[k].process(v)
        return result

    # def process_batch(self, data: Any )
    # print(result)

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def add_pipeline_batch(self, pdct: dict[str, ProcessingPipeline]) -> None:
        [self.add_pipeline(v) for k, v in pdct.items()]
        # print(">>>>", self.pipelines)


ADAPTERS = {
    "json": JSONAdapter,
    "csv": CSVAdapter,
    "stream": StreamAdapter,
}
STAGES = [InputStage, TransformStage, OutputStage]
PIPES = {
    "json": JSONAdapter("JSON"),
    "csv": CSVAdapter("CSV"),
    "stream": StreamAdapter("Stream"),
}
DATA = {
    "json": {"sensor": "temp", "value": 23.5, "unit": "C"},
    "csv": "user,action,timestamp\nAlice,jump,251013",
    "stream": [
        {"sensor": "temp", "value": 23.0, "unit": "C"},
        {"sensor": "temp", "value": 20.6, "unit": "C"},
        {"sensor": "temp", "value": 23.5, "unit": "C"},
        {"sensor": "temp", "value": 21.9, "unit": "C"},
        {"sensor": "temp", "value": 21.5, "unit": "C"},
    ],
}


def get_pipeline_stages(adapt_type: str) -> ProcessingPipeline:
    p = [PIPES[adapt_type.lower()].add_stage(s()) for s in STAGES]
    return p


def get_pipes():
    plst = [get_pipeline_stages(p) for p in PIPES]
    return plst


def disp_stages(pipe: ProcessingPipeline):
    r_str = ""
    for i, p in enumerate(pipe.stages):
        r_str += f"Stage {i + 1}: "
        r_str += p.process.__doc__
        r_str += "\n"
    return r_str


if __name__ == "__main__":
    nman = NexusManager()
    print("\nCreating Data Processing Pipeline...")
    get_pipes()
    print(disp_stages(PIPES["json"]))
    dct = {**DATA}
    print("=== Multi-Format Data Processing ===\n")
    nman.add_pipeline_batch(PIPES)
    nman.process_data(dct)
