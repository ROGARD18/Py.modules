from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class StreamDataError(Exception):
    """Exception raised when data format in a stream is invalid."""
    pass


class StreamExistsError(Exception):
    """Exception raised when attempting to add a stream with a duplicate ID."""
    pass


class DataStream(ABC):
    """
    Abstract base class for all data streams in the Nexus system.
    Provides core functionality for filtering and statistical reporting.
    """
    def __init__(self, stream_id: str):
        """Initialize the stream with a unique identifier and tracking
        metrics."""
        self.stream_id: str = stream_id
        self.processed: float = 0
        self.type: str

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a summary string."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter the data batch based on a simple string matching criteria."""
        if criteria is None:
            return data_batch

        list_result: list[Any] = []
        for elem in data_batch:
            if isinstance(elem, str) and criteria in elem:
                list_result.append(elem)
        return list_result

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return a dictionary containing basic stream performance metrics."""
        return {
            "STREAM_ID": self.stream_id,
            "TYPE": self.type,
            "PROCESSED": self.processed
        }


class SensorStream(DataStream):
    """Stream processor for environmental sensor data (temperature,
    humidity)."""
    def __init__(self, stream_id: str):
        """Initialize sensor stream and average temperature tracker."""
        super().__init__(stream_id=stream_id)
        self.type: str = "Environmental Data"
        self.avg_temp: float = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Parse temperature readings and update the moving average."""
        temp: float = 0
        nb_temp: int = 0
        for elem in data_batch:
            if not isinstance(elem, str):
                raise StreamDataError(f"{elem} is not of type str")
            if elem == "":
                raise StreamDataError("Empty element in data_batch")
            data: tuple[str, str] = elem.split(":")
            if data[0] == "temp":
                temp += float(data[1])
                nb_temp += 1
            self.processed += 1
        if nb_temp > 0:
            self.avg_temp = temp / nb_temp
        result: str = f"Sensor analysus: {self.processed} reading"
        return result + f" processed, avg temp: {self.avg_temp:2.f}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter sensor data for critical thresholds (temp > 40 or
        humidity > 90)."""
        if criteria is None:
            return data_batch
        if criteria != "critical":
            return super().filter_data(data_batch)
        filtered: List[Any] = []
        for elem in data_batch:
            if not isinstance(elem, str):
                raise StreamDataError(f"{elem} is not of type str")
            if elem == "":
                raise StreamDataError("empty element in data_batch")
            data: tuple[str, str] = elem.split(":")
            if data[0] == "temp":
                if float(data[1]) > 40:
                    filtered = filtered + [elem]
            elif data[0] == "humidity":
                if int(data[1]) > 90:
                    filtered = filtered + [elem]
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream stats including the current average temperature."""
        stats: Dict[str, str | int | float] = super().get_stats()
        stats.update({"AVG_TEMP": self.avg_temp})
        return stats


class TransactionStream(DataStream):
    """Stream processor for financial transaction data (buy/sell)."""
    def __init__(self, stream_id: str) -> None:
        """Initialize transaction stream and net flow tracker."""
        super().__init__(stream_id)
        self.type = "Financial Data"
        self.net_flow: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Calculate the net flow based on buys and sells in the batch."""
        buys: int = 0
        sells: int = 0
        for elem in data_batch:
            if not isinstance(elem, str):
                raise StreamDataError(f"{elem} is not of type str")
            if elem == "":
                raise StreamDataError("empty element in data_batch")
            data: tuple[str, str] = elem.split(":")
            if data[0] != "buy" and data[0] != "sell":
                raise StreamDataError(f"transaction data '{data[0]} 'is not of"
                                      " type 'buy' or 'sell'")
            if data[0] == "buy":
                buys += int(data[1])
            else:
                sells += int(data[1])
            self.processed += 1
        self.net_flow: int = buys - sells
        result: str = f"Transaction analysis: {self.processed} operation"
        return result + f", net flow: {self.net_flow:+}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter transactions based on priority thresholds."""
        if criteria is None:
            return data_batch
        if criteria != "high-priority":
            return super().filter_data(data_batch)
        filtered: List[Any] = []
        for elem in data_batch:
            if not isinstance(elem, str):
                raise StreamDataError(f"{elem} is not of type str")
            if elem == "":
                raise StreamDataError("empty element in data_batch")
            data: tuple[str, str] = elem.split(":")
            if data[0] != "buy" and data[0] != "sell":
                raise StreamDataError(f"transaction data '{data[0]} 'is not of"
                                      " type 'buy' or 'sell'")
            if data[0] == "buy" and int(data[1]) < 100:
                filtered = filtered + [elem]
            elif int(data[1]) > 500:
                filtered = filtered + [elem]
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream stats including the current net financial flow."""
        stats: Dict[str, str | int | float] = super().get_stats()
        stats.update({"NET_FLOW": self.net_flow})
        return stats


class EventStream(DataStream):
    """Stream processor for system-level events and error logging."""
    def __init__(self, stream_id: str) -> None:
        """Initialize event stream and error counter."""
        super().__init__(stream_id)
        self.type = "System Events"
        self.errors: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Identify error strings in the batch and update error counts."""
        for elem in data_batch:
            if not isinstance(elem, str):
                raise StreamDataError(f"{elem} is not of type str")
            if elem == "":
                raise StreamDataError("empty element in data_batch")
            if elem == "error":
                self.errors += 1
            self.processed += 1
        result: str = f"Event analysis: {self.processed} event"
        result += f", {self.errors} error"
        return result + " detected"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Extract only critical error events from the batch."""
        if criteria is None:
            return data_batch
        if criteria != "critical":
            return super().filter_data(data_batch)
        filtered: List[Any] = []
        for elem in data_batch:
            if not isinstance(elem, str):
                raise StreamDataError(f"{elem} is not of type str")
            if elem == "":
                raise StreamDataError("empty element in data_batch")
            if elem == "error":
                filtered = filtered + [elem]
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream stats including the total number of errors
        detected."""
        stats: Dict[str, str | int | float] = super().get_stats()
        stats.update({"ERRORS": self.errors})
        return stats


class StreamProcessor():
    """Manager class to handle multiple data streams through a
    unified interface."""
    def __init__(self) -> None:
        """Initialize the processor with an empty registry of streams."""
        self.streams: List[DataStream] = []

    def add_stream(self, new_stream: DataStream) -> None:
        """Add a new stream to the registry, ensuring ID uniqueness."""
        for stream in self.streams:
            if stream.stream_id == new_stream.stream_id:
                raise StreamExistsError(f"stream_id '{new_stream.stream_id}'"
                                        "already exists")
        self.streams = self.streams + [new_stream]


def main() -> None:
    """Diagnostic routine for testing polymorphic stream
    processing and filtering."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor_stream: SensorStream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor_stream.stream_id}, Type: {sensor_stream.type}")
    sensor_stream_data: List[str] = ["temp:22.5", "humidity:65",
                                     "pressure:1013"]
    print(f"Processing sensor batch: {sensor_stream_data}")
    try:
        print(sensor_stream.process_batch(sensor_stream_data))
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")

    print("")
    print("Initializing Transaction Stream...")
    trans_stream: TransactionStream = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans_stream.stream_id}, Type: {trans_stream.type}")
    trans_stream_data: List[str] = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {trans_stream_data}")
    try:
        print(trans_stream.process_batch(trans_stream_data))
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")

    print("")
    print("Initializing Event Stream...")
    event_stream: EventStream = EventStream("EVENT_001")
    print(f"Stream ID: {event_stream.stream_id}, Type: {event_stream.type}")
    event_stream_data: List[str] = ["login", "error", "logout"]
    print(f"Processing event batch: {event_stream_data}")
    try:
        print(event_stream.process_batch(event_stream_data))
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")

    print("")
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    stream_processor = StreamProcessor()
    streams: dict[str, DataStream] = {
        "SENSOR_001":
            (SensorStream("SENSOR_001"), ["temp:22.5", "temp:50"]),
        "TRANS_001":
            (TransactionStream("TRANS_001"), ["buy:100", "sell:150",
                                              "buy:75", "buy:500"]),
        "EVENT_001":
            (EventStream("EVENT_001"), ["login", "error", "logout"])
    }
    for key in streams:
        stream_processor.add_stream(streams[key][0])
    print("\nBatch 1 Results:")
    for stream in stream_processor.streams:
        try:
            stream.process_batch(streams[stream.stream_id][1])
            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {stream.processed} reading", end="")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {stream.processed} operation",
                      end="")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {stream.processed} event", end="")
            print(" processed")
        except Exception as e:
            print("Caught error in the stream processor, skipping stream")
            print(f"{e.__class__.__name__}: {e}")

    print("\nStream filtering active: High-priority data only")
    filtered_results: Dict[str, int] = {
        "critical": 0,
        "high-priority": 0
    }
    print("Filtered results: ", end="")
    for stream in stream_processor.streams:
        filtered: List[Any] = []
        is_transaction: bool = isinstance(stream, TransactionStream)
        try:
            if is_transaction:
                filtered = stream.filter_data(streams[stream.stream_id][1],
                                              "high-priority")
            else:
                filtered = stream.filter_data(streams[stream.stream_id][1],
                                              "critical")
            for _ in filtered:
                if is_transaction:
                    filtered_results["high-priority"] += 1
                else:
                    filtered_results["critical"] += 1
        except Exception as e:
            print("Caught error in the stream processor, skipping stream")
            print(f"{e.__class__.__name__}: {e}")
    print(f"{filtered_results['critical']} critical sensor alert", end="")
    if filtered_results["critical"] > 1:
        print("s", end="")
    print(f", {filtered_results['high-priority']} large transaction", end="")
    if filtered_results["high-priority"] > 1:
        print("s", end="")
    print()
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
