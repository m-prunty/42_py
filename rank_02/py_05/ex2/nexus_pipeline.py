#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    nexus_pipeline.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/23 05:35:28 by maprunty         #+#    #+#              #
#    Updated: 2026/02/25 14:13:44 by maprunty        ###   ########.fr        #
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
        r_dct = data
        self.log()
        print(self.process.__doc__) 
        return r_dct


class TransformStage:
    """Transform:."""

    def process(self, data: Any) -> dict:
        """Data transformation and enrichment"""
        r_dct = data
        print(self.process.__doc__) 
        return r_dct


class OutputStage:
    """Output:."""

    def process(self, data: Any) -> str:
        """Output formatting and delivery"""
        r_dct = data
        print(self.process.__doc__) 
        return r_dct


class ProcessingPipeline(ABC):
    """ProcessingPipe."""
    def __init__(self) -> None:
        self.stages: list[ProcessingStage] = []

    @abstractmethod
    def process(self, data: Any) -> Any:
        print(self.__doc__)
        for s in self.stages:
            print(s.process)
        return data

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def log(self, name=__doc__):
        """Log string:."""
        print(">", name, ">>", self.log.__doc__, ">>>", self.__doc__) 
        print(", ".join(s.__doc__ for s in self.stages))
        return name


# Adapters
class JSONAdapter(ProcessingPipeline):
    """JSON Adapter."""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        print(self.__doc__) 
        
    def process(self, data: Any) -> Any:
        super().log()
        for s in self.stages:
            print(s)
        return super().process(data)


class CSVAdapter(ProcessingPipeline):
    """CSV Adapter."""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        print(self.__doc__) 

    def process(self, data: Any) -> Any:

        return super().process(data)


class StreamAdapter(ProcessingPipeline):
    """Stream Adapter."""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        print(self.__doc__) 

    def process(self, data: Any) -> Any:
        return super().process(data)


# Manager
class NexusManager:
    """=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ==="""

    def __init__(self) -> None:
        print(self.__doc__ + '\n')
        print("Initializing Nexus Manager...")
        self.pipelines: List[ProcessingPipeline] = []
        self.metrics = {}
        self.cap = 1000
        print(f"Pipeline capacity: {self.cap} streams/second")

    def process_data(self, data: Any) -> None:
        result = []
        print(self.pipelines[0].stages)
        for pipe in self.pipelines:
            result.append(pipe.process(data))
        print(result)

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

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

def get_pipeline_stages(adapt_type: str) -> ProcessingPipeline:
    pipe = PIPES[adapt_type.lower()]
    print(pipe)
    for s in STAGES:
        print(s)
        pipe.add_stage(s)
    return pipe 

def disp_stages(pipe: ProcessingPipeline):
    for i, p in enumerate(pipe.stages):
        print(f"Stage {i + 1}:", end=" ")
        print(p.__doc__)

if __name__ == "__main__":
    json = {"sensor": "temp", "value": 23.5, "unit": "C"}
    csv = "user,action,timestamp"

    nman = NexusManager()
    print("\nCreating Data Processing Pipeline...")
    jpipe = get_pipeline_stages("json")
    print(disp_stages(jpipe))
    cpipe = get_pipeline_stages("csv")
    spipe = get_pipeline_stages("stream")
    nman.add_pipeline(jpipe)
    print("=== Multi-Format Data Processing ===")
    nman.process_data(json)


