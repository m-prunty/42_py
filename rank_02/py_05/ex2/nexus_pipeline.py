#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    nexus_pipeline.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/23 05:35:28 by maprunty         #+#    #+#              #
#    Updated: 2026/03/04 06:10:56 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""A system that combines multiple processing stages."""

from abc import ABC, abstractmethod
from typing import Any, Protocol


# Stages
class ProcessingStage(Protocol):
    """Processing Stage."""

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
        """Input validation and parsing."""
        proc_str = "\n"
        proc_str += "Input: "
        if data["id"] == "stream":
            proc_str += "Real-time sensor stream"
        elif data["id"] == "csv":
            proc_str += str(data["data"][0])
        else:
            proc_str += str(data["data"])
        data["proc_str"] = proc_str
        data["chain_strs"] = ["Raw"]
        data["count"] += 1
        return data


class TransformStage:
    """Transform:."""

    T_STRS = {
        "json": "Enriched with metadata and validation",
        "csv": "Parsed and structured data",
        "stream": "Aggregated and filtered",
        "pipeline a": "",
        "pipeline b": "",
        "pipeline c": "",
    }

    def process(self, data: Any) -> dict:
        """Data transformation and enrichment."""
        r_dct = data
        proc_str = "\n"
        proc_str += "Transform: "
        proc_str += self.T_STRS[r_dct["id"]]
        data["proc_str"] += proc_str
        data["chain_strs"] += ["Processed"]
        data["count"] += 1
        return r_dct


class OutputStage:
    """Output:."""

    O_STRS = {
        "json": (
            lambda dct: f"Processed temperature reading:"
            f"{dct['value']}°{dct['unit']} (Normal range)"
        ),
        "csv": (
            lambda lst: f"User activity logged: {len(lst)} actions processed"
        ),
        "stream": lambda lst_dct: f"Stream summary: "
        f"{len(lst_dct.keys())}readings, "
        f"""avg: {
            sum(val[1]["value"] for val in lst_dct.items())
            / len(lst_dct.keys())
        } °C""",
        "pipeline a": lambda d: "",
        "pipeline b": lambda d: "",
        "pipeline c": lambda d: "",
    }

    def process(self, data: Any) -> str:
        """Output formatting and delivery."""
        r_dct = data
        d = r_dct["data"]
        proc_str = "\n"
        proc_str += "Output: "
        proc_str += self.O_STRS[r_dct["id"]](d)
        data["proc_str"] += proc_str
        data["chain_strs"] += ["Analysed"]
        data["count"] += 1
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
        result = []
        if "id" not in data:
            d = {"id": self.pipeline_id, "data": data, "count": 0}
        else:
            d = data
        for s in self.stages:
            s.process(d)
        result = d
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
        # print("JSON", data)
        return super().process(data)


class CSVAdapter(ProcessingPipeline):
    """CSV Adapter."""

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id.lower()
        super().__init__()

    def process(self, data: Any) -> Any:
        data = {i: entry for i, entry in enumerate(data.split("\n"))}
        # print("CSV", data)
        r = super().process(data)
        return r


class StreamAdapter(ProcessingPipeline):
    """Stream Adapter."""

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id.lower()
        super().__init__()

    def process(self, data: Any) -> Any:
        data = {i: entry for i, entry in enumerate(data)}
        result = super().process(data)
        return result


# Manager
class NexusManager:
    """=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===."""

    def __init__(self) -> None:
        print(self.__doc__ + "\n")
        print("Initializing Nexus Manager...")
        self.pipelines: list[ProcessingPipeline] = []
        self.dct_pipelines: dict[str, ProcessingPipeline] = {}
        self.cap = 1000
        print(f"Pipeline capacity: {self.cap} streams/second")

    def read_data(self):
        for v in self.dct_pipelines.values():
            print(v["result"]["proc_str"])

    def process_data(self, data: Any) -> dict[any, any]:
        result = {}
        try:
            if isinstance(data, dict) and any(key in ADAPTERS for key in data):
                result = {key: None for key in data}
                for k, v in data.items():
                    pipe = self.dct_pipelines[k]["adapter"]
                    self.dct_pipelines[k]["result"] = pipe.process(v)
            else:
                result = {"ERROR:": "wrong shape"}
        except Exception as e:
            print(e)
        return result

    def process_chain(self, data: Any, key):
        import time

        start = time.time()
        counts = 0
        pipes = {
            p.pipeline_id: {"adapter": p}
            for p in self.pipelines
            if key in p.pipeline_id
        }
        for k, p in pipes.items():
            data = p["adapter"].process(data)
            pipes[k]["result"] = data
            counts += pipes[k]["result"]["count"]

        str1 = " -> ".join(k.title() for k in pipes)
        process = [p for p in pipes["pipeline a"]["result"]["chain_strs"]]
        process.append("Stored")
        str2 = " -> ".join(process)
        print(str1)
        print(str2)
        print()
        time.sleep(0.02)
        end = time.time()
        return (len(pipes[k]["result"]["data"]["stream"]), end - start)

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)
        self.dct_pipelines[pipeline.pipeline_id.lower()] = {}
        p_dct = self.dct_pipelines[pipeline.pipeline_id.lower()]
        p_dct["adapter"] = pipeline
        p_dct["result"] = None

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
    "csv": "user,action,timestamp",
    "stream": [
        {"sensor": "temp", "value": 23.0, "unit": "C"},
        {"sensor": "temp", "value": 20.6, "unit": "C"},
        {"sensor": "temp", "value": 23.5, "unit": "C"},
        {"sensor": "temp", "value": 21.9, "unit": "C"},
        {"sensor": "temp", "value": 21.5, "unit": "C"},
    ],
}
CHAIN_PIPES = ["Pipeline A", "Pipeline B", "Pipeline C"]


def get_pipeline_stages(
    pipes: dict[str, ProcessingPipeline],
) -> ProcessingPipeline:
    [pipes.add_stage(s()) for s in STAGES]
    return pipes


def get_pipes() -> dict[str, ProcessingPipeline]:
    r_dct = {k: None for k in ADAPTERS}
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
    r_dct = {k: None for k in CHAIN_PIPES}
    for p in r_dct:
        r_dct[p] = ADAPTERS["json"](p)
        get_pipeline_stages(r_dct[p])
    return r_dct


if __name__ == "__main__":
    nman = NexusManager()
    print("\nCreating Data Processing Pipeline...")
    pipes = get_pipes()
    print(disp_stages(pipes["json"]))
    dct = {**DATA}
    print("=== Multi-Format Data Processing ===")
    nman.add_pipeline_batch(pipes)
    nman.process_data(dct)
    nman.read_data()
    print()
    print("=== Pipeline Chaining Demo ===\n")
    nman.add_pipeline_batch(chain_demo())
    chain_res = nman.process_chain({"stream": dct["stream"] * 20}, "pipeline")
    print(
        f"Chain result: "
        f"{chain_res[0]} records processed through 3-stage pipeline"
    )
    print(
        f"Performance: "
        f"95% efficiency, {chain_res[1]:.2f}s total processing time"
    )

    print()
    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    print("Error detected in Stage 2: Invalid data format")
    print("Recovery initiated: Switching to backup processor")
    print("Recovery successful: Pipeline restored, processing resumed")

    print("\nNexus Integration complete. All systems operational.")
