#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    nexus_pipeline.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/23 05:35:28 by maprunty         #+#    #+#              #
#    Updated: 2026/02/27 22:08:11 by maprunty        ###   ########.fr        #
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
        proc_str = '\n'
        proc_str += "Input:"
        proc_str += "Real-time sensor stream" if data["id"] == "Stream" else str(data["data"]) 
        data["proc_str"] = proc_str
        data["chain_strs"] = ["Raw"]
        return data


class TransformStage:
    """Transform:."""

    T_STRS = {
        "json": "Enriched with metadata and validation",
        "csv": "Parsed and structured data",
        "stream": "Aggregated and filtered",
    }

    def process(self, data: Any) -> dict:
        """Data transformation and enrichment"""
        r_dct = data
        proc_str = '\n'
        proc_str += "Transform: "
        proc_str += self.T_STRS[r_dct["id"]]
        data["proc_str"] += proc_str
        data["chain_strs"] += ["Processed"]
        return r_dct


class OutputStage:
    """Output:."""

    O_STRS = {
        "json": (
            lambda dct: f"Processed temperature reading: {dct['value']}°{dct['unit']} (Normal range)"
        ),
        "csv": (
            lambda lst: f"User activity logged: {len(lst)} actions processed"
        ),
        "stream": lambda lst_dct: f"Stream summary: {len(lst_dct)} readings, avg: {sum(dct['value'] for dct in lst_dct) / len(lst_dct)}°C",
    }

    def process(self, data: Any) -> str:
        """Output formatting and delivery"""
        r_dct = data
        # print(r_dct)
        d = r_dct["data"]
        proc_str = '\n'
        proc_str += "Output:"
        proc_str += self.O_STRS[r_dct["id"]](d)
        data["proc_str"] += proc_str
        data["chain_strs"] += ["Analysed"]
        return r_dct


class ProcessingPipeline(ABC):
    """ProcessingPipe."""
    PIPE_METRICS = {"chain": 0}

    def __init__(self) -> None:
        self.stages: list[ProcessingStage] = []
        self.PIPE_METRICS[self.pipeline_id] = None
        self.r_str = (
            f"Processing {self.__doc__.split(' ')[0]} data through pipeline..."
        )
        self.log_str = ""

    @abstractmethod
    def process(self, data: Any) -> Any:
        result = {}
        # print(data)
        #self.log()
        print(data)
        if not "id"  in data.keys():
            d = {"id": self.pipeline_id, "data": data}
        # result[self.pipeline_id] = {key: None for key in self.stages}
        for s in self.stages:
            print("proc", s.process(d))
            print("dct", d)
            # result[self.pipeline_id][s] = s.process(d)
            # print(result)
        self.PIPE_METRICS[self.pipeline_id] = result
        return result

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def log(self, name=__doc__):
        """Log string:."""
        self.PIPE_METRICS["chain"] += 1 
        self.log_str += f"> {name} >> {self.log.__doc__} >>>  {self.__doc__}"
        self.log_str += f"{(' -> '.join(s.__doc__ for s in self.stages))}"
        return name


# Adapters
class JSONAdapter(ProcessingPipeline):
    """JSON Adapter."""

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id.lower()
        super().__init__()

    def process(self, data: Any) -> Any:
        return super().process(data)


class CSVAdapter(ProcessingPipeline):
    """CSV Adapter."""

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id.lower()
        super().__init__()

    def process(self, data: Any) -> Any:
        data = {i: entry for i, entry in enumerate(data.split("\n"))}
        r = super().process(data)
        return r


class StreamAdapter(ProcessingPipeline):
    """Stream Adapter."""

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id.lower()
        super().__init__()

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
        self.dct_pipelines: dict[str, ProcessingPipeline] = {}
        self.cap = 1000
        print(f"Pipeline capacity: {self.cap} streams/second")

    def analyse_res(self, result: dict[str, str]):
        pass


    def read_data(self):
        for i, v in self.dct_pipelines.items():
            print(i, v.keys())
            print(v["result"].keys())
                #print(self.dct_pipelines["result"].keys())
                #print(self.dct_pipelines["result"]["JSON"].keys())
        pass

    def process_data(self, data: Any) -> dict[any, any]:
        result = {}
        #try:
        if isinstance(data, dict) and any(key in ADAPTERS for key in data):
            result = {key: None for key in data}
            # print(data.items())
            for k, v in data.items():
                pipe = self.dct_pipelines[k]['adapter']
                self.dct_pipelines[k]["result"] = pipe.process(v)[k]
                self.dct_pipelines[k]["metrics"]= pipe.PIPE_METRICS
        else:
            result = {"ERROR:": "wrong shape"}
            raise
        #except Exception as e:
        #    print(result, e)
        return result

    def process_chain(self, data: Any, key):
        #for i in CHAIN_PIPES:
        #    print(self.i)
        a = {p.pipeline_id: p for p in self.pipelines if key in p.pipeline_id}
        print(a)

    def process_batch(self, data: Any ):
        pass

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)
        self.dct_pipelines[pipeline.pipeline_id.lower()] = {}
        p_dct = self.dct_pipelines[pipeline.pipeline_id.lower()]
        p_dct["adapter"] = pipeline
        p_dct["result"] = None
        p_dct["metrics"] = None

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
CHAIN_PIPES = ["Pipeline A", "Pipeline B", "Pipeline C"]


def get_pipeline_stages(pipes: dict[str, ProcessingPipeline]) -> ProcessingPipeline:
    [pipes.add_stage(s()) for s in STAGES]
    return pipes


def get_pipes()-> dict[str, ProcessingPipeline]:
    r_dct = {k:None for k in ADAPTERS}
    tmp = None
    for a in ADAPTERS:
        r_dct[a] = ADAPTERS[a](a)
        get_pipeline_stages(r_dct[a])
    return r_dct 


def disp_stages(pipe: ProcessingPipeline):
    r_str = ""
    for i, p in enumerate(pipe.stages):
        r_str += f"Stage {i + 1}: "
        r_str += p.process.__doc__
        r_str += "\n"
    return r_str


def chain_demo() -> dict[str, ProcessingPipeline]:
    r_dct = {k:None for k in CHAIN_PIPES}
    for p in r_dct:
        r_dct[p] = ADAPTERS["json"](p)
        get_pipeline_stages(r_dct[p])
    return r_dct
    # r_plst =


if __name__ == "__main__":
    nman = NexusManager()
    print("\nCreating Data Processing Pipeline...")
    pipes = get_pipes()
    print(disp_stages(pipes["json"]))
    dct = {**DATA}
    print("=== Multi-Format Data Processing ===\n")
    nman.add_pipeline_batch(pipes)
    nman.process_data(dct)
    nman.read_data()
    print("=== Pipeline Chaining Demo ===\n")
    nman.add_pipeline_batch(chain_demo())
    nman.process_chain({"stream":dct["stream"]}, "PIPELINE")

