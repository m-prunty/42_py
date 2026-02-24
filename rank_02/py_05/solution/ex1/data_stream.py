#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    data_stream.py                                    :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 01:02:28 by maprunty         #+#    #+#              #
#    Updated: 2026/02/24 03:43:09 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod
from typing import Any


class DataStream(ABC):
    """TODO: Docstring."""

    stype = None
    dtype = None

    def init_s(self, stream_id: str) -> None:
        self.init_str = f"Initializing {self.stype.capitalize()} Stream...\n"
        self.init_str += f"Stream ID: {stream_id}, Type: {self.dtype}\n"
        self.stats = {"ops": "", "info": "", "filter": ""}

    @abstractmethod
    def process_batch(self, data_batch: list[Any]) -> str:
        """Process a batch of data"""
        self.init_str += f"Processing {self.stype} batch: {data_batch}\n"
        self.init_str += (
            f"{self.stype.capitalize()} analysis: "
            + f"{self.stats['ops']}, "
            + f"{self.stats['info']}\n"
        )
        return

    def filter_data(
        self, data_batch: list[Any], criteria: str | None = None
    ) -> list[Any]:
        """Filter data based on criteria."""
        if isinstance(criteria, int):
            return [i for i in data_batch if int(i) >= int(criteria)]
        if len(data_batch[0].split(":")) > 1 and isinstance(criteria, str):
            criteria = criteria.split(", ")
            return [
                v
                for k, v in [i.split(":") for i in data_batch]
                if k in criteria
            ]
        if isinstance(criteria, str):
            return [i for i in data_batch if i == criteria]

    def get_stats(self) -> dict[str, str | int | float]:
        """Return stream statistics"""
        return self.stats


class SensorStream(DataStream):
    """TODO: doc."""

    stype = "sensor"
    dtype = "Environmental Data"

    def __init__(self, stream_id: str) -> None:
        """TODO: doc."""
        super().init_s(stream_id)

    def process_batch(self, data_batch: list[Any]) -> str:
        """Process a batch of data"""
        sdct = {}
        n = len(data_batch)
        for d in data_batch:
            k, v = d.split(":")
            v = float(v)
            sdct[k].append(v) if k in sdct else sdct.update({k: [v]})
        avg_t = sum(sdct["temp"]) / len(sdct["temp"]) if "temp" in sdct else 0
        f = super().filter_data(data_batch, "temp, humidity")
        self.stats["ops"] = f"{n} readings processed"
        self.stats["info"] = f"avg temp: {avg_t}°C"
        self.stats["filter"] = (
            f"{len(f)} critical sensor alert{'s'[: len(f) ^ 1]}" if f else ""
        )
        super().process_batch(data_batch)
        return


class TransactionStream(DataStream):
    """TODO: doc."""

    stype = "transaction"
    dtype = "Financial Data"

    def __init__(self, stream_id: str) -> None:
        """TODO: doc."""
        super().init_s(stream_id)

    def process_batch(self, data_batch: list[Any]) -> str:
        """Process a batch of data"""
        sdct = {}
        n = len(data_batch)
        for d in data_batch:
            k, v = d.split(":")
            v = float(v)
            sdct[k].append(v) if k in sdct else sdct.update({k: [v]})
        buy = sum(sdct["buy"]) if "buy" in sdct else 0
        sell = sum(sdct["sell"]) if "sell" in sdct else 0
        f = super().filter_data(sdct["buy"] + sdct["sell"], 200)
        net_flow = int(buy - sell)
        self.stats["ops"] = f"{n} operations"
        self.stats["info"] = (
            f"net flow: {'+' if net_flow >= 0 else '-'}{net_flow} units"
        )
        self.stats["filter"] = (
            f"{len(f)} large transaction{'s'[: len(f) ^ 1]}" if f else ""
        )
        super().process_batch(data_batch)
        return


class EventStream(DataStream):
    """TODO: doc."""

    stype = "event"
    dtype = "System Events"

    def __init__(self, stream_id: str) -> None:
        """TODO: doc."""
        super().init_s(stream_id)

    def process_batch(self, data_batch: list[Any]) -> str:
        """Process a batch of data"""
        n = len(data_batch)
        self.stats["filter"] = super().filter_data(data_batch, "error")
        nerr = len(self.stats["filter"]) if self.stats["filter"] else 0
        self.stats["ops"] = f"{n} events"
        self.stats["info"] = f"{nerr} error detected"
        super().process_batch(data_batch)
        return


class StreamProcessor:
    def __init__(self) -> None:
        self.slist: List[DataStream] = list()

    def print_inits(self) -> None:
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
        [print(f"{s.init_str}") for s in self.slist]

    def print_batch(self) -> str:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("\nBatch 1 Results:")
        [
            print(f"- {i.stype.capitalize()} data: {i.stats['ops']}")
            for i in self.slist
        ]
        print("\nStream filtering active: High-priority data only")
        print(
            f"""Filtered results: {
                ", ".join(
                    [
                        (str(i.stats["filter"]))
                        for i in self.slist
                        if i.stats["filter"]
                    ]
                )
            }"""
        )
        return (
            "\nAll streams processed successfully. Nexus throughput optimal."
        )

    def add_stream(self, stream_id: str, values: list) -> None:
        if "SENSOR" in stream_id:
            self.slist.append(SensorStream(stream_id))
        elif "TRANS" in stream_id:
            self.slist.append(TransactionStream(stream_id))
        elif "EVENT" in stream_id:
            self.slist.append(EventStream(stream_id))
        self.slist[-1].process_batch(values)

    def process_dict(self, dct: dict) -> None:
        for k, v in dct.items():
            self.add_stream(k, v)


dct1 = {
    "SENSOR_001": ["temp:22.5", "humidity:65", "pressure:1013"],
    "TRANS_001": ["buy:100", "sell:150", "buy:75"],
    "EVENT_001": ["login", "error", "logout"],
}
p = StreamProcessor()
p.process_dict(dct1)
p.print_inits()
dct2 = {
    "SENSOR_002": ["temp:22.5", "humidity:65"],
    "TRANS_002": ["buy:100", "sell:150", "buy:75", "buy:250"],
    "EVENT_002": ["login", "display", "logout"],
}
p = StreamProcessor()
p.process_dict(dct2)
print(p.print_batch())
