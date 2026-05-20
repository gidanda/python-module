from typing import Any, Protocol, TypeAlias
from abc import ABC, abstractmethod

NumericData: TypeAlias = int | float | list[int | float]
TextData: TypeAlias = str | list[str]
LogEntry: TypeAlias = dict[str, str]
LogData: TypeAlias = LogEntry | list[LogEntry]
StoredItem: TypeAlias = tuple[int, str]



class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[StoredItem] = []
        self._rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> StoredItem:
        return self._data.pop(0)
    
    def _store(self, value: str) -> None:
        self._data.append((self._rank, value))
        self._rank += 1

    def get_total_processed(self) -> int:
        return self._rank
    
    def get_remaining_count(self) -> int:
        return len(self._data)

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False    

    def ingest(self, data: NumericData) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        
        if isinstance(data, list):
            for item in data:
                self._store(str(item))
        else:
            self._store(str(data))

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False
    
    def ingest(self, data: TextData) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        
        if isinstance(data, list):
            for item in data:
                self._store(item)

        else:
            self._store(data)
    
class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return (
                isinstance(data.get("log_level"), str)
                and isinstance(data.get("log_message"), str)
            )

        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                if not isinstance(item.get("log_level"), str):
                    return False
                if not isinstance(item.get("log_message"), str):
                    return False
            return True

        return False

    def ingest(self, data: LogData) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        
        if isinstance(data, list):
            for item in data:
                self._store(
                    f"{item['log_level']}: {item['log_message']}"
                )
        else:
            self._store(
                f"{data['log_level']}: {data['log_message']}"
            )

class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...

class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = []

        for _, value in data:
            values.append(value)

        print("CSV Output:")
        print(",".join(values))
    
class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        parts = []

        for rank, value in data:
            parts.append(f'"item_{rank}": "{value}')

        print("JSON Output:")
        print("{" + ", ".join(parts) + "}")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False

            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
                    break
            
            if not processed:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def _processor_name(self, processor: DataProcessor) -> str:
        name = processor.__class__.__name__
        return name.replace("Processor", " Processor")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            print(
                f"{self._processor_name(processor)}: "
                f"total {processor.get_total_processed()} items processed, "
                f"remaining {processor.get_remaining_count()} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            output_data: list[tuple[int, str]] = []

            for _ in range(nb):
                if processor.get_remaining_count() == 0:
                    break
                output_data.append(processor.output())
                
                if output_data:
                    plugin.process_output(output_data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...\n")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Processors\n")
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())

    first_batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {first_batch}\n")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()

    print(f"\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVExportPlugin())

    data_stream.print_processors_stats()

    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"\nSend another batch of data: {second_batch}\n")
    data_stream.process_stream(second_batch)
    data_stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONExportPlugin())

    data_stream.print_processors_stats()
